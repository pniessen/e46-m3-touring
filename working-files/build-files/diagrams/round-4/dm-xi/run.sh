#!/bin/sh
# Regenerate 42-xi-driveline.svg, build its test page and shoot it (light + dark, 390 px).
R=/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold
G=/home/user/archeyon/e46-m3-touring-conversion
set -e
python3 -I "$R/dgen/dm-xi/gen42.py"
python3 -I "$R/tools/make_pages.py" "$R/dtest/dm-xi/pages" "$G/diagrams/42-xi-driveline.svg"
cd "$R/tools" && NODE_PATH=$(npm root -g) node shoot.js "$R/dtest/dm-xi/shots" "$R/dtest/dm-xi/pages/42-xi-driveline.html"
