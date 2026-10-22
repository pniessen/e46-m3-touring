#!/bin/sh
# usage: sh run.sh NN   (generate figure NN, build its test page as the brief says, shoot and check)
set -e
R=/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold
D=$R/dgen/dm-coding-b
T=$R/dtest/dm-coding-b
G=/home/user/archeyon/e46-m3-touring-conversion/diagrams
cd $D
python3 -B gen$1.py
F=$(ls $G/$1-*.svg)
python3 -I $R/tools/make_pages.py $T/pages $F >/dev/null
cd $R/tools && NODE_PATH=$(npm root -g) node shoot.js $T/shots $T/pages/$(basename $F .svg).html
