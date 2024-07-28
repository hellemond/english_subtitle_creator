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

langs = langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
source_file = 'subtitles.srt'
target_file = 'test_subtitles.srt'
x = 'zulu'
translated = GoogleTranslator(source='es', target='en').translate_file(source_file)

f = open(target_file, "w")
f.write(translated)
f.close