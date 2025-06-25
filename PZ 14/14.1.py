"""
Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
«произведение»
"""

import re


surname = re.compile(r"\n\b[А-ЯЁ][а-яё]+-*[^е]*?\b")
file = open("write.app", "r", encoding="utf-8")
text = ''.join(file.readlines())
print("Кол-во фамилий", len(surname.findall(text)))
file.close()

new_file = open("new_text.txt", "w", encoding="utf-8")
new_text = re.sub("роман", "произведение", text)
print(new_text, file=new_file)
new_file.close()
