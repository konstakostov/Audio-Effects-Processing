from pedalboard_native import (
    Chorus, Clipping, Distortion, Phaser,
    Compressor, Gain, Limiter,
    HighpassFilter, PeakFilter, LowpassFilter,
    Delay, Reverb,
    PitchShift,
)

"""
This functions is used to transform every effect and it's parameters as a Pedalboard object.
The 'result' variable is used to store all used Pedalboard objects.
We are iterating through every selected effects and their parameters.
If there is a match with the selected effect it is transformed as a Pedalboard object.
The transformed Pedalboard object is appended to the 'result' variable.
The 'result' variable is returned when the function is called.
"""


def convert_effect_parameters(parameters):
    result = []

    for name, parameter_values in parameters.items():
        if name == "Chorus":
            result.append(Chorus(
                rate_hz=parameter_values[0],
                depth=parameter_values[1],
                centre_delay_ms=parameter_values[2],
                feedback=parameter_values[3],
                mix=parameter_values[4],
            ))

        elif name == "Clipping":
            result.append(Clipping(
                threshold_db=parameter_values[0],
            ))

        elif name == "Distortion":
            result.append(Distortion(
                drive_db=parameter_values[0],
            ))

        elif name == "Phaser":
            result.append(Phaser(
                rate_hz=parameter_values[0],
                depth=parameter_values[1],
                centre_frequency_hz=parameter_values[2],
                feedback=parameter_values[3],
                mix=parameter_values[4],
                ))

        elif name == "Compressor":
            result.append(Compressor(
                threshold_db=parameter_values[0],
                ratio=parameter_values[1],
                attack_ms=parameter_values[2],
                release_ms=parameter_values[3],
            ))

        elif name == "Gain":
            result.append(Gain(
                gain_db=parameter_values[0],
            ))

        elif name == "Limiter":
            result.append(Limiter(
                threshold_db=parameter_values[0],
                release_ms=parameter_values[1]
            ))

        elif name == "Highpass Filter":
            result.append(HighpassFilter(
                cutoff_frequency_hz=parameter_values[0],
            ))

        elif name == "Peak Filter":
            result.append(PeakFilter(
                cutoff_frequency_hz=parameter_values[0],
                gain_db=parameter_values[1],
                q=parameter_values[2],
            ))

        elif name == "Lowpass Filter":
            result.append(LowpassFilter(
                cutoff_frequency_hz=parameter_values[0],
            ))

        elif name == "Delay":
            result.append(Delay(
                delay_seconds=parameter_values[0],
                feedback=parameter_values[1],
                mix=parameter_values[2],
            ))

        elif name == "Reverb":
            result.append(Reverb(
                room_size=parameter_values[0],
                damping=parameter_values[1],
                wet_level=parameter_values[2],
                dry_level=parameter_values[3],
                width=parameter_values[4],
                freeze_mode=parameter_values[5],
            ))

        elif name == "PitchShift":
            result.append(PitchShift(
                semitones=parameter_values[0]
            ))

    return result
