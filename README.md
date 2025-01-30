Challenge #1: Metadata retrieval from AWS EC2

The Task:

To write a script that will retrieve metadata from a AWS EC2 Instanceand output it in JSON format. BONUS: The script should allow retrieval of specific metadata key individually.

Features:
IMDSv2 Token Retrieval -
1. Utilised a PUT request, fetching a session token with a TTL (Time to Live) of 6 hours
2. Ensures Secure access to metadata

Metadata Retrieval -
1. Will fetch metadata from the EC2 instance using the token
2. Will return all metadata or individual if key is specified 

Performance Optimisation - 
1. By reusing the HTTP session for multiple requests, the efficency is improved by reducing the amount of API calls

Error Handling - 
1. Will handle invalid keys and connection timeouts/failures

JSON Format - 
1. Returns retrieved metadata in JSON format



**Bonus** 
1. Individual data key retrieval - The script will take a individual data key as an argument and retrieve the metadata.
2. Performance Optimisation - Reused the HTTP session to improve efficiency when fetching the metadata.

**Hints Used:**
AWS Documentation

****Demonstration:****


**SSH Connection** 
SSH into the EC2 Instance:

![alt text](https://github.com/Deorbiting/LSEGAssessment/blob/main/SSH%20Connection.png)

**Retrieve All Metadata**
Run the script with no arguments returns all metadata in JSON format:

![alt text](https://github.com/Deorbiting/LSEGAssessment/blob/main/Succesful%20Full%20Retrieval.png)

***Bonus***

Run the script with a specified datakey Example: "instance-id" in JSON format:

![alt text](https://github.com/Deorbiting/LSEGAssessment/blob/main/Successful%20Key%20Retrieval.png)

**Invalid Data Key**

When a user inputs an invalid data key to be retrieved Example: "instance":

![alt text](https://github.com/Deorbiting/LSEGAssessment/blob/main/Failed%20Key.png)
