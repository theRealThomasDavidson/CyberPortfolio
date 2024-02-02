# Update A file with python

In this exercise from the Google Cybersecurity Professional Certificate program, I will write a python algorithm to update a file called allow_lists.txt to update a current allow list.

Information in *italics* will be questions or descriptions from the lab.

### Setting the Scene

*You are a security professional working at a health care company. As part of your job, you're required to regularly update a file that identifies the employees who can access restricted content. The contents of the file are based on who is working with personal patient records. Employees are restricted access based on their IP address. There is an allow list for IP addresses permitted to sign into the restricted subnetwork. There's also a remove list that identifies which employees you must remove from this allow list.*

*Your task is to create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. If so, you should remove those IP addresses from the file containing the allow list.*

### Overview of instructions

- read file contents
- convert string to list
- iterate through the remove list
- remove IP addresses on the remove list
- update the file with the new list

I think I'm going to set these up in various functions with the flow described in main().
Some supporting functions will be made as well so that this is useful. 
this will be written in ./file_update.py

### What I wrote


get_allowed_ips(file_name:str=FILE_NAME)->gen->str

    generator that will show each of the ips currently in the allow list one at a time. 
    This has a default value for the file_name of the allow list, but can be changed if needed.

is_in_file(addr:str, file_name:str=FILE_NAME) -> bool:

    this tells you if a particular address is in the allowed list
    it return True if the address is in the file otherwise it returns false

remove_ips(remove_list:list|set|tuple, file_name:str=FILE_NAME) -> None:

    This removes any entries that are in the current list that are also in the remove list.
    It handles items not in the current list by simply not adding them to the list.
    This has a default value for the file_name of the allow list, but can be changed if needed.
    No return is needed since it modifies the file and no additional information is needed. 


add_ips(add_list:list|set|tuple, file_name:str=FILE_NAME) -> None:


    This adds any entries that are not in the current list that are in the add list.
    It handles items in the current list by simply not adding them to the list a second time.
    This has a default value for the file_name of the allow list, but can be changed if needed.
    No return is needed since it modifies the file and no additional information is needed.

### Conclusion

Running the remove ips is basically all that is needed to finish the lab, but all of these functions are useful for the described scenario, so you might as well get them all write