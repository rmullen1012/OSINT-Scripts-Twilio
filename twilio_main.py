# Python Code:

import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables.
# Export SID and Key as Environment Variable using below commands on Linux:
# echo "export TWILIO_ACCOUNT_SID='ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'" > twilio.env
# echo "export TWILIO_AUTH_TOKEN='your_auth_token'" >> twilio.env
# source ./twilio.env

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

phone_number = client.lookups \
                     .v1 \
                     .phone_numbers('+16316906401') \
                     .fetch(country_code='US', type=['carrier']) \
                     .fetch(type=['caller-name'])\
                     .fetch(add_ons=['dataaxle_bizinfo', 'ekata_reverse_phone', 'ekata_phone_valid', 'twilio_carrier_info', 'twilio_caller_name', 'icehook_scout', 'digitalsegment_businessinfo', 'telo_opencnam', 'truecnam_truespam']) \

print(phone_number.add_ons)

