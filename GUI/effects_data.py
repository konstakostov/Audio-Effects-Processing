# Class that holds each effect group's effects
class EffectGroups:
    # Creates a list, containing effects name labels for 'Guitar Effects'
    guitar_effects = ['Chorus', 'Clipping', 'Distortion', 'Phaser']

    # Creates a list, containing effects name labels for 'Dynamic Range Effects'
    dynamic_range_effects = ['Compressor', 'Gain', 'Limiter']

    # Creates a list, containing effects name labels for 'Equalizers and Filters'
    eq_filter_effects = ['Highpass Filter', 'Ladder Filter', 'Lowpass Filter']

    # Creates a list, containing effects name labels for 'Spatial Effects'
    spatial_effects = ['Delay', 'Reverb']

    # Creates a list, containing effects name labels for 'Pitch Effects'
    pitch_effects = ['PitchShift']


# Class that holds each effects parameters (name, bottom_value, top_value)
class TopWindowEffectsParameters:
    # Used effects dictionary that holds all effects
    used_effects = {
        # First Frame 'Guitar Effects'
        'Chorus': [
            ['Rate [Hz]', 0, 1000],
            ['Depth', 0, 1],
            ['Centre Delay [ms]', 0, 1000],
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
            ['Rate [Hz]', 0, 100],
            ['Depth', 0, 1],
            ['Center Frequency', 0, 1000],
            ['Feedback', 0, 1],
            ['Mix', 0, 1],
        ],

        # Second Frame Dynamic Range Effects'
        'Compressor': [
            ['Rate [Hz]', 0, 100],
            ['Threshold [dB]', -100, 100],
            ['Ratio', 0, 1],
            ['Attack [ms]', 0, 10000],
            ['Release [ms]', 0, 10000],
        ],

        'Gain': [
            ['Gain [dB]', 0, 100],
        ],

        'Limiter': [
            ['Threshold [dB]', -100, 100],
            ['Release [ms]', 0, 10000],
        ],

        # Third Frame 'Equalizers and Filters'
        'Highpass Filter': [
            ['Cutoff Frequency [Hz]', 0, 1000]
        ],

        'Ladder Filter': [
            ['Mode', 0, 5],
            ['Cutoff [Hz]', 0, 1000],
            ['Resonance', 0, 1],
            ['Drive', 1, 100],
        ],

        'Lowpass Filter': [
            ['Cutoff Frequency [Hz]', 0, 1000]
        ],

        # Fourth Frame 'Spatial Effects'
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

        # Fifth Frame 'Pitch Effects'
        'PitchShift': [
            ['Semitones', 0, 10],
        ]
    }
