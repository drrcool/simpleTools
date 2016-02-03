#!/bin/bash
# Wrapper to run the MMIRS task mask2dxf on all .msk files in your current
# working directory.

# If mask2dxf is located somewhere else, just change this path
binfile=/usr/local/bin/mask2dxf

for filename in *.msk
do
	fileroot="${filename%.*}"
	$binfile < $fileroot.msk > $fileroot.dxf
done
