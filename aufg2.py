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
	"""no usfülle"""
	parser = ET.iterparse(infile, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}title')

	reservoir = []

	for position, item in enumerate(parser):
		#print(position, item[1].text)

		if position < k:
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


	for word in reservoir:
		testfile.write(word)

	return reservoir


def main():

	gesamtdatei = bz2.open('dewiki-latest-pages-articles.xml.bz2', mode='r', \
		compresslevel=9, encoding=None, errors=None, newline=None)

	gc.enable()

	testen = open('testfile.txt', 'w')
	trainieren = open('trainfile.txt', 'w')


	print(gettitles(gesamtdatei, testen, trainieren, 20))



	testen.close()
	trainieren.close()
	gesamtdatei.close()






if __name__ == '__main__':
	main()