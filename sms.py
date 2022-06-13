from twilio.rest import Client

account_sid = 'AC854a78ec983f8ba21a3984656e8cf58b'
auth_token = '2eda7278f876e8c4bb1a5e78a6b40d43'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG59aa45087af06ead96e4d25b4ebce630',
    body='MID- TERM TEST ',
    to='+2347055626519'
)

print(message.sid)