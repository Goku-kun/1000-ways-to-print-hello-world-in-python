import translators as ts

text = "हैलो वर्ल्ड!"
translation = ts.translate_text(text, translator="google", from_language="hi", to_language="en")
print(translation)
