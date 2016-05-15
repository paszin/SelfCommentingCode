#!/bin/sh

"python $1/main.py
git add .
exit 0" > $PWD/.git/hooks/pre-commit

"#!/bin/sh
$1/main.py " + '$@' > /usr/local/bin/monty.sh
