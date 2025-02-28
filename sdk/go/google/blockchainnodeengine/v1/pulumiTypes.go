// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package v1

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-google-native/sdk/go/google/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

// The connection information through which to interact with a blockchain node.
type ConnectionInfoResponse struct {
	// The endpoint information through which to interact with a blockchain node.
	EndpointInfo EndpointInfoResponse `pulumi:"endpointInfo"`
	// A service attachment that exposes a node, and has the following format: projects/{project}/regions/{region}/serviceAttachments/{service_attachment_name}
	ServiceAttachment string `pulumi:"serviceAttachment"`
}

// The connection information through which to interact with a blockchain node.
type ConnectionInfoResponseOutput struct{ *pulumi.OutputState }

func (ConnectionInfoResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionInfoResponse)(nil)).Elem()
}

func (o ConnectionInfoResponseOutput) ToConnectionInfoResponseOutput() ConnectionInfoResponseOutput {
	return o
}

func (o ConnectionInfoResponseOutput) ToConnectionInfoResponseOutputWithContext(ctx context.Context) ConnectionInfoResponseOutput {
	return o
}

// The endpoint information through which to interact with a blockchain node.
func (o ConnectionInfoResponseOutput) EndpointInfo() EndpointInfoResponseOutput {
	return o.ApplyT(func(v ConnectionInfoResponse) EndpointInfoResponse { return v.EndpointInfo }).(EndpointInfoResponseOutput)
}

// A service attachment that exposes a node, and has the following format: projects/{project}/regions/{region}/serviceAttachments/{service_attachment_name}
func (o ConnectionInfoResponseOutput) ServiceAttachment() pulumi.StringOutput {
	return o.ApplyT(func(v ConnectionInfoResponse) string { return v.ServiceAttachment }).(pulumi.StringOutput)
}

// Contains endpoint information through which to interact with a blockchain node.
type EndpointInfoResponse struct {
	// The assigned URL for the node JSON-RPC API endpoint.
	JsonRpcApiEndpoint string `pulumi:"jsonRpcApiEndpoint"`
	// The assigned URL for the node WebSockets API endpoint.
	WebsocketsApiEndpoint string `pulumi:"websocketsApiEndpoint"`
}

// Contains endpoint information through which to interact with a blockchain node.
type EndpointInfoResponseOutput struct{ *pulumi.OutputState }

func (EndpointInfoResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointInfoResponse)(nil)).Elem()
}

func (o EndpointInfoResponseOutput) ToEndpointInfoResponseOutput() EndpointInfoResponseOutput {
	return o
}

func (o EndpointInfoResponseOutput) ToEndpointInfoResponseOutputWithContext(ctx context.Context) EndpointInfoResponseOutput {
	return o
}

// The assigned URL for the node JSON-RPC API endpoint.
func (o EndpointInfoResponseOutput) JsonRpcApiEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v EndpointInfoResponse) string { return v.JsonRpcApiEndpoint }).(pulumi.StringOutput)
}

// The assigned URL for the node WebSockets API endpoint.
func (o EndpointInfoResponseOutput) WebsocketsApiEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v EndpointInfoResponse) string { return v.WebsocketsApiEndpoint }).(pulumi.StringOutput)
}

