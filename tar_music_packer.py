#! /bin/python
import string
from os import walk


f=[]
for (dirname,dirpath,filenames) in walk("/home/kreid/music"):
    f.extend(dirname)
print f


arr =[]
x = 0
for letter in string.ascii_uppercase:
    arr.append(letter)
    x = x+1
print arr
x = 0

#I need an array with 26 elements, each one contating the corresponding folde


#counter=0
#for letter in {A..Z}
#do
#	for i in $list
#	do
#		if [ ${i:2:1} == $letter ]
#		then
#			declare -a tar_array_$letter[$counter]=$i
#			let "counter = $counter + 1"
#		else
#			let "counter = 0"
#				fi
#	done	


