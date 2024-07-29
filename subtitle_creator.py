#this code will take a video file of any language, and add english subtitles to it

import assemblyai as aai
from deep_translator import GoogleTranslator
                             
aai.settings.api_key = "66f9661530504430a3379b59f7a5f969"
langs = langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
checking_language = True
targed_lang = 'en'
output_file = 'target.srt'
source_srt = 'source.srt'



def create_subtitles(path, code):

    # subtitle generator config
    config = aai.TranscriptionConfig(
                                    speech_model=aai.SpeechModel.nano,
                                    # language_detection = True
                                    language_code= code
                                    )

    # path to file to create transcript of
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(path)

    # export srt file of transcript
    subtitles = transcript.export_subtitles_srt()

    f = open(source_srt, "w", encoding='utf-8')
    f.write(subtitles)
    f.close()

def translate_line(line_to_translate, code):
    #   function to translate a line sent to this
    # returns line translated to english
    translated = GoogleTranslator(source=code, target='en').translate(text=line_to_translate)
    return translated

def make_subs_english(code):
    # opens srt of source language
    file1=open(source_srt,"r")
    # opens file of srt to be written in english
    file2=open(output_file,"w", encoding='utf-8')
    i = 0

    for line in file1.readlines():
        # read each line of source srt and writes them to output.srt in english
        if i < 2:
            file2.write(line)

        elif i == 2:
            translated_line = translate_line(line, code)
            file2.write(translated_line + '\n')

        elif i > 2: 
            if (i-2) % 4 == 0:
                translated_line = translate_line(line, code)
                file2.write(translated_line + '\n')
            else:
                file2.write(line)
            

        i += 1

    file1.close()
    file2.close()

if __name__ == '__main__':

    print("\nType 'languages' for a list of available languages\n")

    while checking_language == True:
        # checks if language is within dictionary
        source_lang = input("\nSource language of the video: ").lower()

        for i in langs:
            # checks through language dictionary to verify if input language is available to translate
            if source_lang == i:
                checking_language = False
                lang_code = langs[source_lang]
                print("\nLanguage available for translation.")
                print(lang_code)
                break
        
        if source_lang == 'languages':
            # print list of available languages
            for lang in langs:
                print(lang)
        else:
            #retry code
            if checking_language == False:
                break
            else:
                print("\nThat language is not available, please try again.")

    # manually input path to video needing subtitles
    video_file = input("\nFile path of video to translate: ")

    # create srt file of source language
    create_subtitles(video_file, lang_code)
    # translate former srt file into new english srt file
    make_subs_english(lang_code)