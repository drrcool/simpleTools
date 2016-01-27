#!/usr/bin/bash
#This just removes commas from  all the dat files in the directory.
#Helpful for when someone sends data that's both comma and white separated and 
#(Though I coudl just split on both, but :effort:)


for f in *.dat
do
	/usr/bin/sed "s/\,/ /g" $f > "new_"$f
	/bin/cp "new_"$f $f
	/bin/rm "new_"$f
done

