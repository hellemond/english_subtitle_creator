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


3. download required model files for whisperai
    follow step 3 @ this site: https://github.com/openai/whisper/discussions/1463

4. edit 'openai_public.py' file located at .\venv\Lib\site-packages\tiktoken_ext\openai_public.py
    - This step is also mentioned in step 3 on the linked webpage

5. add missing dependency (libomp140.x86_64.dll) to .\venv\Lib\site-packages\torch\lib
    - the file is located in 'step_5_torch_file' directory

6. Add input.mp4 file to 'inputs' directory

7. run code
