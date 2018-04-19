#!/bin/bash

pythonfile=$1
pythonfilename=`basename $pythonfile .py`
tempcythonfile="${pythonfilename}.pyx"
cythonfilename=$2

cp $pythonfile $tempcythonfile
cythonize $tempcythonfile build_ext --inplace
mv ${pythonfilename}.*.so "${cythonfilename}.so"
rm "${pythonfilename}.c"
rm "${pythonfilename}.pyx"

exit 0;
