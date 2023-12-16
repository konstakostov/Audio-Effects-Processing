class TopWindowEffectsParameters:
    used_effects = {
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

        'PitchShift': [
            ['Semitones', 0, 10],
        ]
    }