// Ethereum-specific blockchain node details.
type EthereumDetails struct {
	// Immutable. Enables JSON-RPC access to functions in the `admin` namespace. Defaults to `false`.
	ApiEnableAdmin *bool `pulumi:"apiEnableAdmin"`
	// Immutable. Enables JSON-RPC access to functions in the `debug` namespace. Defaults to `false`.
	ApiEnableDebug *bool `pulumi:"apiEnableDebug"`
	// An Ethereum address which the beacon client will send fee rewards to if no recipient is configured in the validator client. See https://lighthouse-book.sigmaprime.io/suggested-fee-recipient.html or https://docs.prylabs.network/docs/execution-node/fee-recipient for examples of how this is used. Note that while this is often described as "suggested", as we run the execution node we can trust the execution node, and therefore this is considered enforced.
	BeaconFeeRecipient *string `pulumi:"beaconFeeRecipient"`
	// Immutable. The consensus client.
	ConsensusClient *EthereumDetailsConsensusClient `pulumi:"consensusClient"`
	// Immutable. The execution client
	ExecutionClient *EthereumDetailsExecutionClient `pulumi:"executionClient"`
	// Details for the Geth execution client.
	GethDetails *GethDetails `pulumi:"gethDetails"`
	// Immutable. The Ethereum environment being accessed.
	Network *EthereumDetailsNetwork `pulumi:"network"`
	// Immutable. The type of Ethereum node.
	NodeType *EthereumDetailsNodeType `pulumi:"nodeType"`
}

// EthereumDetailsInput is an input type that accepts EthereumDetailsArgs and EthereumDetailsOutput values.
// You can construct a concrete instance of `EthereumDetailsInput` via:
//
//	EthereumDetailsArgs{...}
type EthereumDetailsInput interface {
	pulumi.Input

	ToEthereumDetailsOutput() EthereumDetailsOutput
	ToEthereumDetailsOutputWithContext(context.Context) EthereumDetailsOutput
}

// Ethereum-specific blockchain node details.
type EthereumDetailsArgs struct {
	// Immutable. Enables JSON-RPC access to functions in the `admin` namespace. Defaults to `false`.
	ApiEnableAdmin pulumi.BoolPtrInput `pulumi:"apiEnableAdmin"`
	// Immutable. Enables JSON-RPC access to functions in the `debug` namespace. Defaults to `false`.
	ApiEnableDebug pulumi.BoolPtrInput `pulumi:"apiEnableDebug"`
	// An Ethereum address which the beacon client will send fee rewards to if no recipient is configured in the validator client. See https://lighthouse-book.sigmaprime.io/suggested-fee-recipient.html or https://docs.prylabs.network/docs/execution-node/fee-recipient for examples of how this is used. Note that while this is often described as "suggested", as we run the execution node we can trust the execution node, and therefore this is considered enforced.
	BeaconFeeRecipient pulumi.StringPtrInput `pulumi:"beaconFeeRecipient"`
	// Immutable. The consensus client.
	ConsensusClient EthereumDetailsConsensusClientPtrInput `pulumi:"consensusClient"`
	// Immutable. The execution client
	ExecutionClient EthereumDetailsExecutionClientPtrInput `pulumi:"executionClient"`
	// Details for the Geth execution client.
	GethDetails GethDetailsPtrInput `pulumi:"gethDetails"`
	// Immutable. The Ethereum environment being accessed.
	Network EthereumDetailsNetworkPtrInput `pulumi:"network"`
	// Immutable. The type of Ethereum node.
	NodeType EthereumDetailsNodeTypePtrInput `pulumi:"nodeType"`
}

func (EthereumDetailsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*EthereumDetails)(nil)).Elem()
}

func (i EthereumDetailsArgs) ToEthereumDetailsOutput() EthereumDetailsOutput {
	return i.ToEthereumDetailsOutputWithContext(context.Background())
}

func (i EthereumDetailsArgs) ToEthereumDetailsOutputWithContext(ctx context.Context) EthereumDetailsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EthereumDetailsOutput)
}

func (i EthereumDetailsArgs) ToEthereumDetailsPtrOutput() EthereumDetailsPtrOutput {
	return i.ToEthereumDetailsPtrOutputWithContext(context.Background())
}

func (i EthereumDetailsArgs) ToEthereumDetailsPtrOutputWithContext(ctx context.Context) EthereumDetailsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EthereumDetailsOutput).ToEthereumDetailsPtrOutputWithContext(ctx)
}

