#!/urs/bin/env python3
# -*- coding: utf-8 -*-
# FS17, PCL II, Übung 4
# Aufgabe 1
# Valentina Vogel & Martina Stüssi

import lxml.etree as ET
import glob
import operator

def getfreqwords(indir, outfile):
	my_dict = {}
	for file in indir:
		# alle sätze
		tree = ET.iterparse(file, events=('end',), tag='s')

		for _, sentence in tree:
			sents = ''
			wc = 0
			for word in sentence.iterfind('.//w'):
				lemma = str(word.get('lemma'))
				sents += '{} {}'.format(' ', lemma)
				word.clear()
# 			hängt jedes mal den satz an, immer plus ein wort.
			if len(sents.split()) > 5 and sents.endswith('.'):
				if sents in my_dict:
					my_dict[sents] += 1
				else:
					my_dict[sents] = 1
# 			Wichtig damit der Speicher nicht stirbt.
			sentence.clear()

	sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)

	#print(sorted_dict[:20])

	for sent, number in sorted_dict[:20]:
		outfile.write(str(number) + '\t' + str(sent) + '\n')

# 	Ausgabe implementieren
	#outfile.write(sorted_dict[0:20])


def main():
	ausgabe = open('haeufigste-saetze.txt', 'w')
	file_names = []
	for filename in glob.glob('Text+Berg_Release_152_v01/**/SAC-Jahrbuch_????_mul.xml', recursive = True):
		file_names.append(filename)

	getfreqwords(file_names, ausgabe)

	ausgabe.close()

if __name__ == '__main__':
	main()
# http://lxml.de/api/lxml.etree.iterparse-class.html
