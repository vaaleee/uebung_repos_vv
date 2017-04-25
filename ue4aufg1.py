#!/urs/bin/env python3
# -*- coding: utf-8 -*-
# FS17, PCL II, Übung 4
# Aufgabe 1
# Valentina Vogel & Martina Stüssi

import lxml.etree as ET
import glob
import operator

def getfreqwords(indir, outfile):
    """Gets most frequent lemma sentences out of directory with xml files"""

    file_names = []
    for filename in glob.glob(indir, recursive = True):
        file_names.append(filename)
    # Test ob glob funktioniert
    #print(file_names)

    my_dict = {}
    for file in file_names:
        # parses the sentences for each file
        tree = ET.iterparse(file, events=('end',), tag='s')

        for _, sentence in tree:
            #makes a string out of the sentences and adds them to a dict
            sents = ''
            wc = 0
            for word in sentence.iterfind('.//w'):
                lemma = str(word.get('lemma'))
                sents += '{} {}'.format(' ', lemma)
                word.clear()

            if len(sents.split()) > 5 and sents.endswith('.'):
                if sents in my_dict:
                    my_dict[sents] += 1
                else:
                    my_dict[sents] = 1
            sentence.clear()

    sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)

    #print(sorted_dict[:20])
# writes output into file
    for sent, number in sorted_dict[:20]:
        outfile.write(str(number) + '\t' + str(sent) + '\n')



def main():
    ausgabe = open('haeufigste-saetze.txt', 'w')

    directory = '**/SAC/SAC-Jahrbuch_????_mul.xml'

    getfreqwords(directory, ausgabe)

    ausgabe.close()

if __name__ == '__main__':
    main()
# http://lxml.de/api/lxml.etree.iterparse-class.html
