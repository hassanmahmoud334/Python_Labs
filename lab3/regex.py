import re
from decorators import log_time

@log_time
def run_task():
    log_lines = [
        "user1@example.com",
        "invalid_email@@",
        "hello@domain.com",
        "justtext",
        "admin@mail.org",
        "fake@@domain..com",
        "test.user@gmail.com",
        "nonsense line",
        "contact@company.com",
        "user1@example.eg"
    ]

    with open("access.log", "w") as f:
        f.write("\n".join(log_lines))
    
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}"

    with open("access.log", "r") as f:
        content = f.read()

    emails = re.findall(email_pattern, content)
    unique_emails = set(emails)

    with open("valid_emails.txt", "w") as f:
        f.write("\n".join(unique_emails))

    print(f"Found {len(unique_emails)} unique valid emails.")
    print("Saved into valid_emails.txt")
