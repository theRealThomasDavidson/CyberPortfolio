# Security Audit

In this exercise from the Google Cybersecurity Professional Certificate program, I will conduct a mock security audit for a fictional company.

Information in *italics* will be questions or descriptions from the lab.

### Setting the Scene

*Botium Toys is a small U.S. business that develops and sells toys. The business has a single physical location, which serves as their main office, a storefront, and warehouse for their products. However, Botium Toy’s online presence has grown, attracting customers in the U.S. and abroad. As a result, their information technology (IT) department is under increasing pressure to support their online market worldwide.*

*The manager of the IT department has decided that an internal IT audit needs to be conducted. She expresses concerns about not having a solidified plan of action to ensure business continuity and compliance, as the business grows. She believes an internal audit can help better secure the company’s infrastructure and help them identify and mitigate potential risks, threats, or vulnerabilities to critical assets. The manager is also interested in ensuring that they comply with regulations related to internally processing and accepting online payments and conducting business in the European Union (E.U.).*

*The IT manager starts by implementing the National Institute of Standards and Technology Cybersecurity Framework (NIST CSF), establishing an audit scope and goals, listing assets currently managed by the IT department, and completing a risk assessment. The goal of the audit is to provide an overview of the risks and/or fines that the company might experience due to the current state of their security posture.*

### My Role

*Your task is to review the IT manager’s scope, goals, and risk assessment report. Then, perform an internal audit by completing a controls and compliance checklist.*

### Audit Outline

The scope, goals, and risk assessment Report are saved in this folder as AuditOutline.pdf.

#### Scope

*The scope is defined as the entire security program at Botium Toys. This means
all assets need to be assessed alongside internal processes and procedures related to
the implementation of controls and compliance best practices.*

#### Goals

*Assess existing assets and complete the controls and compliance checklist to
determine which controls and compliance best practices need to be implemented to
improve Botium Toys’ security posture.*

### Notes on Current Assets

Looks like a sales business. Seems to have the assets of wholesale (office and warehouse equipment) as well as retail (POS) and online retail. As well as internal processing of a good bit of their work. last note is there are unspecified legacy systems.

### Notes on Risk Assessment

We are the first people to do a security audit while this system has been in place, so a lot of recommendations may be needed. initial assessment of a Risk score of 8 from 1-10 is not ideal. We need to implement a least privilege model. **Credit card info has to be encrypted** we might be breaking the law here. IDS should be installed and there should be a plan of when it gets monitored. No recovery plan for data, we might want to do weekly long term storage of changes to a could provider, or as a physical disk to some local banks lock box, we might need to make storage RAID. Password policies are a bit out of date, let's make sure our employees passwords are updated soon and have a long term plan for customers. We need a sso or federated login system to make sure passwords are easily tracked. This could require long term planning. No specific guidelines for monitoring legacy systems. physical security is not bad, but we have CCTV but no offsite backup of information.



### Controls and Compliance Checklist

I am using a provided checklist for this activity found in this folder at ControlsComplianceCHecklist.pdf

#### Controls Assessment checklist

*for each control below I will assess if this control is currently in place.*

*Least Privilege*:    No

*Disaster recovery plans*: No

*Password policies*: Yes (not up to date)

*Separation of duties*: No

*Firewall*: Yes

*Intrusion detection system (IDS)*: No

*Backups*: No

*Antivirus software*: Yes

*Manual monitoring, maintenance, and intervention for legacy systems*: Yes (not structured enough)

*Encryption*: No (High Priority)

*Password management system*: Yes (inadequite)

*Locks (offices, storefront, warehouse)*: Yes

*Closed-circuit television (CCTV) surveillance*: Yes

*Fire detection/prevention (fire alarm, sprinkler system, etc.)*: Yes

#### Compliance Checklist

For each control below I will assess the company is in complience

##### Payment Card Industry Data Security Standard (PCI DSS):

*Only authorized users have access to customers’ credit card information*: No

*Credit card information is stored, accepted, processed, and transmitted internally, in a secure environment*: No

*Implement data encryption procedures to better secure credit card transaction touchpoints and data*: No

*Adopt secure password management policies*: No

##### General Data Protection Regulation (GDPR):

*E.U. customers’ data is kept private/secured*: No

*There is a plan in place to notify E.U. customers within 72 hours if their data is compromised/there is a breach*: Yes

*Ensure data is properly classified and inventoried*: No

*Enforce privacy policies, procedures, and processes to properly document and maintain data*: Yes


##### System and Organizations Controls (SOC type 1, SOC type 2):

*User access policies are established*: No

*Sensitive data (PII/SPII) is confidential/private*: No

*Data integrity ensures the data is consistent, complete, accurate, and has been validated*: Yes (until it is no longer available)

*Data is available to individuals authorized to access it*: No (needs to implement least privilege)