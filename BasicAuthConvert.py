import base64
import sys

def convert_to_basic_auth(username, password):
    credentials = f"{username}:{password}"
    encoded_credentials = credentials.encode('utf-8')
    basic_auth = base64.b64encode(encoded_credentials).decode('utf-8')
    return basic_auth

if len(sys.argv) != 4:
    print("Usage: python script.py <usernames_file> <passwords_file> <output_file>")
    sys.exit(1)

usernames_file = sys.argv[1]
passwords_file = sys.argv[2]
output_file = sys.argv[3]

with open(usernames_file, "r") as user_f, open(passwords_file, "r") as pass_f, open(output_file, "w") as out_f:
    usernames = [username.strip() for username in user_f]
    passwords = [password.strip() for password in pass_f]

    for username in usernames:
        for password in passwords:
            basic_auth = convert_to_basic_auth(username, password)
            out_f.write(f"{basic_auth}\n")

print("Basic authentication syntax generated and saved to", output_file)
