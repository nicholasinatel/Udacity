# Udacity-Log-Analysis-Project

Visit my Portfolio at: [nicklobo](http://nicklobo.com.br/)

# What it is
Internal reporting tool that uses information from the database to discover user behavior, creating an informative summary from logs.
The tool is run throw command-line and returns the result from complex queries for business conclusions over data.

Technologies used:
- [PostgreSQL](https://www.postgresql.org/) - Open source object-relation database system.
- [psycopg2](http://initd.org/psycopg/docs/usage.html) - A PostgreSQL adapter for the Python programming language. It is a wrapper for the libpq, the official PostgreSQL client library.

Tools:
- [VirtualBox](https://www.virtualbox.org/) - x86 and AMD64/Intel64 virtualization.
- [Vagrant](https://www.vagrantup.com/) - Tool for building and managing virtual machine environments in a single workflow.

## Table of Contents
- [What it is](https://github.com/nicholasinatel/Udacity/tree/master/Projects/07-/#what-it-is)
- [QuickStart](https://github.com/nicholasinatel/Udacity/tree/master/Projects/07-/#quickstart)
- [Objective](https://github.com/nicholasinatel/Udacity/tree/master/Projects/07-/#objective)
- [Details](https://github.com/nicholasinatel/Udacity/tree/master/Projects/07-/#details)
- [License](https://github.com/nicholasinatel/Udacity/tree/master/Projects/07-/#license)

## Dependencies
Install the following softwares
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) - Install the platform package for your operating system. There is no need for installing the extension pack or the SDK. Do not launch Virtual Box, the Vagrant software will run it.
- [Vagrant](https://www.vagrantup.com/downloads.html) - Download the version of your operating system.

After downloading the software’s, git clone the virtual machine configuration at your work station:
- [log-analysis](https://github.com/nicholasinatel/Udacity/tree/master/Projects/07-Log-Analysis) - This will give you a folder called FSND-Virtual-Machine, containing the VM files.

- [postgresql-table](https://drive.google.com/open?id=1PvQHYcsbdiavXjurodWcszaf7a23q7Bf) - Download this file, extract and paste at `FSND-Virtual-Machine/vagrant/project/`


## Configuration
1 - **Start the virtual machine** by going to the `FSND-Virtual-Machine/vagrant/` folder and executing `vagrant up` , once the command finishes running, type `vagrant ssh`

2 - **Inside the vagrant environment**, run `cd /vagrant` for the shared folder with access to the Virtual Machine, your current OS and the project files.

3 - First you need to import the sql database, go to the `/vagrant/project` directory and import the database by executing `psql -d news -f newsdata.sql` . The command is performing the following actions:
```
psql // the PostgreSQL command line program
-d news // connect to the database named news which has been set up previously
-f newsdata.sql // run the SQL statements 
```

4 - Now you need to connect to the database to create 3 SQL Views before implementing the **psycopg2** 

``` psql -d news ```

5 - First view, in the psql terminal, enter:
```
CREATE VIEW pop_articles AS
SELECT ARTICLES.title, COUNT(SPLIT_PART(path, '/article/', '2')) AS NUM 
FROM ARTICLES
JOIN log ON ARTICLES.slug = SPLIT_PART(path, '/article/','2')
GROUP BY ARTICLES.title 
ORDER BY NUM DESC
LIMIT 3;
```
6 - Second view:
```
CREATE VIEW pop_authors AS
SELECT AUTHORS.name, count(log.path) AS NUM 
FROM AUTHORS 
JOIN ARTICLES ON AUTHORS.id = ARTICLES.author
JOIN log ON ARTICLES.slug = SPLIT_PART(path, '/article/', '2')
GROUP BY AUTHORS.name 
ORDER BY NUM DESC;
```
7 - Third and last view:
```
CREATE VIEW error_days AS
WITH CTE_1
AS
(
SELECT 
DATE_TRUNC('day', TIME) as day,
COUNT(DATE_TRUNC('day', TIME)) AS total_day_error
FROM log
WHERE STATUS != '200 OK'
GROUP BY day
), CTE_2 AS(
SELECT 
DATE_TRUNC('day', TIME) as day2,
COUNT(DATE_TRUNC('day', TIME)) AS total_day_ok
FROM log
WHERE STATUS = '200 OK'
GROUP BY day2
)
SELECT
DATE_PART('month', TIME) as month_log,
DATE_PART('day', TIME) as day_log,
DATE_PART('year', TIME) as year_log,
(100.0 * (CAST(CTE_1.total_day_error AS FLOAT)/CTE_2.total_day_ok)) AS Percent
FROM log AS T1
JOIN CTE_1 ON DATE_TRUNC('day', TIME) = CTE_1.day
JOIN CTE_2 ON CTE_1.day = CTE_2.day2
WHERE T1.STATUS = '200 OK' AND (100.0 * (CAST(CTE_1.total_day_error AS FLOAT)/CTE_2.total_day_ok)) > 1
GROUP BY month_log, day_log, year_log, CTE_1.total_day_error, CTE_2.total_day_ok;
```

8 - To log out from psql terminal type `\q` and `enter`

# Code Execution

At the vagrant terminal, run: `python projectdb.py`

You should see the resulting query from the database, that must be similar to  this:
```
   --//--

The most popular three articles:

Candidate is jerk, alleges rival - 338647 views

Bears love berries, alleges bear - 253801 views

Bad things gone, say good people - 170098 views

   --//--

The most popular authors:

Ursula La Multa - 507594 views

Rudolf von Treppenwitz - 423457 views

Anonymous Contributor - 170098 views

Markoff Chaney - 84557 views

   --//--

Days with more than 1% requests leading to errors:
July 17, 2016 - 2.32% errors
```


## Details
Optionally i have implemented a basic function for [bleach](https://pypi.org/project/bleach/) library usage.

There is also functions for conducting spam queries, update and delete.

## License
MIT License

Copyright (c) [2018] [Nicholas Lobo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.