import base64
import json

# JWT provided
jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9mZnBhdGgiLCJhZG1pbiI6ZmFsc2V9.EL_8J0mUIWTimZpGPzDoW8dqIxEbAfmJG2v3LhQGplc"

# Split the JWT into its three components
header_encoded, payload_encoded, signature_encoded = jwt_token.split('.')

# Convert base64-url to base64
def base64_url_decode(input):
    input += '=' * (4 - (len(input) % 4))  # Pad with '=' to make the length a multiple of 4
    return base64.urlsafe_b64decode(input)

# Decode the payload
payload_decoded = base64_url_decode(payload_encoded)

# Convert the decoded payload to JSON
payload_json = json.loads(payload_decoded)

# Extract the flag
flag = payload_json.get('flag', 'Flag not found')

print(flag)
