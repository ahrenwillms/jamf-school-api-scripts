#!/usr/bin/env python3

# Requires Python 3 and requests module to be installed

# Jamf School API documentation: https://school.jamfcloud.com/api/docs/

import sys
import requests
import json

network_id = "YOUR_NETWORK_ID"
api_key = "YOUR_API_KEY"
domain = "YOUR_DOMAIN"

# Store the script's first argument as a serial number variable
serial_number = sys.argv[1] if len(sys.argv) > 1 else "Invalid Serial Number"

# Look up device using the Jamf School API
query_url = f'https://{domain}.jamfcloud.com/api/devices/?serialnumber={serial_number}'
query_headers = {'Content-Type': 'application/json'}
query_result = requests.get(query_url, headers=query_headers, auth=(network_id, api_key))

# Store the response in JSON format
query_response = query_result.json()

# Store device UDID as a variable
device_udid=query_response["devices"][0]["UDID"]

# Send the restart command using the Jamf School API
device_command_url = f'https://{domain}.jamfcloud.com/api/devices/{device_udid}/restart'
device_command_headers = {'Content-Type': 'application/json'}
device_command_result = requests.post(device_command_url, headers=device_command_headers, auth=(network_id, api_key))

# Store the response in JSON format
device_command_reponse = device_command_result.json()

# Format the response as a string
formatted_device_command_response = json.dumps(device_command_reponse, indent=2)

# Print the response
print(formatted_device_command_response)