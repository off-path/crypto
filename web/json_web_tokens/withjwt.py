import jwt

jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9mZnBhdGgiLCJhZG1pbiI6ZmFsc2V9.EL_8J0mUIWTimZpGPzDoW8dqIxEbAfmJG2v3LhQGplc"

# Decode the JWT without verifying the signature
decoded_payload = jwt.decode(jwt_token, options={"verify_signature": False})

# Extract the flag from the decoded payload
flag_with_pyjwt = decoded_payload.get('flag', 'Flag not found')

print(flag_with_pyjwt)
