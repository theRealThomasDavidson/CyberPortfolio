# SQL Queries

In this exercise from the Google Cybersecurity Professional Certificate program, I will be using SQL to get relevant information while responding to a mock security event.

Information in *italics* will be questions or descriptions from the lab.

### Project description

#### Setting the Scene

*You are a security professional at a large organization. Part of your job is to investigate security issues to help keep the system secure. You recently discovered some potential security issues that involve login attempts and employee machines.*

*Your task is to examine the organization’s data in their 'employees' and 'log_in_attempts' tables. You’ll need to use SQL filters to retrieve records from different datasets and investigate the potential security issues.*

#### Tool specifications

In this exercise I will be using MariaDB ("Server version: 10.3.39-MariaDB-0+deb10u1 Debian 10").

The lay of the land is:

    > show tables;
    +------------------------+
    | Tables_in_organization |
    +------------------------+
    | employees              |
    | log_in_attempts        |
    | machines               |
    +------------------------+


    > describe employees;
    +-------------+-------------+------+-----+---------+-------+
    | Field       | Type        | Null | Key | Default | Extra |
    +-------------+-------------+------+-----+---------+-------+
    | employee_id | int(11)     | NO   | PRI | NULL    |       |
    | device_id   | varchar(16) | YES  |     | NULL    |       |
    | username    | varchar(16) | NO   |     | NULL    |       |
    | department  | varchar(32) | NO   |     | NULL    |       |
    | office      | varchar(32) | NO   |     | NULL    |       |
    +-------------+-------------+------+-----+---------+-------+


    > describe log_in_attempts;
    +------------+-------------+------+-----+---------+-------+
    | Field      | Type        | Null | Key | Default | Extra |
    +------------+-------------+------+-----+---------+-------+
    | event_id   | int(11)     | NO   | PRI | NULL    |       |
    | username   | varchar(16) | NO   |     | NULL    |       |
    | login_date | date        | NO   |     | NULL    |       |
    | login_time | time        | NO   |     | NULL    |       |
    | country    | varchar(16) | NO   |     | NULL    |       |
    | ip_address | varchar(16) | NO   |     | NULL    |       |
    | success    | tinyint(1)  | YES  |     | NULL    |       |
    +------------+-------------+------+-----+---------+-------+

The machines table is not expected to be queried in this lab, so I will not describe it above.


### Retrieve after hours failed login attempts

*You recently discovered a potential security incident that occurred after business hours. To investigate this, you need to query the log_in_attempts table and review after hours login activity. Use filters in SQL to create a query that identifies all failed login attempts that occurred after 18:00.*

Login activity is recorded in the 'log_in_attempts' table, and the times are in the 'login_time' column. I will assume that success is false for failed login attempts (in SQL false is the called 0). I'm going to limit this to 10 entries and do a count afterwards to give an example and a sense of scale.

    > select * from log_in_attempts where login_time > "16:00:00" and Success = 0 limit 10;
    +----------+----------+------------+------------+---------+----------------+---------+
    | event_id | username | login_date | login_time | country | ip_address     | success |
    +----------+----------+------------+------------+---------+----------------+---------+
    |        2 | apatel   | 2022-05-10 | 20:27:27   | CAN     | 192.168.205.12 |       0 |
    |        6 | arutley  | 2022-05-12 | 17:00:59   | MEXICO  | 192.168.3.24   |       0 |
    |       15 | lyamamot | 2022-05-09 | 17:17:26   | USA     | 192.168.183.51 |       0 |
    |       18 | pwashing | 2022-05-11 | 19:28:50   | US      | 192.168.66.142 |       0 |
    |       20 | tshah    | 2022-05-12 | 18:56:36   | MEXICO  | 192.168.109.50 |       0 |
    |       28 | aestrada | 2022-05-09 | 19:28:12   | MEXICO  | 192.168.27.57  |       0 |
    |       31 | acook    | 2022-05-12 | 17:36:45   | CANADA  | 192.168.58.232 |       0 |
    |       34 | drosas   | 2022-05-11 | 21:02:04   | US      | 192.168.45.93  |       0 |
    |       41 | apatel   | 2022-05-10 | 17:39:42   | CANADA  | 192.168.46.207 |       0 |
    |       42 | cgriffin | 2022-05-09 | 23:04:05   | US      | 192.168.4.157  |       0 |
    +----------+----------+------------+------------+---------+----------------+---------+

    > select count(*) from log_in_attempts where login_time > "16:00:00";
    +----------+
    | count(*) |
    +----------+
    |       30 |
    +----------+

    > select count(*) from log_in_attempts;
    +----------+
    | count(*) |
    +----------+
    |      200 |
    +----------+

