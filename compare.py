import re


# Function to extract the indices of the first '<' and '>' characters in a string
def get_index(a_text):
    return a_text.index('<'), a_text.index('>')


# Open the roster file and extract emails that are enclosed in '<>' brackets
with open("input-files/roster_emails.txt") as roster:
    roster_list = [
        re.search(r'<(.*?)>', entry).group(1).strip().lower()
        for entry in roster.read().split(';')
        if '<' in entry and '>' in entry
    ]


# Open the file containing new member emails
with open("input-files/new_member_emails.txt") as recruits:
    # Split the content by whitespace, strip surrounding whitespace,
    # keep only strings that contain '@', and convert them to lowercase
    recruit_list = [email.strip().lower()
                    for email in recruits.read().split()
                    if '@' in email]


# Identify emails in recruit_list that are not already on the roster
new_list = list(set(recruit_list) - set(roster_list))

# removed from roster
with open("input-files/roster-removal", mode='r') as rr:
    quit_club = [email.strip().lower() for email in rr.read().split()]

# Write emails not on the roster to an output file, excluding specific emails
with (open("output-files/not_on_roster.txt", mode='w') as new_file):
    for email in new_list:
        if email not in quit_club and 'snhu' in email:
            new_file.write(email + '\n')

# Open the file containing GitHub user emails
with open("input-files/github_emails") as github:
    github_content = github.read().lower()  # Read and normalize the content to lowercase
    # Identify emails from new_list that are not found in the GitHub content
    need_invite = [email for email in new_list if email.lower() not in github_content and 'snhu' in email]

# Write emails needing GitHub invites to a separate file, excluding specific emails
with (open("output-files/need_existing_meetings_and_github_invites.txt", mode='w') as need_invite_file):
    for email in need_invite:
        need_invite_file.write(email + '\n')


with open("input-files/fail-github-invite") as no_github:
    fail_github = [email.strip().lower() for email in no_github if '@' in email]


with open("output-files/send-roster-removal-notice", 'w') as removal_notice:
    for email in fail_github:
        if email not in ['a.claerhout@snhu.edu', 'j.daigle@snhu.edu'] and email not in quit_club:
            removal_notice.write(email + '\n')
