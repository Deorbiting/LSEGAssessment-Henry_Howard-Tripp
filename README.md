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

Error Handling
1. Will hnadle invalida keys and connection timeouts/failures


Demonstration:
