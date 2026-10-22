#!/bin/sh
# run.sh NN  : generate figure NN, lint it, build its test page and shoot it
set -e
cd "$(dirname "$0")"
D=/home/user/archeyon/e46-m3-touring-conversion/diagrams
case "$1" in
  19) F=19-circuit-dmtl; P="" ;;
  23) F=23-can-network; P="" ;;
  11) F=11-fuel-pump-control; P="--portrait" ;;
esac
timeout 240 python3 gen$1.py
python3 lint_b.py $D/$F.svg
python3 make_pages_b.py pages $P $D/$F.svg > /dev/null
NODE_PATH=$(npm root -g) timeout 240 node shoot_b.js shots pages/$F.html
