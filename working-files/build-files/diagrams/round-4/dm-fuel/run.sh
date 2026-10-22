#!/bin/sh
# usage: sh run.sh 34 [land|brief|both]   generate, build a test page, shoot and check
D=/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold/dgen/dm-fuel
R=/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold
T=$R/dtest/dm-fuel
G=/home/user/archeyon/e46-m3-touring-conversion/diagrams
cd $D
python3 gen$1.py; rc=$?
if [ $rc -eq 3 ]; then python3 gen$1.py || exit 1; elif [ $rc -ne 0 ]; then exit 1; fi
F=$(ls $G/$1-*.svg)
NP=$(npm root -g)
case "${2:-land}" in
  land|both)
    python3 -I make_pages_land.py $T/land/pages $F >/dev/null
    NODE_PATH=$NP node shoot_land.js $T/land/shots $T/land/pages/$(basename $F .svg).html ;;
esac
case "${2:-land}" in
  brief|both)
    python3 -I $R/tools/make_pages.py $T/pages $F >/dev/null
    cd $R/tools && NODE_PATH=$NP node shoot.js $T/shots $T/pages/$(basename $F .svg).html ;;
esac
