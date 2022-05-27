friend_emails = {
    "Anne": "anne@example.com",
    "Brent": "brent@example.com",
    "Dan": "dan@example.com",
    "David": "david@example.com",
    "Fox": "fox@example.com",
    "Jane": "jane@example.com",
    "Kevin": "kevin@example.com",
    "Robert": "robert@example.com"
}


def lookup_email(name):
    try:
        return friend_emails[name]
    except KeyError as e:
        print(f"<No entry for friend {e}>")


name = input("Enter name to look up: ")
email = lookup_email(name)
print(f"Email: {email}")
