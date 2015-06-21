#!/usr/bin/env bash
#Change these variables to your own corresponding directories.
CGIDIR=/Library/WebServer/CGI-Executables

#Copy all the files
cp -r *.py ${CGIDIR}
cp -r default_error ${CGIDIR}
cp -r html_template ${CGIDIR}
cp conf.txt ${CGIDIR}

#Add executable permission to python scripts.
find ${CGIDIR} -name "*.py" | xargs chmod a+x