// EthereumDetailsPtrInput is an input type that accepts EthereumDetailsArgs, EthereumDetailsPtr and EthereumDetailsPtrOutput values.
// You can construct a concrete instance of `EthereumDetailsPtrInput` via:
//
//	        EthereumDetailsArgs{...}
//
//	or:
//
//	        nil
type EthereumDetailsPtrInput interface {
	pulumi.Input

	ToEthereumDetailsPtrOutput() EthereumDetailsPtrOutput
	ToEthereumDetailsPtrOutputWithContext(context.Context) EthereumDetailsPtrOutput
}

type ethereumDetailsPtrType EthereumDetailsArgs

func EthereumDetailsPtr(v *EthereumDetailsArgs) EthereumDetailsPtrInput {
	return (*ethereumDetailsPtrType)(v)
}

func (*ethereumDetailsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**EthereumDetails)(nil)).Elem()
}

func (i *ethereumDetailsPtrType) ToEthereumDetailsPtrOutput() EthereumDetailsPtrOutput {
	return i.ToEthereumDetailsPtrOutputWithContext(context.Background())
}

func (i *ethereumDetailsPtrType) ToEthereumDetailsPtrOutputWithContext(ctx context.Context) EthereumDetailsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EthereumDetailsPtrOutput)
}

// Ethereum-specific blockchain node details.
type EthereumDetailsOutput struct{ *pulumi.OutputState }

func (EthereumDetailsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EthereumDetails)(nil)).Elem()
}

func (o EthereumDetailsOutput) ToEthereumDetailsOutput() EthereumDetailsOutput {
	return o
}

func (o EthereumDetailsOutput) ToEthereumDetailsOutputWithContext(ctx context.Context) EthereumDetailsOutput {
	return o
}

func (o EthereumDetailsOutput) ToEthereumDetailsPtrOutput() EthereumDetailsPtrOutput {
	return o.ToEthereumDetailsPtrOutputWithContext(context.Background())
}

func (o EthereumDetailsOutput) ToEthereumDetailsPtrOutputWithContext(ctx context.Context) EthereumDetailsPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v EthereumDetails) *EthereumDetails {
		return &v
	}).(EthereumDetailsPtrOutput)
}

// Immutable. Enables JSON-RPC access to functions in the `admin` namespace. Defaults to `false`.
func (o EthereumDetailsOutput) ApiEnableAdmin() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v EthereumDetails) *bool { return v.ApiEnableAdmin }).(pulumi.BoolPtrOutput)
}

// Immutable. Enables JSON-RPC access to functions in the `debug` namespace. Defaults to `false`.
func (o EthereumDetailsOutput) ApiEnableDebug() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v EthereumDetails) *bool { return v.ApiEnableDebug }).(pulumi.BoolPtrOutput)
}

// An Ethereum address which the beacon client will send fee rewards to if no recipient is configured in the validator client. See https://lighthouse-book.sigmaprime.io/suggested-fee-recipient.html or https://docs.prylabs.network/docs/execution-node/fee-recipient for examples of how this is used. Note that while this is often described as "suggested", as we run the execution node we can trust the execution node, and therefore this is considered enforced.
func (o EthereumDetailsOutput) BeaconFeeRecipient() pulumi.StringPtrOutput {
	return o.ApplyT(func(v EthereumDetails) *string { return v.BeaconFeeRecipient }).(pulumi.StringPtrOutput)
}

// Immutable. The consensus client.
func (o EthereumDetailsOutput) ConsensusClient() EthereumDetailsConsensusClientPtrOutput {
	return o.ApplyT(func(v EthereumDetails) *EthereumDetailsConsensusClient { return v.ConsensusClient }).(EthereumDetailsConsensusClientPtrOutput)
}

// Immutable. The execution client
func (o EthereumDetailsOutput) ExecutionClient() EthereumDetailsExecutionClientPtrOutput {
	return o.ApplyT(func(v EthereumDetails) *EthereumDetailsExecutionClient { return v.ExecutionClient }).(EthereumDetailsExecutionClientPtrOutput)
}