### Retrieve login attempts on specific dates

*A suspicious event occurred on 2022-05-09. To investigate this event, you want to review all login attempts which occurred on this day and the day before. Use filters in SQL to create a query that identifies all login attempts that occurred on 2022-05-09 or 2022-05-08.*

So, the login_date field will tell me what date the event happened, and to make it easier on myself I will order these chronologically, to do this we order by date first them by time afterwards.


    > select * from log_in_attempts where login_date between "2022-5-08" and "2022-05-09" order by login_date, login_time limit 10;
    +----------+----------+------------+------------+---------+-----------------+---------+
    | event_id | username | login_date | login_time | country | ip_address      | success |
    +----------+----------+------------+------------+---------+-----------------+---------+
    |      117 | bsand    | 2022-05-08 | 00:19:11   | USA     | 192.168.197.187 |       0 |
    |       92 | pwashing | 2022-05-08 | 00:36:12   | US      | 192.168.247.219 |       0 |
    |        8 | bisles   | 2022-05-08 | 01:30:17   | US      | 192.168.119.173 |       0 |
    |        4 | dkot     | 2022-05-08 | 02:00:39   | USA     | 192.168.178.71  |       0 |
    |       80 | cjackson | 2022-05-08 | 02:18:10   | CANADA  | 192.168.33.140  |       1 |
    |       43 | mcouliba | 2022-05-08 | 02:35:34   | CANADA  | 192.168.16.208  |       0 |
    |      184 | alevitsk | 2022-05-08 | 03:09:48   | CAN     | 192.168.33.70   |       0 |
    |       56 | acook    | 2022-05-08 | 04:56:30   | CAN     | 192.168.209.130 |       1 |
    |       47 | dkot     | 2022-05-08 | 05:06:45   | US      | 192.168.233.24  |       1 |
    |      189 | nmason   | 2022-05-08 | 05:37:24   | CANADA  | 192.168.168.117 |       1 |
    +----------+----------+------------+------------+---------+-----------------+---------+

    > select count(*) from log_in_attempts where login_date between "2022-5-08" and "2022-05-09";
    +----------+
    | count(*) |
    +----------+
    |       75 |
    +----------+

### Retrieve login attempts outside of Mexico

*There’s been suspicious activity with login attempts, but the team has determined that this activity didn't originate in Mexico. Now, you need to investigate login attempts that occurred outside of Mexico. Use filters in SQL to create a query that identifies all login attempts that occurred outside of Mexico. (When referring to Mexico, the country column contains values of both MEX and MEXICO, and you need to use the LIKE keyword with % to make sure your query reflects this.)*

