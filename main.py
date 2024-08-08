import whisper
import ffmpeg
from datetime import timedelta
from moviepy.editor import VideoFileClip
from pathlib import Path
import os

# list of available languages
whisper_supported_languages = [
    "English",
    "Spanish",
    "French",
    "German",
    "Italian",
    "Portuguese",
    "Dutch",
    "Russian",
    "Chinese (Mandarin)",
    "Japanese",
    "Korean",
    "Arabic",
    "Turkish",
    "Hindi",
    "Bengali",
    "Urdu",
    "Vietnamese",
    "Polish",
    "Ukrainian",
    "Thai",
    "Czech",
    "Romanian",
    "Hungarian",
    "Greek",
    "Bulgarian",
    "Hebrew",
    "Danish",
    "Swedish",
    "Norwegian",
    "Finnish",
    "Lithuanian",
    "Latvian",
    "Estonian",
    "Slovak",
    "Slovenian",
    "Croatian",
    "Serbian",
    "Bosnian",
    "Montenegrin",
    "Macedonian",
    "Albanian",
    "Georgian",
    "Armenian",
    "Kazakh",
    "Uzbek",
    "Turkmen",
    "Azerbaijani",
    "Pashto",
    "Persian",
    "Swahili",
    "Malay",
    "Indonesian",
    "Filipino",
    "Mongolian",
    "Nepali",
    "Sinhala",
    "Burmese",
    "Khmer",
    "Lao",
    "Maltese"
]

# list of model types available
whisper_model_sizes = [
    "tiny",    # smallest model, fast but less accurate
    "base",    # small model, balanced between speed and accuracy
    "small",   # medium model, better accuracy but slower
    "medium",  # large model, more accurate but slower
    "large"    # largest model, highest accuracy but slowest
]

output_audio = './outputs/temp.mp3'
output_srt = './outputs/temp.srt'

def extract_audio(path):
    # extracts audio from video to temp.mp3
    video = VideoFileClip(path)
    video.audio.write_audiofile(output_audio, codec="mp3")
    
    # else:
    #     print("video has no audio, quitting")

def create_subtitles(model_type):
    # generates subtitles file from audio
    model = whisper.load_model(model_type)
    audio_file_path = output_audio
    audio = whisper.load_audio(audio_file_path)
    audio = whisper.pad_or_trim(audio)
    transcribe = model.transcribe(audio=audio_file_path, language='en', task='translate', condition_on_previous_text=False, fp16=False)
    segments = transcribe["segments"]

    for seg in segments:
        start = str(0) + str(timedelta(seconds=int(seg["start"]))) + ",000"
        end = str(0) + str(timedelta(seconds=int(seg["end"]))) + ",000"
        text = seg["text"]
        segment_id = seg["id"] + 1
        segment = f"{segment_id}\n{start} --> {end}\n{text[1:] if text[0] == ' ' else text}\n\n"
        with open(output_srt, "a", encoding="utf-8") as f:
            f.write(segment)

def combine_srt_with_video(input_video_path):
    # outputs new video of combined srt and input video
    video = ffmpeg.input(input_video_path)
    audio = video.audio
    ffmpeg.concat(video.filter("subtitles", output_srt), audio, v=1, a=1).output('./outputs/subbed_up.mp4').run()


if __name__ == '__main__':

    # first segment
    # user input of mp4 file name in inputs folder
    # checks if file exists to proceed
    print("Type 'L' for a list of available languages")
    checking = True
    while checking == True:

        video_file = input("\n\nEnter file name of video: ")

        current_directory = os.getcwd()
        tmp_file_path = 'inputs\\' + video_file
        relative_path = os.path.join(current_directory, tmp_file_path)
        
        if video_file.upper() == "L":
            for i in whisper_supported_languages:
                print (i)

        elif os.path.exists(relative_path) == True:
            video_file_path = './inputs/' + video_file
            checking = False

        else: 
            print("\n*** File Does Not Exist ***")

    # second segment
    # user input of whisper ai size/type
    # checks if valid type to proceed
    checking = True
    print("\n\nType 'M' for a list of model types")
    while checking == True:

        model_size = input("\nEnter Model type: ")

        if model_size.upper() == "M":
            print('\nModel Types:')
            for i in whisper_model_sizes:
                print (i)
        elif model_size in whisper_model_sizes:
            checking = False
        else:
            print('\n*** Invalid Model Size ***')

    extract_audio(video_file_path)
    create_subtitles(model_size)
    combine_srt_with_video(video_file_path)
    