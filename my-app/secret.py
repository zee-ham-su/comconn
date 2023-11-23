import os
import binascii

# Generate a random byte string (24 bytes)
secret_key = binascii.hexlify(os.urandom(24)).decode('utf-8')

print("Generated Secret Key:", secret_key)