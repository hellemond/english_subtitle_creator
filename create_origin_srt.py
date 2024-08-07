
import whisper
from datetime import timedelta
from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip

langs = {
    "English": "en",
    "Albanian": "sq",
    "Arabic": "ar",
    "Azerbaijani": "az",
    "Bengali": "bn",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Chinese": "zh",
    "Chinese (traditional)": "zh-TW",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "Esperanto": "eo",
    "Estonian": "et",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Malay": "ms",
    "Norwegian": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Russian": "ru",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish": "es",
    "Swedish": "sv",
    "Tagalog": "tl",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur"
}
checking_source = True

def extract_audio(path):
    video = VideoFileClip(path)
    video.audio.write_audiofile("temp.mp3", codec="mp3")
    
    # else:
    #     print("video has no audio, quitting")

def create_subtitles():
    model = whisper.load_model("base")
    transcribe = model.transcribe(audio='temp.mp3', fp16=False)
    segments = transcribe["segments"]

    for seg in segments:
        start = str(0) + str(timedelta(seconds=int(seg["start"]))) + ",000"
        end = str(0) + str(timedelta(seconds=int(seg["end"]))) + ",000"
        text = seg["text"]
        segment_id = seg["id"] + 1
        segment = f"{segment_id}\n{start} --> {end}\n{text[1:] if text[0] == ' ' else text}\n\n"
        with open('origin_output.srt', "a", encoding="utf-8") as f:
            f.write(segment)

    print("subtitles generated")

def check_if_lang_is_valid(language):
    for i in langs:
    # checks through language dictionary to verify if source language is available
        if language == i:
            lang_code = langs[language]
            return lang_code
    print("\nLanguage not available\n")

if __name__ == '__main__':

    # print("\nType 'languages' for a list of available languages\n")

    # while checking_source == True:
    #     # asks for user input of source and target language

    #     source_lang = input("\nSource language of the video: ").capitalize()

    #     if source_lang == 'Languages':
    #         for i in langs:
    #             print(i)
    #     else:
    #         source_lang_code = check_if_lang_is_valid(source_lang)
    #         if source_lang_code:
    #             checking_source = False

    # video_file = input("\nFile path of video to translate: ")
    video_file_path = './input_video/korean.mp4'
    # + video_file

    # create srt file of source language
    extract_audio(video_file_path)
    create_subtitles()
    