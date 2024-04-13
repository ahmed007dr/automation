#pip install 
#pip install twilio
#doc https://pypi.org/project/twilio/
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "AC618871f54605c0955f4349d55e205854aaa"
auth_token  = "b2d1c4007164be13bcbf2c925a1a8d5baaa"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+201114774986",
    from_="+1 316 313 4979",
    body="Hello from Python!")

print(message.sid)
print("sent Perfect")