// Details for the Geth execution client.
func (o EthereumDetailsOutput) GethDetails() GethDetailsPtrOutput {
	return o.ApplyT(func(v EthereumDetails) *GethDetails { return v.GethDetails }).(GethDetailsPtrOutput)
}

// Immutable. The Ethereum environment being accessed.
func (o EthereumDetailsOutput) Network() EthereumDetailsNetworkPtrOutput {
	return o.ApplyT(func(v EthereumDetails) *EthereumDetailsNetwork { return v.Network }).(EthereumDetailsNetworkPtrOutput)
}

// Immutable. The type of Ethereum node.
func (o EthereumDetailsOutput) NodeType() EthereumDetailsNodeTypePtrOutput {
	return o.ApplyT(func(v EthereumDetails) *EthereumDetailsNodeType { return v.NodeType }).(EthereumDetailsNodeTypePtrOutput)
}

type EthereumDetailsPtrOutput struct{ *pulumi.OutputState }

func (EthereumDetailsPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EthereumDetails)(nil)).Elem()
}

func (o EthereumDetailsPtrOutput) ToEthereumDetailsPtrOutput() EthereumDetailsPtrOutput {
	return o
}

func (o EthereumDetailsPtrOutput) ToEthereumDetailsPtrOutputWithContext(ctx context.Context) EthereumDetailsPtrOutput {
	return o
}

func (o EthereumDetailsPtrOutput) Elem() EthereumDetailsOutput {
	return o.ApplyT(func(v *EthereumDetails) EthereumDetails {
		if v != nil {
			return *v
		}
		var ret EthereumDetails
		return ret
	}).(EthereumDetailsOutput)
}

// Immutable. Enables JSON-RPC access to functions in the `admin` namespace. Defaults to `false`.
func (o EthereumDetailsPtrOutput) ApiEnableAdmin() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *EthereumDetails) *bool {
		if v == nil {
			return nil
		}
		return v.ApiEnableAdmin
	}).(pulumi.BoolPtrOutput)
}

// Immutable. Enables JSON-RPC access to functions in the `debug` namespace. Defaults to `false`.
func (o EthereumDetailsPtrOutput) ApiEnableDebug() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *EthereumDetails) *bool {
		if v == nil {
			return nil
		}
		return v.ApiEnableDebug
	}).(pulumi.BoolPtrOutput)
}

// An Ethereum address which the beacon client will send fee rewards to if no recipient is configured in the validator client. See https://lighthouse-book.sigmaprime.io/suggested-fee-recipient.html or https://docs.prylabs.network/docs/execution-node/fee-recipient for examples of how this is used. Note that while this is often described as "suggested", as we run the execution node we can trust the execution node, and therefore this is considered enforced.
func (o EthereumDetailsPtrOutput) BeaconFeeRecipient() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EthereumDetails) *string {
		if v == nil {
			return nil
		}
		return v.BeaconFeeRecipient
	}).(pulumi.StringPtrOutput)
}

// Immutable. The consensus client.
func (o EthereumDetailsPtrOutput) ConsensusClient() EthereumDetailsConsensusClientPtrOutput {
	return o.ApplyT(func(v *EthereumDetails) *EthereumDetailsConsensusClient {
		if v == nil {
			return nil
		}
		return v.ConsensusClient
	}).(EthereumDetailsConsensusClientPtrOutput)
}

// Immutable. The execution client
func (o EthereumDetailsPtrOutput) ExecutionClient() EthereumDetailsExecutionClientPtrOutput {
	return o.ApplyT(func(v *EthereumDetails) *EthereumDetailsExecutionClient {
		if v == nil {
			return nil
		}
		return v.ExecutionClient
	}).(EthereumDetailsExecutionClientPtrOutput)
}

// Details for the Geth execution client.
func (o EthereumDetailsPtrOutput) GethDetails() GethDetailsPtrOutput {
	return o.ApplyT(func(v *EthereumDetails) *GethDetails {
		if v == nil {
			return nil
		}
		return v.GethDetails
	}).(GethDetailsPtrOutput)
}

