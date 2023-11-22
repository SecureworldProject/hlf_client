import requests
import json
import os
import glob
from dotenv import load_dotenv

load_dotenv()


# Define the folder path

folder_path = os.getenv('SECUREMIRROR_BLOCKCHAIN_TRACE_FOLDER')


# Define the pattern to match the file names
file_pattern = "blockchainTask*"

# Get a list of files that match the pattern
file_list = glob.glob(os.path.join(folder_path, file_pattern))

# Iterate through the file list
for file_path in file_list:
    try:
        # Read the file contents
        with open(file_path, 'r') as file:
            print("File opened")
            file_contents = file.read()
            payload = json.loads(file_contents)
            file.close()
            
            url = os.getenv('URL')

            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer "+os.getenv('TOKEN')
            }
                        
            response = requests.request("POST", url, json=payload, headers=headers)

            print(response.text)
            
        # Delete the file
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")

    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

