#!/urs/bin/env python3
# -*- coding: utf-8 -*-
# FS17, PCL II, Übung 4
# Aufgabe 2
# Valentina Vogel & Martina Stüssi

import lxml.etree as ET
import random
import bz2
import gc


def gettitles(infile, testfile, trainfile, k):
    """Selects k random titles from infile for testfile, adds rest to trainfile"""

    parser = ET.iterparse(infile, events=('end',), \
        tag='{http://www.mediawiki.org/xml/export-0.10/}title')

    #Reservoir for sample
    reservoir = []

    for position, item in enumerate(parser):

        if position < k:
            #adds first k items to reservoir
            reservoir.append(item[1].text)
        else:
            m = random.randint(0, position)
            if m < k:
                trainfile.write(reservoir[m])
                reservoir[m] = item[1].text
                trainfile.write('\n')
            else:
                trainfile.write(item[1].text)
                trainfile.write('\n')

        item[1].clear()

        for ancestor in item[1].xpath('ancestor-or-self::*'):
            while ancestor.getprevious() is not None:
                del ancestor.getparent()[0]


    for word in reservoir:
        testfile.write(word)
        testfile.write('\n')




def main():

    gesamtdatei = bz2.open('dewiki-latest-pages-articles.xml.bz2', mode='r', \
        compresslevel=9, encoding=None, errors=None, newline=None)

    gc.enable()

    testen = open('testfile.txt', 'w')
    trainieren = open('trainfile.txt', 'w')


    print(gettitles(gesamtdatei, testen, trainieren, 100))



    testen.close()
    trainieren.close()
    gesamtdatei.close()



if __name__ == '__main__':
    main()

#http://stackoverflow.com/questions/12160418/why-is-lxml-etree-iterparse-eating-up-all-my-memory