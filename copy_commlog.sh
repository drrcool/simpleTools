#!/bin/bash

for filename in */commlog.ps
do
    
    dirval="${filename%/*}"
    fname="${filename#*/}"
    echo $dirval\_$fname
    cp $filename /home/mmirs/rcool/$dirval\_$fname
done
