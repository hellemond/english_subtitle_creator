import argostranslate.argospm
import argostranslate.translate



# This may take a while
# This will install all the language packages for argostranslate

argostranslate.argospm.install_all_packages()



# run code below to view installed packages

# x = argostranslate.translate.get_installed_languages()
# for i in x:
#     print(i)