from Effects.Effects_Data.audio_effects_data import AudioEffectsData

"""
This class holds all the data related to the used audio effects.
The used effects are stored in a dictionary called 'effects_by_groups'.
Every item in the dictionary is a different audio effects group.
"""


class AudioEffectsGroupsData:
    effects_by_groups = {
        "Guitar-Style Effects": AudioEffectsData.guitar_style_effects,
        "Dynamic Range Effects": AudioEffectsData.dynamic_range_effects,
        "EQ Filter Effects": AudioEffectsData.eq_filter_effects,
        "Spatial Effects": AudioEffectsData.spatial_effects,
        "Pitch Effects": AudioEffectsData.pitch_effects,
    }
