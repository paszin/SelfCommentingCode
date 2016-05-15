#!/bin/sh

echo "python $1main.py
git add .
exit 0" > $PWD/.git/hooks/pre-commit

echo "#!/bin/sh
python $1main.py" '$@' > /usr/local/bin/monty.sh
