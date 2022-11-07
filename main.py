import os


def main():
    files = ['1.txt', '2.txt', '3.txt']
    files_info = lenght_file(files)
    create_file_sorted_by_lenght(files_info)


def lenght_file(files):
    file_info = {}
    for file in files:
        with open(file, 'rt') as f:
            file_info[file.replace('.txt', '')] = len(list(f))
    return file_info


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
