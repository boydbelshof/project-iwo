#!/bin/bash
# Descr: generate a word frequency list order output
#		 by frequency (words split by space)
#
# Usage: ./wordfreq.sh FILE
#
#argument is the file. check if we get it. 

TEXT=$1
if [ -z "$TEXT" ]
then
	echo "specify a file!"
	exit
fi
#split by space, remove empty lines, sort by frequency
cat $TEXT | tr ' ' '\n' | sed '/^$/d' | sort | uniq -c | sort -nr | grep -G '\sde$'
