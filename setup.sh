#!/bin/bash -e

# setup virtualenv
pip install virtualenv
virtualenv venv -p python2.7
source venv/bin/activate
pip install --upgrade -r requirements.txt

# Mac code signing shitty hack
if [[ $(uname) == "Darwin" ]]; then
    codesign -f -s - ./venv/bin/python
    codesign -v ./venv/bin/python
    ret1=$?
    codesign -f -s - ./venv/bin/python2.7
    codesign -v ./venv/bin/python2.7
    ret2=$?
    if [[ $ret1 != 0 ]] || [[ $ret2 != 0 ]]; then
        echo "Failed to execute codesign hack."
        exit
    fi
fi
