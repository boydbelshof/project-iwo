#!/bin/bash
# Descr: prints the amount of times the word 'de' occurs
# 	 in a file
#
# Usage: ./wordfreqDE.sh FILE
#
#argument is the file. check if we get it. 

TEXT=$1
if [ -z "$TEXT" ]
then
	echo "specify a twitter file!"
	exit
fi

#split by space, remove empty lines, sort by frequency
cat $TEXT | tr ' ' '\n' | sed '/^$/d' | sort | uniq -c | sort -nr | grep -G '\sde$'

python clean_names.py
echo "Names cleaned, duplicates are removed."

zless $TEXT | /net/corpora/twitter2/tools/tweet2tab user.name text rt.id | python code.py
echo "Twitter data processed, check the output.txt file for the result"
