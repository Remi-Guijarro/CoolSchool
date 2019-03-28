#!/bin/bash

PROGRAMS=""
COLORAMA=false
SYMPY=false
NUMPY=false

for PIP_LIST_OUTPUT in `pip3 list --format=columns`; do
    if [ "$PIP_LIST_OUTPUT" == "colorama" ]; then
		COLORAMA=true
	elif [ "$PIP_LIST_OUTPUT" == "sympy" ]; then
		SYMPY=true
	elif [ "$PIP_LIST_OUTPUT" == "numpy" ]; then
		NUMPY=true
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

if [ ! -z "$PROGRAMS" ]; then
	pip3 install $PROGRAMS
fi

clear
python3 CoolSchool.py
