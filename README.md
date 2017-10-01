# Logs Analysis

## How to Run the Log Analysis file

## Download
- [GIT](https://git-scm.com/downloads)
- [Python3](https://www.python.org/downloads/)
- [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)

## Run
- First setup vagrant environment 
- Start your terminal and locate this file
- enter `vagrant up`
- Then enter `vagrant ssh`
- Then to load the data enter `psql -d news -f newsdata.sql`
- Sidenote [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) is a large file and can't be added to this repository.
- Enter the data and enter `psql -d news`
- Type the following code to get the answers:
- First Query:
`CREATE VIEW views AS 
 SELECT title, count(*) AS views 
 FROM articles, log 
 WHERE articles.slug=substring(log.path FROM 10) 
 GROUP BY articles.title 
 ORDER BY views 
 DESC LIMIT 3`
- Second Query:
> quote `SELECT name, count(*) AS views 
 FROM authors, articles, log
 WHERE articles.slug = substring(log.path FROM 10)
 GROUP BY authors.name 
 ORDER BY views 
 DESC LIMIT 4`
- Third Query:
`SELECT to_char(time, 'FMMonth DD, YYYY'), round(100.0*sum(case log.status when '404 NOT FOUND' then 1 else 0 end)/count(log.status), 2) AS error
 FROM log
 GROUP BY to_char(time, 'FMMonth DD, YYYY')
 ORDER BY error 
 DESC LIMIT 1`
- Hit `control + D` on your keyboard to exit psql
- Then finally to execute the program enter `python newsdata.py`