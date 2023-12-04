class Effects:
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
    }

