#!/bin/sh
# Regenerate one or more figures and test them: site pages at 390 px (tools/shoot.js) and
# standalone files (shoot_std.js).   sh run.sh 13 31 32 33
R=/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold
G=/home/user/archeyon/e46-m3-touring-conversion
D=$R/dgen/dm-chassis
T=$R/dtest/dm-chassis
mkdir -p $T/pages $T/shots
svgs=""
for n in "$@"; do
  python3 -I $D/gen$n.py || exit 1
  svgs="$svgs $(ls $G/diagrams/$n-*.svg)"
done
python3 -I $R/tools/make_pages.py $T/pages $svgs > /dev/null
pages=""
for s in $svgs; do pages="$pages $T/pages/$(basename $s .svg).html"; done
cd $R/tools && NODE_PATH=$(npm root -g) node shoot.js $T/shots $pages
cd $D && NODE_PATH=$(npm root -g) node shoot_std.js $T/shots $svgs
