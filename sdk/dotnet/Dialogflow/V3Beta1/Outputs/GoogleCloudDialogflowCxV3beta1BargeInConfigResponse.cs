// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.GoogleNative.Dialogflow.V3Beta1.Outputs
{

    /// <summary>
    /// Configuration of the barge-in behavior. Barge-in instructs the API to return a detected utterance at a proper time while the client is playing back the response audio from a previous request. When the client sees the utterance, it should stop the playback and immediately get ready for receiving the responses for the current request. The barge-in handling requires the client to start streaming audio input as soon as it starts playing back the audio from the previous response. The playback is modeled into two phases: * No barge-in phase: which goes first and during which speech detection should not be carried out. * Barge-in phase: which follows the no barge-in phase and during which the API starts speech detection and may inform the client that an utterance has been detected. Note that no-speech event is not expected in this phase. The client provides this configuration in terms of the durations of those two phases. The durations are measured in terms of the audio length fromt the the start of the input audio. The flow goes like below: --&gt; Time without speech detection | utterance only | utterance or no-speech event | | +-------------+ | +------------+ | +---------------+ ----------+ no barge-in +-|-+ barge-in +-|-+ normal period +----------- +-------------+ | +------------+ | +---------------+ No-speech event is a response with END_OF_UTTERANCE without any transcript following up.
    /// </summary>
    [OutputType]
    public sealed class GoogleCloudDialogflowCxV3beta1BargeInConfigResponse
    {
        /// <summary>
        /// Duration that is not eligible for barge-in at the beginning of the input audio.
        /// </summary>
        public readonly string NoBargeInDuration;
        /// <summary>
        /// Total duration for the playback at the beginning of the input audio.
        /// </summary>
        public readonly string TotalDuration;

        [OutputConstructor]
        private GoogleCloudDialogflowCxV3beta1BargeInConfigResponse(
            string noBargeInDuration,

            string totalDuration)
        {
            NoBargeInDuration = noBargeInDuration;
            TotalDuration = totalDuration;
        }
    }
}
