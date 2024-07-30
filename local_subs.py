#this code will take a video file of any language, and add english subtitles to it

import assemblyai as aai
import argostranslate.package
import argostranslate.translate
                             
aai.settings.api_key = "66f9661530504430a3379b59f7a5f969"
checking_source = True
checking_target = True
# targed_lang = 'en'
source_srt = 'source.srt'
output_file = 'target.srt'
h = 0

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

def create_subtitles(path, source_code):

    # subtitle generator config
    config = aai.TranscriptionConfig(
                                    speech_model=aai.SpeechModel.nano,
                                    language_detection = True
                                    # language_code = source_code
                                    )

    # path to file to create transcript of
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(path)

    # export srt file of transcript
    subtitles = transcript.export_subtitles_srt()

    f = open(source_srt, "w", encoding='UTF-16')
    f.write(subtitles)
    f.close()


def translate_line(line_to_translate, source_code, target_code):
    #   function to translate a line sent to this
    # returns line translated to english
    
    translated = argostranslate.translate.translate(line_to_translate, source_code, target_code)
    return translated

def make_subs_english(source_code, target_code):
    # installs language pack if not already installed
    # try:
    #     argostranslate.package.update_package_index()
    #     available_packages = argostranslate.package.get_available_packages()
    #     package_to_install = next(
    #         filter(
    #             lambda x: x.code == source_code and x.to_code == target_code, available_packages
    #         )
    #     )
    #     argostranslate.package.install_from_path(package_to_install.download())

    # except:
    #     pass


    # opens srt of source language
    file1=open(source_srt,"r")
    # opens file of srt to be written in english
    file2=open(output_file,"w", encoding='UTF-16')
    i = 0

    for line in file1.readlines():
        # read each line of source srt and writes them to output.srt in english
        if i < 2:
            file2.write(line)

        elif i == 2:
            translated_line = translate_line(line, source_code, target_code)
            file2.write(translated_line + '\n')

        elif i > 2: 
            if (i-2) % 4 == 0:
                translated_line = translate_line(line, source_code, target_code)
                file2.write(translated_line + '\n')
            else:
                file2.write(line)
        else:
            print("smth happened")
            print(i)
            

        i += 1

    file1.close()
    file2.close()

def check_if_lang_is_valid(language):
    for i in langs:
    # checks through language dictionary to verify if source language is available
        if language == i:
            lang_code = langs[language]
            return lang_code
    print("\nLanguage not available\n")
            

if __name__ == '__main__':

    print("\nType 'languages' for a list of available languages\n")

    while checking_source == True:
        # asks for user input of source and target language

        source_lang = input("\nSource language of the video: ").capitalize()

        if source_lang == 'Languages':
            for i in langs:
                print(i)
        else:
            source_lang_code = check_if_lang_is_valid(source_lang)
            if source_lang_code:
                checking_source = False


    while checking_target == True:

        target_lang = input("\nTarget language of the video: ").capitalize()

        if target_lang == 'Languages':
            for i in langs:
                print(i)
        else:
            target_lang_code = check_if_lang_is_valid(target_lang)
            if target_lang_code:
                checking_target = False


    # manually input path to video needing subtitles
    video_file = input("\nFile path of video to translate: ")

    # create srt file of source language
    create_subtitles(video_file, source_lang_code)
    # download language pack
    # translate former srt file into new english srt file
    make_subs_english(source_lang_code, target_lang_code)