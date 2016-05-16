# Monty

Better than self documented code, self commented code

Everybody hates writing comments. And erverybody is complaining about missing helpful comments.

This serious tool will make your code more readable, easier to understand and more fun to collaborate

### MAKE COLLABORATION GREAT AGAIN!

## Setup
`brew install ruby`

`pip install requests`

`chmod +x install-monty.sh`

`cp install-monty.sh /usr/local/bin/install-monty.sh`


From the project directory you'd like to set up:
`install-monty.sh <full_path_to_this_dir>`

`chmod +x /usr/local/bin/monty.sh`

Now you can run `monty.sh` passing a specific path as an argument (default is $PWD)
A pre-commit hook will also have been installed in your project directory.

## Hall of Fame

```
#&# NOTFOUND is 404 but it could also be 746.113 or 13416.0

NOTFOUND=404 
```

```
#&# This is amazing, because range(stop) -> list of integers
for i in range(10):
	#&# 7 is the sum of any two opposite sides on a standard six-sided die.
	LOG += 7
```

```
#&# logbuffer is a semaphores tor thread locking
	logbuffer=""
	```
## Hall of Shame

```
#TODO: consider scenario where a > 0
if a > 0:
```

```

		#&# It was working in my head

		print "Not Supported: directories / /etc /bin /lib /tmp /usr /dev /sbin"

		#&# The original specification contained conflicting requirements

		print "The -d flag runs the server as a daemon"

		#&# I must have been stress testing our production server

		print "No warranty given or implied"

```


## Comment Types

[x] Stackoverflow link (search for namespace of modules with 'bug')

[x] operator comments (e.g. +, =)

[x] meaning for variables (`todos = [] # this array contains ...`)

[x] todos

[x] fixme

[x] do not touch

[x] faked phrases

[x] ~~reasons~~ excuses ~~(## do this for compatibility with version 3 from __future__ import print_function)~~

[ ] git blame and commit logs

[ ] poetry

[ ] random facts

[x] number facts

[ ] ascii arts

