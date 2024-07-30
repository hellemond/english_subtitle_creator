#this code will take a video file of any language, and add english subtitles to it

import assemblyai as aai
import argostranslate.package
import argostranslate.translate
                             
aai.settings.api_key = "66f9661530504430a3379b59f7a5f969"
checking_language = True
# targed_lang = 'en'
output_file = 'target.srt'
source_srt = 'source.srt'

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
    
    translated = argostranslate.translate.translate(line_to_translate, code, 'en')
    return translated

def make_subs_english(code):
    # installs language pack if not already installed
    try:
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next(
            filter(
                lambda x: x.code == code and x.to_code == 'en', available_packages
            )
        )
        argostranslate.package.install_from_path(package_to_install.download())

    except:
        pass


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
        # asks for user input of source and target language

        source_lang = input("\nSource language of the video: ").lower()
        targed_lang = input("Target language of the video: ").lower()

    


    # manually input path to video needing subtitles
    video_file = input("\nFile path of video to translate: ")

    # create srt file of source language
    create_subtitles(video_file, lang_code)
    # download language pack
    download_language()
    # translate former srt file into new english srt file
    make_subs_english(lang_code)