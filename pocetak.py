import re

# Read file content
with open("email1.txt", mode="r") as f:
    text = f.read()

# Extract emails using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

# Save extracted emails to new file
with open("email2.txt", mode="w") as f:
    for email in emails:
        f.write(email + "\n")

print(emails)