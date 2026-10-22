#!/bin/sh
# usage: sh run.sh 21   (generate, build the test page, shoot and check)
set -e
D=/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/diagrams-test/circuits-a
G=/home/user/archeyon/e46-m3-touring-conversion/diagrams
cd $D
python3 gen$1.py
F=$(ls $G/$1-*.svg)
python3 -I make_pages.py $D/pages $F >/dev/null
NODE_PATH=$(npm root -g) node shoot.js $D/shots $D/pages/$(basename $F .svg).html
