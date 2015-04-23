#!/bin/bash

check_file () {
    if [ -f "$1" ]
    then
        echo "$1 found"
    else
        echo "$1 not found"
        exit -1
    fi
}

echo "Checking for all files"

check_file "apiary.apib"
check_file "IDB.log"
check_file "models.html"
check_file "models.py"
check_file "tests.py"
check_file "tests.out"
check_file "UML.pdf"
check_file "__init__.py"
check_file "db_create.py"
check_file "README.md"