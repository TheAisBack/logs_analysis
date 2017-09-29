# Logs Analysis

## How to Run the Log Analysis file

## Download
- Python3 - https://www.python.org/downloads/
- Virtualbox - https://www.virtualbox.org/wiki/Downloads
- Vagrant - https://www.vagrantup.com/downloads.html

## Run
- First setup vagrant environment 
- Start your terminal and locate this file
- enter `vagrant up`
- Then enter `vagrant ssh`
- Then to load the data enter `psql -d new -f newsdata.sql`
- Sidenote newsdata.sql is a large file and can't be added to this repository.
- Then finally to execute the program `enter python newsdata.py`