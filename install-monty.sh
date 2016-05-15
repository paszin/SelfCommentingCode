#!/bin/sh

echo "python $1/main.py" '$PWD' "\ngit add ." "\nexit 0" > $PWD/.git/hooks/pre-commit

echo "#!/bin/sh
python $1/main.py" '$@' > /usr/local/bin/monty.sh
