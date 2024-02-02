# Analyze a System

In this exercise from the Google Cybersecurity Professional Certificate program, I will conduct a vulnerability assessment of a mock system.

Information in *italics* will be questions or descriptions from the lab.

### Setting the Scene

*You are a newly hired cybersecurity analyst for an e-commerce company. The company stores information on a remote database server, since many of the employees work remotely from locations all around the world. Employees of the company regularly query, or request, data from the server to find potential customers. The database has been open to the public since the company's launch three years ago. As a cybersecurity professional, you recognize that keeping the database server open to the public is a serious vulnerability.*

*A vulnerability assessment of the situation can help you communicate the potential risks with decision makers at the company. You must create a written report that clearly explains how the vulnerable server is a risk to business operations and how it can be secured.*

#### System Description
*The server hardware consists of a powerful CPU processor and 128GB of memory. It runs on the latest version of Linux operating system and hosts a MySQL database management system. It is configured with a stable network connection using IPv4 addresses and interacts with other servers on the network. Security measures include SSL/TLS encrypted connections.*

### Risk Assessment

#### Purpose

This risk assessment is to ensure confidentiality, integrity, and availability for this database system. The database is important for keeping customer information in an accessible place and avoiding siloing information, it is also useful for continued service when a particular employee is not available. This data is a trade secret as the employees spent their work hours collecting it and maintaining the information. This information could be valuable to our customers or competitors.
If the server goes down it can impact the ability for our employees to do their jobs and can lead to a significant loss of productivity.

#### Potential Sources of threats.

This table I'm going to fill out accoriding to NIST SP-800-30 Rev. 1.

|Threat Source| Threat event | Likelihood| Severity| Risk|
|--|--|--|--|--|
|Competitor| Obtain Customer information and use it for their business| 3 | 2 | 6|
|Hacker| Steal customer information to use for identity theft or fraud| 3 | 3 | 9|
|Hacker| Install ransomware ont he system and charge us for access | 2 | 3 | 6 |
|Customer| change or delete info on another customer their competitor for advantage |1|3|3|
|Employee| might leave access to the server open on a public or non secured terminal |3|1|3|
|Operating system| could be compromised and be used as a single source for a watering hole attack or botnet |2|3|6|
|Outsider| could start using the unsecured database as a repository for other info exhausting system resources | 1|2|2|

### Propose a Solution

I guess I'm a simple man who likes to emulate things I see elsewhere, this database should be behind a firewall with an api that is able to govern access to the database. This api should use multi factor authentication or SSO with another part of our system that uses multi factor authentication. The api should also use authorization to define roles for accessing parts of the database according to need. The firewall should allow only port 443 to the api server to accept traffic. The database should also implement a software based firewall policy to only accept requests from the api server's ip address.

At the end of this process employees should still be able to access the information they need to do their jobs but access to other information will be limited. Outside groups will no longer be able to access the database at all limiting the likelihood of information leaking.