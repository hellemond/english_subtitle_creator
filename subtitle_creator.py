#this code will take a video file of any language, and add english subtitles to it

import assemblyai as aai
from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

aai.settings.api_key = "66f9661530504430a3379b59f7a5f969"
langs = langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
checking_language = True

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

if __name__ == '__main__':

    print("\nType 'languages' for a list of available languages\n")

    while checking_language == True:
        #checks if language is within dictionary
        source_lang = input("\nSource language of the video: ").lower()

        for i in langs:
            #checks through language dictionary to verify if input language is available to translate
            if source_lang == i:
                checking_language = False
                lang_code = langs[source_lang]
                print("\nLanguage available for translation.")
                print(lang_code)
                break
        
        if source_lang == 'languages':
            #print list of available languages
            for lang in langs:
                print(lang)
        else:
            #retry code
            if checking_language == False:
                break
            else:
                print("\nThat language is not available, please try again.")
    #manually input path to video needing subtitles
    video_file = input("\nFile path of video to translate: ")
    create_subtitles(video_file)