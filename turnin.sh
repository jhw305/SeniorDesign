#!/usr/bin/env bash

pysrc=src/simlib/src/
errcnt=0

echo "Building project..."
make
echo "Running turnin script..."
for file in $pysrc/*.py ; do
	# Run unit test in all Python source files
	# Error code returned by each file is total number of errors
	# in unit test. Sum should be 0 for the build to pass.
	echo "Testing $file..."
	./$file
	errcnt=$((errcnt+"$?"))
done
echo "Total error count: $errcnt"
if [ "$errcnt" != "0" ] ; then
	echo "Please fix errors. Not pushing."
else
	echo "No errors. Now pushing."
	git push
fi
