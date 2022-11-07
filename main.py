import os


# Функция принимает как заранее известный список
# так и читает в корневой папке все .txt файлы
def main():
    # files = ['1.txt', '2.txt', '3.txt']
    # files_info = lenght_file(files)
    files_info = lenght_file()

    create_file_sorted_by_lenght(files_info)


# вызов функции может осуществляться как с известным списком файлов так и без него
def lenght_file(files=None):

    # вынес в функцию повторябщийся код
    def read_infofile_in_dict(file_name):
        with open(file_name, 'rt') as f:
            file_info[file.replace('.txt', '')] = len(list(f))

    file_info = {}
    if files is None:
        for _x, _y, files_names in os.walk('.'):
            for file in files_names:
                if '.txt' in file and file != 'result.txt':
                    read_infofile_in_dict(file)
    else:
        for file in files:
            read_infofile_in_dict(file)

    return file_info


# создание файла и заполнение его из других файлов на основани отсортированного списка
def create_file_sorted_by_lenght(file_info):
    right_lines = sorted(list(file_info.values()))
    result = open('result.txt', 'w+')
    for lines in right_lines:
        for number_doc, number_lines in file_info.items():
            if number_lines == lines:
                result.write(f'{number_doc}.txt\n{number_lines}\n')
                with open(number_doc+'.txt', 'rt') as f:
                    for line in f:
                        result.write(line)
                    else:
                        result.write('\n')
    result.close()


main()
