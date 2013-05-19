#!/usr/bin/python

# -*- coding= utf8 -*-
import sys, getopt
from string import maketrans
from elot743 import *

def replace_all(text, dic):
	for i, j in dic.iteritems():
    		if i != j:
        		text = text.replace(i, j)
	text.replace(',' , '\n')
	return text

def readFile(infile):
	print "reading file",infile,"...\n"
	i = open(infile, 'r')
	array=[]
	for line in i:
		array.append(replace_all(line.rstrip('\n'),dict))

	i.close()
	return array
	print "\nfinished reading file!\n"

def writeFile(outfile, array):
	print "writing to file",outfile,"...\n"
	print array
	o = open(outfile, 'w')
	for item in array:
 		o.write("%s\n" % item)
 	o.close()
	print "\nfinished writing to file!\n" 

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'names.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'names.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   if inputfile == '':
      inputfile = raw_input('File where the names to be translated exist (ex. names.txt) : ')
   if outputfile =='':
      outputfile = raw_input('File where the translated names will be written (ex. trnames.txt) : ')    
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

   transArray=[]

   transArray=readFile(inputfile)
   writeFile(outputfile,transArray)
   print 'File is translated!'

if __name__ == "__main__":
   main(sys.argv[1:])
