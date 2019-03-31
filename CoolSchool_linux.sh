#!/bin/bash

PROGRAMS=""
COLORAMA=false
SYMPY=false
NUMPY=false
SCIPY=false
PYINSTALLER=false

echo "Scanning system for required libraries..."

for PIP_LIST_OUTPUT in `pip3 list --format=columns`; do
    if [ "$PIP_LIST_OUTPUT" == "colorama" ]; then
		COLORAMA=true
	elif [ "$PIP_LIST_OUTPUT" == "sympy" ]; then
		SYMPY=true
	elif [ "$PIP_LIST_OUTPUT" == "numpy" ]; then
		NUMPY=true
	elif [ "$PIP_LIST_OUTPUT" == "scipy" ]; then
		SCIPY=true
	elif [ "$PIP_LIST_OUTPUT" == "PyInstaller" ]; then
		PYINSTALLER=true
	fi
done

if [ $COLORAMA == false ]; then
	PROGRAMS+="colorama "
fi
if [ $SYMPY == false ]; then
	PROGRAMS+="sympy "
fi
if [ $NUMPY == false ]; then
	PROGRAMS+="numpy "
fi
if [ $SCIPY == false ]; then
	PROGRAMS+="scipy "
fi
if [ $PYINSTALLER == false ]; then
	PROGRAMS+="pyinstaller "
fi

if [ ! -z "$PROGRAMS" ]; then
	pip3 install $PROGRAMS
else
	echo "All libraries already installed."
	echo "Press a key to continue..."
	read
fi

clear
python3 CoolSchool.py
