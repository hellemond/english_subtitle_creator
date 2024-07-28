#this code will take a video file of any language, and add english subtitles to it

import assemblyai as aai


aai.settings.api_key = "66f9661530504430a3379b59f7a5f969"


def create_subtitles(path):
    
    # subtitle generator config
    config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best,
                                     language_detection=True,
                                     )

    # path to file to create transcript of
    transcript = aai.Transcriber(config=config).transcribe(path)

    # export srt file of transcript
    subtitles = transcript.export_subtitles_srt()

    f = open('subtitles', "w")
    f.write(subtitles)
    f.close


create_subtitles('input.mp4')