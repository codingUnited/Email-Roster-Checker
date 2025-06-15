# Function to extract the indices of the first '<' and '>' characters in a string
def get_index(a_text):
    return a_text.index('<'), a_text.index('>')

# Open the roster file and extract emails that are enclosed in '<>' brackets
with open("input-files/roster_emails.txt") as roster:
    # For each email, extract the part between '<' and '>', convert to lowercase, and build a list
    roster_list = [email[get_index(email)[0] + 1: get_index(email)[1]].lower()
                   for email in roster.read().split(';')]

# Open the file containing new member emails
with open("input-files/new_member_emails.txt") as recruits:
    # Split the content by whitespace, strip surrounding whitespace,
    # keep only strings that contain '@', and convert them to lowercase
    recruit_list = [email.strip().lower()
                    for email in recruits.read().split()
                    if '@' in email]

# Identify emails in recruit_list that are not already on the roster
new_list = list(set(recruit_list) - set(roster_list))

# Write emails not on the roster to an output file, excluding specific emails
with open("output-files/not_on_roster.txt", mode='w') as new_file:
    for email in new_list:
        if email not in ["ardynleuzinger@snhu.edu"]:
            new_file.write(email + '\n')

# Open the file containing GitHub user emails
with open("input-files/github_emails") as github:
    github_content = github.read().lower()  # Read and normalize the content to lowercase
    # Identify emails from new_list that are not found in the GitHub content
    need_invite = [email for email in new_list if email.lower() not in github_content]

# Write emails needing GitHub invites to a separate file, excluding specific emails
with open("output-files/need_existing_meetings_and_github_invites.txt", mode='w') as need_invite_file:
    for email in need_invite:
        if email not in ["ardynleuzinger@snhu.edu"]:
            need_invite_file.write(email + '\n')