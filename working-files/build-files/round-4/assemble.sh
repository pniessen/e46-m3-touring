#!/bin/sh
# usage: sh assemble.sh TARGET_DIR   (TARGET_DIR holds a copy of the guide; the four pages are rewritten from the fragments)
set -e
R=/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold
T=$1
cd $R
python3 frag.py join frags "$T"
python3 -I tools/apply_redraws.py "$T" $R/diagrams
python3 -I tools/figures.py "$T" $R/diagrams
python3 -I tools/checklinks.py "$T"
echo "placeholders left:"; grep -n -o '<!-- figure: [^>]*-->' "$T"/README.md "$T"/WIRING-AND-CODING.md || echo none
