#!/bin/sh
# usage: sh changed.sh PAGE FRAGMENT_FILE   -> unified diff of this round's changes to one section (new fragments print in full)
R=/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold
if [ -f "$R/frags-orig/$1/$2" ]; then diff -u "$R/frags-orig/$1/$2" "$R/frags/$1/$2"; else echo "(new fragment)"; cat "$R/frags/$1/$2"; fi
