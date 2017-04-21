#!/urs/bin/env python3
# -*- coding: utf-8 -*-
# FS17, PCL II, Übung 4
# Aufgabe 1
# Valentina Vogel & Martina Stüssi

import lxml.etree as ET
import glob

def getfreqwords(indir, outfile):


	all_files = glob.glob(indir +'/SAC-Jahrbuch_*_mul.xml')
	

	my_dict = {}
	for file in all_files:
		tree = ET.iterparse(file, events=('end',), tag='s')

		for _, sentence in tree:
			sents = ''
			wc = 0
			for word in sentence.iterfind('.//w'):
				lemma = str(word.get('lemma'))
				sents += '{} {}'.format(' ', lemma)
				word.clear()
			if len(sents.split()) > 5:
				if sents in my_dict:
					my_dict[sents] += 1
				else:
					my_dict[sents] = 1
			sentence.clear()

	#sorted_dict = sorted(my_dict, key=my_dict.get, reverse=True)

	for item in my_dict:
		if my_dict[item] > 2:
			print(item, my_dict[item])


	#outfile.write(sorted_dict[0:20])







def main():


	path = 'SAC'
	ausgabe = open('haeufigste-worter.txt', 'w')

	getfreqwords(path, ausgabe)

	ausgabe.close()

if __name__ == '__main__':
	main()