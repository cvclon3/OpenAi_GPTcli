#pip install googletrans==4.0.0-rc1

from googletrans import Translator


def translate(answer, to_lang="ru"):
    translator = Translator()
    result = translator.translate(answer, dest=to_lang)
    return result
