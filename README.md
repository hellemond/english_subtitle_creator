### english_subtitle_creator
### tool designed to create english subtitles on 'any' language video



1. Create virtual environment and activate it

    python -m venv venv
    .\venv\Scripts\Activate.ps1


2. install the pips
    - you can copy paste the code below into your terminal

    pip install git+https://github.com/openai/whisper.git
    pip install blobfile
    pip install moviepy
    pip install ffmpeg-python
    pip install --force-reinstall numpy==1.26.4


3. install ffmpeg
 - easy to follow guide on how to do that:
    - https://phoenixnap.com/kb/ffmpeg-windows
    - **Restart terminal after ffmpeg installation**


4. download required model files for whisperai
    follow step 3 @ this site: https://github.com/openai/whisper/discussions/1463


5. edit 'openai_public.py' file located at .\venv\Lib\site-packages\tiktoken_ext\openai_public.py
    - **step 3 from the linked webpage for instructions on what to edit**


6. add missing dependency (libomp140.x86_64.dll) to .\venv\Lib\site-packages\torch\lib
    - the file is located in 'step_5_torch_file' directory


7. Add input.mp4 file to 'inputs' directory


8. run code
