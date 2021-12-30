# Crypto-Odin

## Setup
Ensure that you have Python3 installed. If you're on MacOS and have HomeBrew installed:
```
brew install python3
```
Make sure you also have virtualenv installed as well. This can be done by calling:
```
pip3 install virtualenv
```

## Create the venv Environment
For MacOS users, Run:
```
python3 -m venv activate
```
This will create a venv named `activate` if one doesn't already exist.

For more information, go here: https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments

## Activating the Environment
Run `. venv/bin/activate` in the command line to activate the virtual python environment.

For more information, go here: https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments

### Dependencies
- pip install requests
- pip install beautifulsoup4

### How to Run
Run `python3 main.py | pbcopy` in the command line from the root directory. This should automatically copy the output so it's easily pastable.

It is formatted to be markdown compatible, so if you want to make a post on Reddit with the output, make sure it's in markdown mode and switch back to "pretty" mode afterwards to see the markdown styles applied.
