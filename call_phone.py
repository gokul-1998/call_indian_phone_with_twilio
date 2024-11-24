from twilio.rest import Client
from env import account_sid, auth_token, to, from_
# Twilio credentials
account_sid = account_sid
auth_token = auth_token

client = Client(account_sid, auth_token)

call = client.calls.create(
    to=to,  # Your Indian phone number
    from_=from_,  # Your Twilio phone number
    url='http://demo.twilio.com/docs/voice.xml'  # URL with TwiML instructions
)

print(f"Call SID: {call.sid}")
