# 8eloume n anoigoume to csv
# kai den mas endiaferei i 1 stili alla i 2 p tin metatrepoume se uri, na dio3ei mi epitreptes metablites

import re
import csv

# sinartiseis p allazoun tous mi epitreptous xaraktires
rexp = re.compile(
    "[:/\\?#\\[\\]@!\\$&'\\(\\)\\*\\+,;=< >\" \\{\\}\\|\\\\^`]  ")

# px edo allazei to / sto ΕΝΑΡΞΗ/ΛΗΞΗ se %2


def q_f(m):
    return '%{:02X}'.format(ord(m.group(0)))


def uri_quote(s):
    return rexp.sub(q_f, s)


# anoigoume to csv, k pos 8 lene to new
with open('rogramm2.csv', 'r', newline='', encoding='utf-8') as ifp, open('programm3.csv', 'w', newline='', encoding='utf-8')as ofp:

    ir = csv.reader(ifp)
    ow = csv.writer(ofp)

    # se epanali3i apo8ikeuoume se mia metabliti tin 1 stili
    for i in ir:
        s = (i[0])
        p = (i[1])
        o = i[2]
        # tin 2 stili tin pername apo tis parapano sinartiseis
        # ean i 1 stili den einai ena apo ta parakato perna to apo tis sinartiseis allios
        # apo8ikeuse to se mia apli metabliti
        if i[1] == 'http://host/p16papa3/vocabulary#ΕΝΑΡΞΗ' or i[1] == 'http://host/p16grig/vocabulary#ΛΗΞΗ':
            o = ('"' + i[2] + ':00:00"')

        if i[1] == 'http://host/p16papa3/vocabulary#ΗΜΕΡΑ':

            o = ('"' + i[2] + '"')

        ow.writerow([s, p, o])
