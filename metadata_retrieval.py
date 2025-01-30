import requests
import json
import sys

METADATA_URL = "http://169.254.169.254/latest/meta-data/"
TOKEN_URL = "http://169.254.169.254/latest/api/token"


 # Function that will retrieve the IMDSv2 token
 # If token is succesfully retrieved, it returns the token
def get_token():
    try:
        response = requests.put(
            TOKEN_URL,
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=1
        )
        response.raise_for_status()
        token = response.text
        return token
    except requests.exceptions.RequestException as e:
        print(f"Could not retrieve IMDSv2 Token: {e}")
        return None
#Will retrieve the EC2 instance metadata using the retrieved token
# If a data key is used as am argument, only that key is returned
def get_metadata(token, key=None):
    try:
        response = requests.get(
            METADATA_URL, headers={"x-aws-ec2-metadata-token": token},
            timeout=1
        )
        response.raise_for_status()
        #Splits the retrieved metadata into seperate items
        metadata = response.text.splitlines()

        #Define dictionary to store metadata
        metadata_dict = {}
        #Starts session
        with requests.Session() as session:
            #Adds the specified token to the header
            session.headers.update({"x-aws-ec2-metadata-token": token})
            for item in metadata:
                item_response =session.get(f"{METADATA_URL}{item}", timeout=1)# Connection reused
                item_response.raise_for_status()
                metadata_dict[item] = item_response.text

                #Improved version reuses the connection for multiple requests, improving performance

        #If a particular data key is specified for retrieval, only requested key is returned
        if key:
            if key in metadata_dict:
                return json.dumps({key: metadata_dict[key]}, indent=1)
            print(f"{key} Was not found,available keys: {', '.join(sorted(metadata_dict.keys()))}")
            return None
        #Returns all metadata as a JSON string
        return json.dumps(metadata_dict, indent=1)

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving metadata: {e}")
        return None

if __name__ == "__main__":
    #Retrieves the token
    token = get_token()
    if not token:
        print("Failed to retrieve token.")
        sys.exit(1)
    #Gets specific metadata if datakey provided 
    key = sys.argv[1] if len(sys.argv) > 1 else None
    #print the metadata
    result = get_metadata(token, key)
    if result:
        print(result)
    else:
        print("No metadata retrieved.")