// Immutable. The Ethereum environment being accessed.
func (o EthereumDetailsPtrOutput) Network() EthereumDetailsNetworkPtrOutput {
	return o.ApplyT(func(v *EthereumDetails) *EthereumDetailsNetwork {
		if v == nil {
			return nil
		}
		return v.Network
	}).(EthereumDetailsNetworkPtrOutput)
}

// Immutable. The type of Ethereum node.
func (o EthereumDetailsPtrOutput) NodeType() EthereumDetailsNodeTypePtrOutput {
	return o.ApplyT(func(v *EthereumDetails) *EthereumDetailsNodeType {
		if v == nil {
			return nil
		}
		return v.NodeType
	}).(EthereumDetailsNodeTypePtrOutput)
}

// Ethereum-specific blockchain node details.
type EthereumDetailsResponse struct {
	// Ethereum-specific endpoint information.
	AdditionalEndpoints EthereumEndpointsResponse `pulumi:"additionalEndpoints"`
	// Immutable. Enables JSON-RPC access to functions in the `admin` namespace. Defaults to `false`.
	ApiEnableAdmin bool `pulumi:"apiEnableAdmin"`
	// Immutable. Enables JSON-RPC access to functions in the `debug` namespace. Defaults to `false`.
	ApiEnableDebug bool `pulumi:"apiEnableDebug"`
	// An Ethereum address which the beacon client will send fee rewards to if no recipient is configured in the validator client. See https://lighthouse-book.sigmaprime.io/suggested-fee-recipient.html or https://docs.prylabs.network/docs/execution-node/fee-recipient for examples of how this is used. Note that while this is often described as "suggested", as we run the execution node we can trust the execution node, and therefore this is considered enforced.
	BeaconFeeRecipient string `pulumi:"beaconFeeRecipient"`
	// Immutable. The consensus client.
	ConsensusClient string `pulumi:"consensusClient"`
	// Immutable. The execution client
	ExecutionClient string `pulumi:"executionClient"`
	// Details for the Geth execution client.
	GethDetails GethDetailsResponse `pulumi:"gethDetails"`
	// Immutable. The Ethereum environment being accessed.
	Network string `pulumi:"network"`
	// Immutable. The type of Ethereum node.
	NodeType string `pulumi:"nodeType"`
}

// Ethereum-specific blockchain node details.
type EthereumDetailsResponseOutput struct{ *pulumi.OutputState }

func (EthereumDetailsResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EthereumDetailsResponse)(nil)).Elem()
}

func (o EthereumDetailsResponseOutput) ToEthereumDetailsResponseOutput() EthereumDetailsResponseOutput {
	return o
}

func (o EthereumDetailsResponseOutput) ToEthereumDetailsResponseOutputWithContext(ctx context.Context) EthereumDetailsResponseOutput {
	return o
}

// Ethereum-specific endpoint information.
func (o EthereumDetailsResponseOutput) AdditionalEndpoints() EthereumEndpointsResponseOutput {
	return o.ApplyT(func(v EthereumDetailsResponse) EthereumEndpointsResponse { return v.AdditionalEndpoints }).(EthereumEndpointsResponseOutput)
}

// Immutable. Enables JSON-RPC access to functions in the `admin` namespace. Defaults to `false`.
func (o EthereumDetailsResponseOutput) ApiEnableAdmin() pulumi.BoolOutput {
	return o.ApplyT(func(v EthereumDetailsResponse) bool { return v.ApiEnableAdmin }).(pulumi.BoolOutput)
}

// Immutable. Enables JSON-RPC access to functions in the `debug` namespace. Defaults to `false`.
func (o EthereumDetailsResponseOutput) ApiEnableDebug() pulumi.BoolOutput {
	return o.ApplyT(func(v EthereumDetailsResponse) bool { return v.ApiEnableDebug }).(pulumi.BoolOutput)
}

