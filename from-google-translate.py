from googletrans import Translator
text = 'Hola Mundo!'
translator = Translator()
print(translator.translate(text).text)