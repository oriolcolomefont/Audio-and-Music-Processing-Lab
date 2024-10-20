# -*- coding: utf-8 -*-

import sys, glob, json, codecs, platform
sys.path.append("ArabicTransliterator/")
import arabic_reshaper
from bidi.algorithm import get_display
from uuid import UUID

def print_reshape(text):
    """Reshapes arabic in order to display characters from right to left
    """
    if platform.system() == "Darwin":
        print text
    else:
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)
        print bidi_text


if __name__ == '__main__':
	for data in ("original", "transliterated"):
		for filename in sorted(glob.glob("data/%s/json/*.json" % data)):
			print filename
			recording_sanas = json.load(codecs.open(filename, "r", "utf-8"))
			for recording_sana in recording_sanas:
				print_reshape(recording_sana['title'])
				print_reshape(recording_sana['type'])
				print_reshape(recording_sana['identifier'])
				for section in recording_sana['sections']:
					for verse in section:
						print len(verse)
						for hemistich in verse[1:]:
							print_reshape(hemistich)
				print "---------------------"
			break