// An Ethereum address which the beacon client will send fee rewards to if no recipient is configured in the validator client. See https://lighthouse-book.sigmaprime.io/suggested-fee-recipient.html or https://docs.prylabs.network/docs/execution-node/fee-recipient for examples of how this is used. Note that while this is often described as "suggested", as we run the execution node we can trust the execution node, and therefore this is considered enforced.
func (o EthereumDetailsResponseOutput) BeaconFeeRecipient() pulumi.StringOutput {
	return o.ApplyT(func(v EthereumDetailsResponse) string { return v.BeaconFeeRecipient }).(pulumi.StringOutput)
}

// Immutable. The consensus client.
func (o EthereumDetailsResponseOutput) ConsensusClient() pulumi.StringOutput {
	return o.ApplyT(func(v EthereumDetailsResponse) string { return v.ConsensusClient }).(pulumi.StringOutput)
}

// Immutable. The execution client
func (o EthereumDetailsResponseOutput) ExecutionClient() pulumi.StringOutput {
	return o.ApplyT(func(v EthereumDetailsResponse) string { return v.ExecutionClient }).(pulumi.StringOutput)
}

// Details for the Geth execution client.
func (o EthereumDetailsResponseOutput) GethDetails() GethDetailsResponseOutput {
	return o.ApplyT(func(v EthereumDetailsResponse) GethDetailsResponse { return v.GethDetails }).(GethDetailsResponseOutput)
}

// Immutable. The Ethereum environment being accessed.
func (o EthereumDetailsResponseOutput) Network() pulumi.StringOutput {
	return o.ApplyT(func(v EthereumDetailsResponse) string { return v.Network }).(pulumi.StringOutput)
}

// Immutable. The type of Ethereum node.
func (o EthereumDetailsResponseOutput) NodeType() pulumi.StringOutput {
	return o.ApplyT(func(v EthereumDetailsResponse) string { return v.NodeType }).(pulumi.StringOutput)
}

// Contains endpoint information specific to Ethereum nodes.
type EthereumEndpointsResponse struct {
	// The assigned URL for the node's Beacon API endpoint.
	BeaconApiEndpoint string `pulumi:"beaconApiEndpoint"`
	// The assigned URL for the node's Beacon Prometheus metrics endpoint. See [Prometheus Metrics](https://lighthouse-book.sigmaprime.io/advanced_metrics.html) for more details.
	BeaconPrometheusMetricsApiEndpoint string `pulumi:"beaconPrometheusMetricsApiEndpoint"`
	// The assigned URL for the node's execution client's Prometheus metrics endpoint.
	ExecutionClientPrometheusMetricsApiEndpoint string `pulumi:"executionClientPrometheusMetricsApiEndpoint"`
}

// Contains endpoint information specific to Ethereum nodes.
type EthereumEndpointsResponseOutput struct{ *pulumi.OutputState }

func (EthereumEndpointsResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EthereumEndpointsResponse)(nil)).Elem()
}

func (o EthereumEndpointsResponseOutput) ToEthereumEndpointsResponseOutput() EthereumEndpointsResponseOutput {
	return o
}

func (o EthereumEndpointsResponseOutput) ToEthereumEndpointsResponseOutputWithContext(ctx context.Context) EthereumEndpointsResponseOutput {
	return o
}

// The assigned URL for the node's Beacon API endpoint.
func (o EthereumEndpointsResponseOutput) BeaconApiEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v EthereumEndpointsResponse) string { return v.BeaconApiEndpoint }).(pulumi.StringOutput)
}

// The assigned URL for the node's Beacon Prometheus metrics endpoint. See [Prometheus Metrics](https://lighthouse-book.sigmaprime.io/advanced_metrics.html) for more details.
func (o EthereumEndpointsResponseOutput) BeaconPrometheusMetricsApiEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v EthereumEndpointsResponse) string { return v.BeaconPrometheusMetricsApiEndpoint }).(pulumi.StringOutput)
}

