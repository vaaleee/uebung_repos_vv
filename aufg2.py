#!/urs/bin/env python3
# -*- coding: utf-8 -*-
# FS17, PCL II, Übung 4
# Aufgabe 2
# Valentina Vogel & Martina Stüssi

import lxml.etree as ET
import random
import bz2



def gettitles(infile, testfile, trainfile, k):
	"""no usfülle"""
	parser = ET.iterparse(infile, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}title')

	reservoir = []
	counter = 0

	for event, element in parser:

		mein_tuple = (counter, element.text)
		if counter < k:
			reservoir.append(element.text)
		else:
			m = random.randint(0, counter)
			if m < k:
				reservoir[m] = element.text
		counter += 1
		element.clear()

	return reservoir


	for word in reservoir:
		testfile.write(word)

def main():

	gesamtdatei = bz2.open('dewiki-latest-pages-articles.xml.bz2', mode='r', \
		compresslevel=9, encoding=None, errors=None, newline=None)


	testen = open('testfile.txt', 'w')
	trainieren = open('trainfile.txt', 'w')


	print(gettitles(gesamtdatei, testen, trainieren, 20))



	testen.close()
	trainieren.close()






if __name__ == '__main__':
	main()