So it looks like we are filtering by country. and are assured that no other country starts with "MEX" in our database. Let's give it a bit of a test.

    > select * from log_in_attempts where country like "MEX%" limit 10;
    +----------+----------+------------+------------+---------+-----------------+---------+
    | event_id | username | login_date | login_time | country | ip_address      | success |
    +----------+----------+------------+------------+---------+-----------------+---------+
    |        6 | arutley  | 2022-05-12 | 17:00:59   | MEXICO  | 192.168.3.24    |       0 |
    |        9 | yappiah  | 2022-05-11 | 13:47:29   | MEX     | 192.168.59.136  |       1 |
    |       20 | tshah    | 2022-05-12 | 18:56:36   | MEXICO  | 192.168.109.50  |       0 |
    |       22 | rjensen  | 2022-05-11 | 00:59:26   | MEX     | 192.168.213.128 |       0 |
    |       23 | yappiah  | 2022-05-10 | 18:11:53   | MEXICO  | 192.168.200.48  |       1 |
    |       24 | arusso   | 2022-05-09 | 06:49:39   | MEXICO  | 192.168.171.192 |       1 |
    |       27 | aalonso  | 2022-05-10 | 01:55:35   | MEX     | 192.168.103.210 |       0 |
    |       28 | aestrada | 2022-05-09 | 19:28:12   | MEXICO  | 192.168.27.57   |       0 |
    |       30 | yappiah  | 2022-05-09 | 03:22:22   | MEX     | 192.168.124.48  |       1 |
    |       35 | tshah    | 2022-05-10 | 15:26:08   | MEX     | 192.168.92.147  |       0 |
    +----------+----------+------------+------------+---------+-----------------+---------+

Looks like our "MEX" filter works, lets do the oppisite of it. 

    > select * from log_in_attempts where country not like "MEX%" limit 10;
    +----------+----------+------------+------------+---------+-----------------+---------+
    | event_id | username | login_date | login_time | country | ip_address      | success |
    +----------+----------+------------+------------+---------+-----------------+---------+
    |        1 | jrafael  | 2022-05-09 | 04:56:27   | CAN     | 192.168.243.140 |       1 |
    |        2 | apatel   | 2022-05-10 | 20:27:27   | CAN     | 192.168.205.12  |       0 |
    |        3 | dkot     | 2022-05-09 | 06:47:41   | USA     | 192.168.151.162 |       1 |
    |        4 | dkot     | 2022-05-08 | 02:00:39   | USA     | 192.168.178.71  |       0 |
    |        5 | jrafael  | 2022-05-11 | 03:05:59   | CANADA  | 192.168.86.232  |       0 |
    |        7 | eraab    | 2022-05-11 | 01:45:14   | CAN     | 192.168.170.243 |       1 |
    |        8 | bisles   | 2022-05-08 | 01:30:17   | US      | 192.168.119.173 |       0 |
    |       10 | jrafael  | 2022-05-12 | 09:33:19   | CANADA  | 192.168.228.221 |       0 |
    |       11 | sgilmore | 2022-05-11 | 10:16:29   | CANADA  | 192.168.140.81  |       0 |
    |       12 | dkot     | 2022-05-08 | 09:11:34   | USA     | 192.168.100.158 |       1 |
    +----------+----------+------------+------------+---------+-----------------+---------+

    > select count(*) from log_in_attempts where country not like "MEX%";
    +----------+
    | count(*) |
    +----------+
    |      144 |

### Retrieve employees in Marketing

*Your team wants to perform security updates on specific employee machines in the Marketing department. You’re responsible for getting information on these employee machines and will need to query the employees table. Use filters in SQL to create a query that identifies all employees in the Marketing department for all offices in the East building.*

*(The department of the employee is found in the department column, which contains values that include Marketing. The office is found in the office column. Some examples of values in this column are East-170, East-320, and North-434. You’ll need to use the LIKE keyword with % to filter for the East building.)*

We are using the 'employees' table. (We described this table near the start of the document in Tool specifications).
Further along with the like check above we are using a logical and that make sure that the returned results fit all of the described criteria.

    > select * from employees where office like "EAST-%" and department = "Marketing";
    +-------------+--------------+----------+------------+----------+
    | employee_id | device_id    | username | department | office   |
    +-------------+--------------+----------+------------+----------+
    |        1000 | a320b137c219 | elarson  | Marketing  | East-170 |
    |        1052 | a192b174c940 | jdarosa  | Marketing  | East-195 |
    |        1075 | x573y883z772 | fbautist | Marketing  | East-267 |
    |        1088 | k865l965m233 | rgosh    | Marketing  | East-157 |
    |        1103 | NULL         | randerss | Marketing  | East-460 |
    |        1156 | a184b775c707 | dellery  | Marketing  | East-417 |
    |        1163 | h679i515j339 | cwilliam | Marketing  | East-216 |
    +-------------+--------------+----------+------------+----------+
    7 rows in set



