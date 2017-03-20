from twilio.rest import TwilioRestClient

account_sid = "AC383235e5ab0c11f6cd6a26637c2aa5a1" # Your Account SID from www.twilio.com/console
auth_token  = "95faabae29dcd6527f594e3f31584939"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+14156761595",    # Replace with your phone number
    from_="+14156826577") # Replace with your Twilio number

print(message.sid)
