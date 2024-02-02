# Incident handler's journal

In this exercise from the Google Cybersecurity Professional Certificate program, I will document an incident with an incident handler's journal.

Information in *italics* will be questions or descriptions from the lab.

### Setting the Scene

*A small U.S. health care clinic specializing in delivering primary-care services experienced a security incident on a Tuesday morning, at approximately 9:00 a.m. Several employees reported that they were unable to use their computers to access files like medical records. Business operations shut down because employees were unable to access the files and software needed to do their job.*

*Additionally, employees also reported that a ransom note was displayed on their computers. The ransom note stated that all the company's files were encrypted by an organized group of unethical hackers who are known to target organizations in healthcare and transportation industries. In exchange for restoring access to the encrypted files, the ransom note demanded a large sum of money in exchange for the decryption key.*

*The attackers were able to gain access into the company's network by using targeted phishing emails, which were sent to several employees of the company. The phishing emails contained a malicious attachment that installed malware on the employee's computer once it was downloaded.*

*Once the attackers gained access, they deployed their ransomware, which encrypted critical files. The company was unable to access critical patient data, causing major disruptions in their business operations. The company was forced to shut down their computer systems and contact several organizations to report the incident and receive technical assistance.*

### Anatomy of a Journal Entry

|Date: {Date} | Entry: {Entry ID}|
|--|--|
|Description | {brief description of event}|
|Tool(s) Used| {list of tools that were used to **respond** to the incident}|
|Who | {caused the incident} |
|What | {happened during the incident}|
|When| {did the incident take place}|
|Where| {did the incident happen}|
|Why| {did the incident happen}|
|Notes| {any relevant information that is not covered by the other rows}|

### This incident

|Date: 1/25/2024 | Entry: 00001|
|--|--|
|Description | Ransomware attack following phishing success|
|Tool(s) Used| None |
|Who | Incident caused by a cyber crime gang in search of a payout.  |
|What | Phishing emails were sent, malicious attachments were opened, the attachements allowed for access to critical systems that were subject to encryption. |
|When| Tuesday morning, at approximately 9:00 a.m |
|Where| On site, over emails|
|Why| The attackers were in search of a payout, phishing training was inadequate at this stage to prevent at least one employee from opening a malicious attachment. |
|Notes| We should assess if PHI was exfiltrated for additional ransom once the systems have been restored. Training for phishing needs to be reevaluated. |

### Other incidents

|Date: 1-26-2024| Entry: 00002|
|--|--|
|Description | suspicious file downloaded to employee computer after phishing |
|Tool(s) Used| Virus total|
|Who | employee, targeted hacker |
|What | user was emailed, they opened a malicious attachment and ran it |
|When| unspecified in the example|
|Where| over the wire |
|Why| phishing emails were seen as legit |
|Notes| review the standards for phishing training. consult if you can turn off macros in microsoft windows to prevent this from happening again.|
|Notes| In this example I worked on the Identification aspect of incident response, and determined if a file was suspicious. |


below incident can be found at ../SplunkExample/

|Date: 1-26-24 | Entry: 00003|
|--|--|
|Description | botnet trying to brute force login for mail server|
|Tool(s) Used| Splunk cloud |
|Who | a botnet unclear source |
|What | a large number of login attempts happened over many days at a particular time of day |
|When| 3/3/23 - 3/6/23 at 1:39:51 every day |
|Where| mailsv server|
|Why| email has to be open to the internet, |
|Notes| we may need to whitelist ip addresses for sshing into the mail server. or just drop incoming calls to port 22 to the mail server. |
|Notes| In this example I worked on the Identification phase of incident response, and reviewed logs to find anomalies that could be Indicators of Compromise. |

below incident can be found at ../ChronicleExample/

|Date: 1-26-2024| Entry: 00004|
|--|--|
|Description | A phishing email got some of our users to try to login on a 3rd party site so that they could collect their emails|
|Tool(s) Used| Google Chronicle|
|Who | users of the website |
|What | several users were emailed, they went to a malicious url, some entered login information |
|When| around 2pm 2/31/23|
|Where| over the wire |
|Why| phishing emails were seen as legit |
|Notes| review the standards for phishing training.|
|Notes| In this example I worked on the Identification of incident response, and reviewed logs to find which computers of ours ended up interacting with a phishing website. |

### Reflection

This whole thing was a lot of fun, frankly it would have been a bit more fun if I didn't spend so much time screenshotting things in the splunk example, but that is the price you pay for using a GUI. Further it was kind of cool getting the tutorial wrong for the Splunk example because I got to figure out what was going on, how to fix it, and determine if the fix worked on my own. I certainly don't downplay the value of having a good guide, but it is nice to figure stuff out, that is kind of why I'm choosing to take this course.