##@file format_js.py
#@brief Uses jsbeatifier to format js files into another file
#@details The CLI parameters could be the same file, so changes will be shown on it
#@author Rafael Karosuo


import sys #CLI params
import os #r/w files
import jsbeautifier #js formatter

my_formatted_file = None
original_file = None
try:
	if len(sys.argv) == 3:
		try:						
			original_file = open(sys.argv[1]) #Open the original unformatted file			
			formatted_string = original_file.read() ##Read all unformatted file
			formatted_string = jsbeautifier.beautify(formatted_string) #Format it
			my_formatted_file = open(sys.argv[2],'w',os.O_NONBLOCK) #Open output file, if it's the same do it after the reading ops
			my_formatted_file.write(formatted_string) #write it down
		except IOError as e:
			print("IOError: {!s}".format(e))
	else:
		print('\n>>Error\nNeed to provide at least 2 params.\n\nUsage: '+sys.argv[0]+' <file_to_format.js> <output_file.js>\n')
	
except KeyboardInterrupt:
	if my_formatted_file is not None and original_file is not None:
		print("\nClosing {!s} file...".format("my_formatted_file"))
		my_formatted_file.close()
		print("\nClosing {!s} file...".format("original_file"))
		original_file.close()
