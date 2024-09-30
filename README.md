# Audio Effects Processing version 1.1

## Description

The **Audio Effects Processing** tool is a graphical user interface (GUI) developed using Tkinter, a Python library for creating user interfaces. It allows users to apply various audio effects to `.wav` files in a user-friendly way. These audio effects are implemented using Pedalboard, a Python library that applies effects to audio files.

## How to Use

To use the tool, please make sure you have Python 3 installed. 

<ol>
    <li>
        <p>
            Run the following command to install the required libraries:
            <pre><code>py -m pip install -r requirements.txt</code></pre>
        </p>   
    </li>
    <li>
        <p>Navigate to the <b>Run</b> folder and run <b><i>run_gui.py</i></b> to launch the tool.</p>
        <p>
            <img src="https://github.com/user-attachments/assets/1a1e0dc3-c508-4f01-a1d3-3e1b91131d0a" alt="Main Window of the GUI">
        </p>
    </li>
    <li>
        <p>
            There are 3 main sections to the GUI.
        </p>
        <ul>
            <li>
                <p>
                    The first section (Labeled <b>'1'</b> on the above image) is the Audio Processing part.
                </p>
                <ul>
                    <li>
                        <p>
                            It allows the user to process an audio file, in .wav format.
                        </p>
                    </li>
                    <li>
                        <p>
                            The user should first select the .wav file it wants to process via the "Select .wav File" button.
                        </p>
                    </li>
                    <li>
                        <p>
                            The user can choose the effect(s) it wants to apply to it by selecting the checkbox next to each effect, and after that setting the effect parameters by clicking the "Set Parameters" button.
                        </p>
                    </li>
                    <li>
                        <p>
                            After a .wav file and the desired effects have been chosen, the user should press the "Process Audio File" button. By pressing the button, the audio file is processed with the selected effects and saved in the directory of the initial .wav file.
                        </p>
                    </li>
                </ul>
            </li>
            <li>
                <p>
                    The second section (Labeled <b>'2'</b> on the above image) allows the user to open the last saved directory in the audio processing part.
                </p>
                <ul>
                    <li>
                        <p>
                            It allows the user to quickly open the directory and find the last processed .wav file
                        </p>
                    </li>
                </ul>
            </li>
            <li>
                <p>
                    The third section (Labeled <b>'3'</b> on the above image) is the Audio Visualization part.
                </p>
                <ul>
                    <li>
                        <p>
                            It allows the user to visualize an audio signal, in .wav format.
                        </p>
                    </li>
                    <li>
                        <p>
                            The user should first select the .wav file it wants to process via the "Select .wav File" button.
                        </p>
                    </li>
                    <li>
                        <p>
                            After an audio file has been selected, the user can choose the type of visualization to be plotted.
                        </p>
                    </li>
                    <li>
                        <p>
                            The available visualizations are:
                        </p>
                        <ul>
                            <li>
                                <p>
                                    Amplitude-Time Graph: 
                                </p>
                            </li>
                            <li>
                                <p>
                                    Spectrogram: 
                                </p>
                            </li>
                            <li>
                                <p>
                                    Magnitude [dB] Spectrum Graph: 
                                </p>
                            </li>
                            <li>
                                <p>
                                    Magnitude [Energy] Spectrum Graph: 
                                </p>
                            </li>
                            <li>
                                <p>
                                    Angle Spectrum Graph:
                                </p>
                            </li>
                            <li>
                                <p>
                                    Phase Spectrum Graph:
                                </p>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        <p>Choose the effect(s) to process the audio file by ticking the checkbox next to the desired effect(s) to unlock the <b>"Set Parameters"</b> button.</p>
        <ul>
            <li>
                <p>
                    After unlocking the button and clicking it, a top window will appear displaying all the selected effects' parameters.
                </p>
            </li>
            <li>
                <p>
                    Adjust the values of each parameter using the provided spinboxes or by directly editing the field within the allowed range.
                </p>
            </li>
        </ul>
        <p>
            <img src="https://github.com/konstakostov/Audio-Effects-Processing/assets/122868401/2f778f33-0240-448d-aded-5ae03f9784da" alt="Top Window of the GUI">
        </p>
    </li>
    <li>
        <p>
            Once you've selected all the effects and the input file, click the <b>"Set Parameters"</b> button to process the selected items. The output file will be generated in the same directory as the input file.
        </p>
    </li>
</ol>


## Future Improvements
- [x] Allow users to open _.wav_ file from any directory.
- [x] Add a graphical representation of the input and output files in the Main Window.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](https://github.com/konstakostov/Audio-Effects-Processing/blob/main/LICENSE) file for details.

## Credits
**Social Media Preview Photo** by <a href="https://unsplash.com/@benoit_adam?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Benoit Adam</a> on <a href="https://unsplash.com/photos/a-bunch-of-electronic-equipment-sitting-on-top-of-a-wooden-floor-cOT3PJee02w?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

**Pedalboard Library** by [Spotify Pedalboard](https://github.com/spotify/pedalboard?tab=readme-ov-file)

