
import re
import csv

rexp = re.compile(
    "[:/\\?#\\[\\]@!\\$&'\\(\\)\\*\\+,;=< >\" \\{\\}\\|\\\\^`]  ")


def q_f(m):
    return '%{:02X}'.format(ord(m.group(0)))


def uri_quote(s):
    return rexp.sub(q_f, s)


with open('programm3.csv', 'r', newline='', encoding='utf-8') as ifp:

    ir = csv.reader(ifp)
    for i in ir:
        s = ('_:' + i[0])
        p = ('<' + i[1] + '>')
        o = ('<' + i[2] + '>')
        # tin 2 stili tin pername apo tis parapano sinartiseis
        # ean i 1 stili den einai ena apo ta parakato perna to apo tis sinartiseis allios
        # apo8ikeuse to se mia apli metabliti
        if i[1] == 'http://host/p16papa3/vocabulary#ΕΝΑΡΞΗ' or i[1] == 'http://host/p16papa3/vocabulary#ΛΗΞΗ':
            o = (i[2] + '^^<http://www.w3.org/2001/XMLSchema#time>')

        if i[1] == 'http://host/p16papa3/vocabulary#ΗΜΕΡΑ':

            o = (i[2])
        print(' {} {} {} .'.format(s, p, o))
