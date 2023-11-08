#!/bin/bash
workdir='/Users/jeffreyeardley/Desktop/Personal_Projects/personal-assistant'
touch "$workdir/python_scripts/test.py"
echo "print('hello world')" >> "$workdir/python_scripts/test.py"
python3 "$workdir/python_scripts/test.py"
