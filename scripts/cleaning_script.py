import os
from collections import OrderedDict
import string

from copy import copy

parts = 'book', 'BOOK', 'Book', 'chapter', 'CHAPTER', 'Chapter', 'SECTION', 'Section', 'section', \
        'SECT', 'Sect', 'sect', 'PART', 'Part', 'part', 'essay', 'Essay', 'ESSAY', 'Cap', 'CAP', \
        'cap', 'lecture', 'LECTURE', 'Lecture', 'vol', 'VOL', 'Vol', '§', 'CHAP', 'Chap'

roman = []

punctuations = '.', '-', '--', ':', '_', '—', ','

alphabet = string.ascii_uppercase


def write_roman(num):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


# generate roman numbers
for i in range(1, 150):
    char = write_roman(i).upper()
    roman.append(char)


def remove_punctuations(line: str):
    new_line = line
    for i in punctuations:
        if line.startswith(i):
            new_l = line.strip(i)
            new_li = new_l.strip()
            new_line = remove_punctuations(new_li)
            break
    return new_line


def remove_chapter_name(line: str):
    new_linee = ''
    if len(line) <= 3:
        new_linee = '\n'
    else:
        for i in parts:
            if line.startswith(i):
                new_l = line.strip(i)
                new_li = new_l.strip()
                new_line = remove_punctuations(new_li)
                new_linee = remove_numbers(new_line)
                break
    if new_linee != '':
        return new_linee
    else:
        return line


def remove_roman_numbers(line: str):
    new_line = ''
    for m in roman:
        if len(m) > 1:
            if line.startswith(m):
                new_l = line.strip(m)
                new_li = new_l.strip()
                new_lin = remove_punctuations(new_li)
                new_line = remove_roman_numbers(new_lin)
                break
        else:
            if len(line) < 3:
                new_line = '\n'
                break
            else:
                if line[1] in punctuations:
                    if line.startswith(m):
                        new_l = line.strip(m)
                        new_li = new_l.strip()
                        new_line = remove_punctuations(new_li)
                        break
    if new_line != '':
        return new_line
    else:
        return line


def remove_numbers(line: str):
    new_line = ''
    for i in range(0, 350):
        if line.startswith(str(i)):
            new_l = line.strip(str(i))
            new_li = new_l.strip()
            new_lin = remove_punctuations(new_li)
            new_line = remove_numbers(new_lin)
            break
    if new_line != '':
        return new_line
    else:
        return line


def remove_illustrations(line: str):
    new_line = ''
    if '[ILL' in line or '(ILL' in line or '(Ill' in line or '[Ill' in line:
        new_line = '\n'
    if new_line != '':
        return new_line
    else:
        return line


def remove_stars(line: str):
    new_line = ''
    if line != '\n':
        if line.count('*') or line.count('.') >= 5:
            new_line = '\n'
    if new_line != '':
        return new_line
    else:
        return line


def remove_notes(line: str):
    new_line = ''
    new_lineee = ''
    for i in range(0, 350):
        note1 = '[' + str(i) + ']'
        note2 = '(' + str(i) + ')'
        note3 = '(<i>' + str(i) + '</i>).'
        note4 = '=' + str(i) + '.='
        note5 = '{'+str(i)+'}'
        footnote = '[Footnote: '+str(i)+']'
        sidenote = 'Sidenote'
        if note1 in line:
            new_lin = line.replace(note1, '')
            new_line = new_lin.strip()
            break
        if note2 in line:
            new_lin = line.replace(note2, '')
            new_line = new_lin.strip()
            break
        if note3 in line:
            new_lin = line.replace(note3, '')
            new_line = new_lin.strip()
            break
        if note4 in line:
            new_lin = line.replace(note4, '')
            new_line = new_lin.strip()
            break
        if note5 in line:
            new_lin = line.replace(note5, '')
            new_line = new_lin.strip()
            break
        if sidenote in line:
            new_line = '\n'
            break
        if footnote in line:
            new_lin = line.replace(footnote, '')
            new_line = new_lin.strip()
            break
    for j in alphabet:
        note6 = '['+j+']'
        if new_line != '':
            if new_line.startswith(note6):
                new_lineee = '\n'
                break
            elif note6 in new_line:
                new_linee = new_line.replace(note6, '')
                new_lineee = new_linee.strip()
                break
    if new_lineee != '':
        return new_lineee
    elif new_line != '':
        return new_line
    else:
        return line


path = '/home/cecile/Bureau/scriptNLP/texts/'

if __name__ == "__main__":
    for filename in os.listdir(path):
        with open('/home/cecile/Bureau/scriptNLP/texts/' + filename, 'r') as file:
            lines = copy(file.readlines())
        with open('/home/cecile/Bureau/scriptNLP/texts/' + filename, 'w') as file:
            cpt_empty_lines = 0
            index = 0
            for l in lines:
                if index == 0 and l == '\n':
                    """"""
                else:
                    index += 1
                    if cpt_empty_lines == 1 and l == '\n':
                        """"""
                    else:
                        cpt_empty_lines = 0
                        l0 = l.strip()
                        l1 = remove_notes(l0)
                        l2 = remove_chapter_name(l1)
                        l3 = remove_roman_numbers(l2)
                        l4 = remove_numbers(l3)
                        l5 = remove_illustrations(l4)
                        l6 = remove_stars(l5)
                        lfinal = l6.strip()
                        if not lfinal.endswith('\n'):
                            lfinal += '\n'
                        if lfinal == '\n':
                            cpt_empty_lines += 1
                        file.write(lfinal)
        file.close()
