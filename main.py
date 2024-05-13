import os

# сортируем в папке файлы по количеству строк
dict_txt = {}
for file in os.listdir():
    if file.endswith('.txt'):
        with open(file, 'r', encoding='utf-8') as f:
            dict_txt[file] = f.readlines()
sorted_dict = sorted(dict_txt.items(), key=lambda x: len(x[1]))
# создаем новый файл
with open('sorted.txt', 'w', encoding='utf-8') as f:
    for file in sorted_dict:
        f.write(f"Название файла: {file[0]}   Количество строк: {len(file[1])}\n")
        f.write(''.join(file[1]))
        f.write('\n\n')