// The assigned URL for the node's execution client's Prometheus metrics endpoint.
func (o EthereumEndpointsResponseOutput) ExecutionClientPrometheusMetricsApiEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v EthereumEndpointsResponse) string { return v.ExecutionClientPrometheusMetricsApiEndpoint }).(pulumi.StringOutput)
}

// Options for the Geth execution client. See [Command-line Options](https://geth.ethereum.org/docs/fundamentals/command-line-options) for more details.
type GethDetails struct {
	// Immutable. Blockchain garbage collection mode.
	GarbageCollectionMode *GethDetailsGarbageCollectionMode `pulumi:"garbageCollectionMode"`
}

// GethDetailsInput is an input type that accepts GethDetailsArgs and GethDetailsOutput values.
// You can construct a concrete instance of `GethDetailsInput` via:
//
//	GethDetailsArgs{...}
type GethDetailsInput interface {
	pulumi.Input

	ToGethDetailsOutput() GethDetailsOutput
	ToGethDetailsOutputWithContext(context.Context) GethDetailsOutput
}

// Options for the Geth execution client. See [Command-line Options](https://geth.ethereum.org/docs/fundamentals/command-line-options) for more details.
type GethDetailsArgs struct {
	// Immutable. Blockchain garbage collection mode.
	GarbageCollectionMode GethDetailsGarbageCollectionModePtrInput `pulumi:"garbageCollectionMode"`
}

func (GethDetailsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GethDetails)(nil)).Elem()
}

func (i GethDetailsArgs) ToGethDetailsOutput() GethDetailsOutput {
	return i.ToGethDetailsOutputWithContext(context.Background())
}

func (i GethDetailsArgs) ToGethDetailsOutputWithContext(ctx context.Context) GethDetailsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GethDetailsOutput)
}

func (i GethDetailsArgs) ToGethDetailsPtrOutput() GethDetailsPtrOutput {
	return i.ToGethDetailsPtrOutputWithContext(context.Background())
}

func (i GethDetailsArgs) ToGethDetailsPtrOutputWithContext(ctx context.Context) GethDetailsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GethDetailsOutput).ToGethDetailsPtrOutputWithContext(ctx)
}

// GethDetailsPtrInput is an input type that accepts GethDetailsArgs, GethDetailsPtr and GethDetailsPtrOutput values.
// You can construct a concrete instance of `GethDetailsPtrInput` via:
//
//	        GethDetailsArgs{...}
//
//	or:
//
//	        nil
type GethDetailsPtrInput interface {
	pulumi.Input

	ToGethDetailsPtrOutput() GethDetailsPtrOutput
	ToGethDetailsPtrOutputWithContext(context.Context) GethDetailsPtrOutput
}

type gethDetailsPtrType GethDetailsArgs

func GethDetailsPtr(v *GethDetailsArgs) GethDetailsPtrInput {
	return (*gethDetailsPtrType)(v)
}

func (*gethDetailsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**GethDetails)(nil)).Elem()
}

func (i *gethDetailsPtrType) ToGethDetailsPtrOutput() GethDetailsPtrOutput {
	return i.ToGethDetailsPtrOutputWithContext(context.Background())
}

func (i *gethDetailsPtrType) ToGethDetailsPtrOutputWithContext(ctx context.Context) GethDetailsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GethDetailsPtrOutput)
}

// Options for the Geth execution client. See [Command-line Options](https://geth.ethereum.org/docs/fundamentals/command-line-options) for more details.
type GethDetailsOutput struct{ *pulumi.OutputState }

func (GethDetailsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GethDetails)(nil)).Elem()
}

func (o GethDetailsOutput) ToGethDetailsOutput() GethDetailsOutput {
	return o
}

func (o GethDetailsOutput) ToGethDetailsOutputWithContext(ctx context.Context) GethDetailsOutput {
	return o
}

func (o GethDetailsOutput) ToGethDetailsPtrOutput() GethDetailsPtrOutput {
	return o.ToGethDetailsPtrOutputWithContext(context.Background())
}

