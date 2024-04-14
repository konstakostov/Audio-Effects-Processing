from Windows_Version.Effects.Effects_Data.audio_effects_groups_data import AudioEffectsGroupsData

"""
The 'MainWindowEffectsFrameInputData' class is used to hold the data for each of the frame. Each frame has the following
attributes: 'start_row', 'end_row', 'column', 'effects_group_name' and 'effects_in_group'.
"""


class MainWindowProcessingFrameInputData:
    effects_processing_input_data = [
        {
            "start_row": 1,
            "end_row": 5,
            "column": 0,
            "effects_group_name": list(AudioEffectsGroupsData.effects_by_groups.keys())[0],
            "effects_in_group": list(list(AudioEffectsGroupsData.effects_by_groups.values())[0].keys())
        },

        {
            "start_row": 6,
            "end_row": 9,
            "column": 0,
            "effects_group_name": list(AudioEffectsGroupsData.effects_by_groups.keys())[1],
            "effects_in_group": list(list(AudioEffectsGroupsData.effects_by_groups.values())[1].keys())
        },

        {
            "start_row": 1,
            "end_row": 4,
            "column": 2,
            "effects_group_name": list(AudioEffectsGroupsData.effects_by_groups.keys())[2],
            "effects_in_group": list(list(AudioEffectsGroupsData.effects_by_groups.values())[2].keys())
        },

        {
            "start_row": 5,
            "end_row": 7,
            "column": 2,
            "effects_group_name": list(AudioEffectsGroupsData.effects_by_groups.keys())[3],
            "effects_in_group": list(list(AudioEffectsGroupsData.effects_by_groups.values())[3].keys())
        },

        {
            "start_row": 8,
            "end_row": 9,
            "column": 2,
            "effects_group_name": list(AudioEffectsGroupsData.effects_by_groups.keys())[4],
            "effects_in_group": list(list(AudioEffectsGroupsData.effects_by_groups.values())[4].keys())
        },
    ]
