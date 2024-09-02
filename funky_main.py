from tkinter import *
import customtkinter as ctk
from customtkinter import filedialog
import whisper
import ffmpeg
from datetime import timedelta
from moviepy.editor import VideoFileClip
import os

output_audio = './outputs/video_audio.mp3'
output_srt = './outputs/video_subtitles.srt'
output_video = './outputs/output_video.mp4'


ctk.set_appearance_mode("dark")
app = ctk.CTk()

# window size
app.geometry('500x300')


def extract_audio(path):
    # extracts audio from video to audio.mp3
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
    ffmpeg.concat(video.filter("subtitles", output_srt), audio, v=1, a=1).output(output_video).run()


# title of window
title = ctk.CTkLabel(app, text="SUBTITLE GENERATOR", fg_color="transparent", font =('Arial', 20))
title.pack(padx = 35, pady = 25)
title.anchor("center")

# select input file button
def selectfile():
    filename = filedialog.askopenfilename()
    print(filename)

    global input_path
    input_path = filename

    file_path_label.configure(text=input_path)

input_video_button = ctk.CTkButton(app, text = "Select Input Video", command = selectfile)
input_video_button.pack(padx = 25)
input_video_button.anchor("center")


file_path_label = ctk.CTkLabel(app, text='', fg_color="transparent", )
file_path_label.pack(padx = 25)
file_path_label.anchor("center")


# select model size button
def combobox_callback(choice):
    print("model size chosen:", choice)
    global model_size
    model_size = choice

model_dropdown = ctk.CTkComboBox(app, values=["tiny", "base", "small", "medium", "large"],
                                     command=combobox_callback)
model_dropdown.pack(padx=20, pady=10)
model_dropdown.set("Select Model")

# run program button
def button_event():

    extract_audio(input_path)
    create_subtitles(model_size)
    combine_srt_with_video(input_path)
    os.remove(output_audio)
    os.remove(output_srt)


run_app_button = ctk.CTkButton(app, text="Create Subtitled Video", command=(button_event))
run_app_button.pack(padx=20, pady=25)
run_app_button.anchor("s")


# progress bar
# progressbar = ctk.CTkProgressBar(app, progress_color='cyan', mode='indeterminate')
# progressbar.pack(padx = 1, pady = 10)

# run the app
app.mainloop()