func (o GethDetailsOutput) ToGethDetailsPtrOutputWithContext(ctx context.Context) GethDetailsPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v GethDetails) *GethDetails {
		return &v
	}).(GethDetailsPtrOutput)
}

// Immutable. Blockchain garbage collection mode.
func (o GethDetailsOutput) GarbageCollectionMode() GethDetailsGarbageCollectionModePtrOutput {
	return o.ApplyT(func(v GethDetails) *GethDetailsGarbageCollectionMode { return v.GarbageCollectionMode }).(GethDetailsGarbageCollectionModePtrOutput)
}

type GethDetailsPtrOutput struct{ *pulumi.OutputState }

func (GethDetailsPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GethDetails)(nil)).Elem()
}

func (o GethDetailsPtrOutput) ToGethDetailsPtrOutput() GethDetailsPtrOutput {
	return o
}

func (o GethDetailsPtrOutput) ToGethDetailsPtrOutputWithContext(ctx context.Context) GethDetailsPtrOutput {
	return o
}

func (o GethDetailsPtrOutput) Elem() GethDetailsOutput {
	return o.ApplyT(func(v *GethDetails) GethDetails {
		if v != nil {
			return *v
		}
		var ret GethDetails
		return ret
	}).(GethDetailsOutput)
}

// Immutable. Blockchain garbage collection mode.
func (o GethDetailsPtrOutput) GarbageCollectionMode() GethDetailsGarbageCollectionModePtrOutput {
	return o.ApplyT(func(v *GethDetails) *GethDetailsGarbageCollectionMode {
		if v == nil {
			return nil
		}
		return v.GarbageCollectionMode
	}).(GethDetailsGarbageCollectionModePtrOutput)
}

// Options for the Geth execution client. See [Command-line Options](https://geth.ethereum.org/docs/fundamentals/command-line-options) for more details.
type GethDetailsResponse struct {
	// Immutable. Blockchain garbage collection mode.
	GarbageCollectionMode string `pulumi:"garbageCollectionMode"`
}

// Options for the Geth execution client. See [Command-line Options](https://geth.ethereum.org/docs/fundamentals/command-line-options) for more details.
type GethDetailsResponseOutput struct{ *pulumi.OutputState }

func (GethDetailsResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GethDetailsResponse)(nil)).Elem()
}

func (o GethDetailsResponseOutput) ToGethDetailsResponseOutput() GethDetailsResponseOutput {
	return o
}

func (o GethDetailsResponseOutput) ToGethDetailsResponseOutputWithContext(ctx context.Context) GethDetailsResponseOutput {
	return o
}

// Immutable. Blockchain garbage collection mode.
func (o GethDetailsResponseOutput) GarbageCollectionMode() pulumi.StringOutput {
	return o.ApplyT(func(v GethDetailsResponse) string { return v.GarbageCollectionMode }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EthereumDetailsInput)(nil)).Elem(), EthereumDetailsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*EthereumDetailsPtrInput)(nil)).Elem(), EthereumDetailsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GethDetailsInput)(nil)).Elem(), GethDetailsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GethDetailsPtrInput)(nil)).Elem(), GethDetailsArgs{})
	pulumi.RegisterOutputType(ConnectionInfoResponseOutput{})
	pulumi.RegisterOutputType(EndpointInfoResponseOutput{})
	pulumi.RegisterOutputType(EthereumDetailsOutput{})
	pulumi.RegisterOutputType(EthereumDetailsPtrOutput{})
	pulumi.RegisterOutputType(EthereumDetailsResponseOutput{})
	pulumi.RegisterOutputType(EthereumEndpointsResponseOutput{})
	pulumi.RegisterOutputType(GethDetailsOutput{})
	pulumi.RegisterOutputType(GethDetailsPtrOutput{})
	pulumi.RegisterOutputType(GethDetailsResponseOutput{})
}