### Retrieve employees in Finance or Sales

*Your team now needs to perform a different security update on machines for employees in the Sales and Finance departments. Use filters in SQL to create a query that identifies all employees in the Sales or Finance departments. (The department of the employee is found in the department column, which contains values that include Sales and Finance.)*

FOr this we use an or statement to get all employees who fit at least one of the criteria of in "Finance" or in "Sales".

    > select * from employees where department = "Finance" or department = "Sales" limit 10;
    +-------------+--------------+----------+------------+-----------+
    | employee_id | device_id    | username | department | office    |
    +-------------+--------------+----------+------------+-----------+
    |        1003 | d394e816f943 | sgilmore | Finance    | South-153 |
    |        1007 | h174i497j413 | wjaffrey | Finance    | North-406 |
    |        1008 | i858j583k571 | abernard | Finance    | South-170 |
    |        1009 | NULL         | lrodriqu | Sales      | South-134 |
    |        1010 | k242l212m542 | jlansky  | Finance    | South-109 |
    |        1011 | l748m120n401 | drosas   | Sales      | South-292 |
    |        1015 | p611q262r945 | jsoto    | Finance    | North-271 |
    |        1017 | r550s824t230 | jclark   | Finance    | North-188 |
    |        1018 | s310t540u653 | abellmas | Finance    | North-403 |
    |        1022 | w237x430y567 | arusso   | Finance    | West-465  |
    +-------------+--------------+----------+------------+-----------+

    >  select count(*) from employees where department = "Finance" or department = "sales";
    +----------+
    | count(*) |
    +----------+
    |       71 |
    +----------+
### Retrieve all employees not in IT

*Your team needs to make one more update to employee machines. The employees who are in the Information Technology department already had this update, but employees in all other departments need it. Use filters in SQL to create a query which identifies all employees not in the IT department. (The department of the employee is found in the department column, which contains values that include Information Technology.)*

This is pretty easily we describe employees in IT then we use the not operator to get everything that doesn't fit that description.

First attempt fails as we find employees in departments with the name "Information Technology". And we try again. 

    > select * from employees where not department = "Information Technology" limit 10;
    +-------------+--------------+----------+-----------------+-------------+
    | employee_id | device_id    | username | department      | office      |
    +-------------+--------------+----------+-----------------+-------------+
    |        1000 | a320b137c219 | elarson  | Marketing       | East-170    |
    |        1001 | b239c825d303 | bmoreno  | Marketing       | Central-276 |
    |        1002 | c116d593e558 | tshah    | Human Resources | North-434   |
    |        1003 | d394e816f943 | sgilmore | Finance         | South-153   |
    |        1004 | e218f877g788 | eraab    | Human Resources | South-127   |
    |        1005 | f551g340h864 | gesparza | Human Resources | South-366   |
    |        1007 | h174i497j413 | wjaffrey | Finance         | North-406   |
    |        1008 | i858j583k571 | abernard | Finance         | South-170   |
    |        1009 | NULL         | lrodriqu | Sales           | South-134   |
    |        1010 | k242l212m542 | jlansky  | Finance         | South-109   |
    +-------------+--------------+----------+-----------------+-------------+

    > select count(*) from employees where not department = "Information Technology";
    +----------+
    | count(*) |
    +----------+
    |      161 |
    +----------+


### Summary

Overall, I fell like I have a good handle on logical Operators as well as querying single tables in MariaDB. My previous experience with MySQL 8.0 seems to have covered most of what we did here, but I am aware that MariaDB has some other functions that may make my life easier but were not needed today. 