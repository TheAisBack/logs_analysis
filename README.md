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
- Then to load the data enter `psql -d news -f newsdata.sql`
- Sidenote newsdata.sql is a large file and can't be added to this repository.
- Enter the data and enter `psql -d news`
- Create two views
- `CREATE VIEW views`
- `CREATE VIEW error`
- Hit control D to exit psql
- Then finally to execute the program enter `python newsdata.py`