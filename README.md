# Audio Effects Processing version 1.0

## Description

The **Audio Effects Processing** tool is a graphical user interface (GUI) developed using Tkinter, a Python library for creating user interfaces. It allows users to apply various audio effects to `.wav` files in a user-friendly way. These audio effects are implemented using Pedalboard, a Python library for applying effects to audio files.

## How to Use

To use the tool, ensure you have Python 3 installed.

1. Run the following command to install the required libraries:
    ```
    py -m pip install -r requirements.txt
    ```

2. Navigate to the **Run** folder and run **`run_gui.py`** to launch the tool.

![Main Window of the GUI](https://github.com/konstakostov/Audio-Effects-Processing/assets/122868401/64473e6f-e382-4320-960c-7d0bb5011924)

3. To select a `.wav` file for processing, click the **"Select .wav File"** button and choose the desired file.
    - The `.wav` file must be placed in the **Processing** folder.

4. Choose the effect(s) to process the audio file by ticking the checkbox next to the desired effect(s) to unlock the **"Set Parameters"** button.
    - After unlocking the button and clicking it, a top window will appear displaying all the selected effects' parameters.
    - Adjust the values of each parameter using the provided spinboxes or by directly editing the field within the allowed range.

![Chorus Effects Parameters Top Window](https://github.com/konstakostov/Audio-Effects-Processing/assets/122868401/2f778f33-0240-448d-aded-5ae03f9784da)


5. Once you've selected all the effects and the input file, click the **"Set Parameters"** button to process the selected items. The output file will be generated in the same directory as the input file.

## Future Improvements
- [x] Allow users to open _.wav_ file from any directory.
- [x] Add graphical representation of the input and output files in the Main Window.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](https://github.com/konstakostov/Audio-Effects-Processing/blob/main/LICENSE) file for details.

## Credits
**Social Media Preview Photo** by <a href="https://unsplash.com/@benoit_adam?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Benoit Adam</a> on <a href="https://unsplash.com/photos/a-bunch-of-electronic-equipment-sitting-on-top-of-a-wooden-floor-cOT3PJee02w?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

**Pedalboard Library** by [Spotify Pedalboard](https://github.com/spotify/pedalboard?tab=readme-ov-file)

