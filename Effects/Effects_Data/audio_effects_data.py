"""
This class holds all the data related to the used audio effects groups.
Each group consist of one or more audio effect.
Each effect has its own parameter(s) and their min and max allowed values.
"""


class AudioEffectsData:
    guitar_style_effects = {
        'Chorus': [
            ['Rate [Hz]', 0, 100],
            ['Depth', 0, 1],
            ['Centre Delay [ms]', 0, 10000],
            ['Feedback', 0, 1],
            ['Mix', 0, 1],
        ],

        'Clipping': [
            ['Threshold [dB]', -100, 100],
        ],

        'Distortion': [
            ['Drive [dB]', 0, 100],
        ],

        'Phaser': [
            ['Rate [Hz]', 0, 1000],
            ['Depth', 0, 1],
            ['Center Frequency', 0, 1000],
            ['Feedback', 0, 1],
            ['Mix', 0, 1],
        ]
    }

    dynamic_range_effects = {
        'Compressor': [
            ['Threshold [dB]', -100, 100],
            ['Ratio', 0.1, 1],
            ['Attack [ms]', 0, 10000],
            ['Release [ms]', 0, 10000],
        ],

        'Gain': [
            ['Gain [dB]', -100, 100],
        ],

        'Limiter': [
            ['Threshold [dB]', -100, 100],
            ['Release [ms]', 0, 10000],
        ],
    }

    eq_filter_effects = {
        'Highpass Filter': [
            ['Cutoff Frequency [Hz]', 0, 1000]
        ],

        'Peak Filter': [
            ['Cutoff Frequency [Hz]', 0, 1000],
            ['Gain [db]', 0, 100],
            ['q', 0.1, 1],
        ],

        'Lowpass Filter': [
            ['Cutoff Frequency [Hz]', 0, 1000]
        ],
    }

    spatial_effects = {
        'Delay': [
            ['Delay [s]', 0, 30],
            ['Feedback', 0, 1],
            ['Mix', 0, 1],
        ],

        'Reverb': [
            ['Room Size', 0, 1],
            ['Damping', 0, 1],
            ['Wet Level', 0, 1],
            ['Dry Level', 0, 1],
            ['Width', 0, 1],
            ['Freeze Mode', 0, 1],
        ],
    }

    pitch_effects = {
        'PitchShift': [
            ['Semitones', -72, 72],
        ],
    }
