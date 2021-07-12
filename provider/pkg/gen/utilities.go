// Copyright 2016-2021, Pulumi Corporation.

package gen

import (
	"fmt"
	"github.com/gedex/inflector"
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/pkg/v3/codegen"
	"github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"regexp"
	"strings"
)

var s = codegen.NewStringSet()

// apiParamNameToSdkName returns an SDK name for a given API parameter name.
// In particular, it converts pluralized ID names to singular ID names.
func apiParamNameToSdkName(name string) string {
	if strings.HasSuffix(name, "Id") {
		name = inflector.Singularize(name[:len(name)-2])
		switch name {
		case "project", "location", "managedZone":
			return name
		case "datum":
			return "dataId"
		default:
			return name + "Id"
		}
	}
	return name
}

// apiPropNameToSdkName returns an SDK name for a given API property name.
// In particular, it converts pluralized ID names to singular ID names.
func apiPropNameToSdkName(name string) string {
	switch name {
	case "projectId", "locationId", "managedZoneId":
		return name[:len(name)-2]
	default:
		return ToLowerCamel(name)
	}
}

// nameRegexes is a list of regular expressions to match property formats in property descriptions.
var nameRegexes = []*regexp.Regexp {
	// Example: "The resource name in the format `foo/*`"
	regexp.MustCompile(`(?:Format|format|form|forms|formatted|pattern|Example|example|e\.g\.|such|Structured)(?: (?:of|is|as|like|will be))?[^\w]+(\w+(?:/[\w\{\}\*-\[\]]*)+)`),
	// Example: "Must be in `projects/{project}/locations/{location}/triggers/{trigger}` format"
	regexp.MustCompile(`in[^\w]+(\w+(?:/[\w\{\}\*-\[\]]*)+)[^\w]+format`),
}

// namePropertyPattern extracts the pattern to build the name property for the given resource's property specs.
// It uses the descriptions of a property called 'name' and parses it to find a pattern of an example usage.
// Returns an error if no 'name' property or if its description failed to parse.
func namePropertyPattern(inputProperties map[string]schema.PropertySpec) (string, error) {
	nameProp, has := inputProperties["name"]
	if !has {
		return "", errors.New("no 'name' property")
	}

	if !strings.Contains(nameProp.Description, "/") {
		return "{name}", nil
	}

	var match string
	for _, nameRegex := range nameRegexes {
		matches := nameRegex.FindStringSubmatch(nameProp.Description)
		if len(matches) == 2 {
			match = matches[1]
			break
		}
	}

	if match == "" {
		return "", errors.New("name pattern not found in property description")
	}

	parts := strings.Split(match, "/")
	if len(parts) == 0 || len(parts)%2 == 1 {
		return "", errors.Errorf("pattern of %d parts in description is not supported", len(parts))
	}

	var res []string
	for i := 0; i < len(parts)-2; i+=2 {
		part := parts[i]
		val := apiParamNameToSdkName(part + "Id")
		if _, ok := inputProperties[val]; ok {
			res = append(res, fmt.Sprintf("%s/{%s}", part, val))
		} else {
			return "", errors.Errorf("unknown property %q in description", val)
		}
	}
	res = append(res, fmt.Sprintf("%s/{name}", parts[len(parts)-2]))

	return strings.Join(res, "/"), nil
}

// ToLowerCamel converts a string to lowerCamelCase.
// The code is adopted from https://github.com/iancoleman/strcase but changed in several ways to handle
// all the cases that are found in API specs in a most user-friendly way.
func ToLowerCamel(s string) string {
	if s == "" {
		return s
	}
	if r := rune(s[0]); r == '_' {
		s = s[1:]
	}
	for _, acronym := range uppercaseAcronyms {
		if strings.HasPrefix(s, acronym) {
			s = strings.ToLower(acronym) + strings.TrimPrefix(s, acronym)
		}
	}
	if r := rune(s[0]); r >= 'A' && r <= 'Z' {
		s = strings.ToLower(string(r)) + s[1:]
	}
	return toCamelInitCase(s, false)
}

// ToUpperCamel converts a string to UpperCamelCase.
func ToUpperCamel(s string) string {
	return toCamelInitCase(s, true)
}

func toCamelInitCase(s string, initCase bool) string {
	if s == strings.ToUpper(s) {
		// lowercase the UPPER_SNAKE_CASE
		s = strings.ToLower(s)
	}

	s = strings.Trim(s, " ")
	n := ""
	capNext := initCase
	for _, v := range s {
		if v >= 'A' && v <= 'Z' {
			n += string(v)
		}
		if v >= '0' && v <= '9' {
			n += string(v)
		}
		if v >= 'a' && v <= 'z' {
			if capNext {
				n += strings.ToUpper(string(v))
			} else {
				n += string(v)
			}
		}
		if v == '_' || v == ' ' || v == '-' || v == '.' {
			capNext = true
		} else {
			capNext = false
		}
	}
	return n
}

var uppercaseAcronyms = []string{
	"IP",
}
