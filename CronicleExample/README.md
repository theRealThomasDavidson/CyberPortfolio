# Google Chronicle Example

In this exercise from the Google Cybersecurity Professional Certificate program, I will useChronicle to investigate a security incident. 

Information in *italics* will be questions or descriptions from the lab.

### Setting up Chronicle

I start by searching "signin.office365x24.com" and select that domain.

I am greeted with a dashboard.

I use legacy view. I see an item called "VT context (7/89)" that gives a virus total report on the domain.
While not many results are here we see the domain flagged in malware, malicious, and phishing.

ET intelligence rep list says it is the drop site for logs or stolen credentials.

I am able to find specific requests to the domain. and am able to identify 3 POST requests that possibly compromised usernames and passwords.

|Date: 1-26-2024| Entry: 00003|
|--|--|
|Description | A phishing email got some of our users to try to login on a 3rd party site so that they could collect their emails|
|Tool(s) Used| Google Chronicle|
|Who | users of the website |
|What | several users were emailed, they went to a malicious url, some entered login information |
|When| around 2pm 2/31/23|
|Where| over the wire |
|Why| phishing emails were seen as legit |
|Notes| review the standards for phishing training.|