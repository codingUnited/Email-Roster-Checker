# 📧 Email Roster Checker

This Python project processes and compares email lists to identify new members who are **not on an existing roster** and/or **need GitHub invitations**. It's useful for team onboarding, classroom organization, or any situation involving email-based group management.

## 📁 Project Structure

```
project/
├── input-files/
│   ├── roster_emails.txt
│   ├── new_member_emails.txt
│   └── github_emails.txt
├── output-files/
│   ├── not_on_roster.txt
│   └── need_existing_meetings_and_github_invites.txt
└── email_roster_checker.py
```

## 📥 Input Preparation

1. **Collect club member emails** from the official roster and add them to `roster_emails.txt` using the format:
   ```
   John Doe <john@example.com>; Jane Smith <jane@example.com>
   ```

2. **Collect GitHub invite emails** from the Engagement folder and add them to `github_emails.txt` as plain text.

3. **Collect new member email list** (e.g., from sign-up forms or interest surveys) and add them to `new_member_emails.txt`, one per line or space-separated.

All input files must be saved in the `input-files/` directory.

## 🧠 How It Works

1. Extracts emails from the roster (between `<` and `>`, converted to lowercase).
2. Cleans and normalizes new email addresses from the new members file.
3. Compares the two lists and identifies:
   - Emails not on the existing roster.
   - Emails missing from the GitHub access list.
4. Writes the output to two separate text files in `output-files/`.
5. Excludes `ardynleuzinger@snhu.edu` from all results.

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Place your input files inside the `input-files/` directory.
3. Run the Python script:

```bash
python email_roster_checker.py
```

4. Check the `output-files/` directory for the results.

## ✅ Sample Output

**Input – `new_member_emails.txt`:**
```
alice@example.com
bob@example.com
john@example.com
```

**Input – `roster_emails.txt`:**
```
John Smith <john@example.com>; Mary Jane <mary@example.com>
```

**Input – `github_emails.txt`:**
```
john@example.com
mary@example.com
```

**Output – `not_on_roster.txt`:**
```
alice@example.com
bob@example.com
```

**Output – `need_existing_meetings_and_github_invites.txt`:**
```
alice@example.com
bob@example.com
```

## ⚠️ Notes

- Assumes `< >` formatting for roster emails.
- GitHub file is treated as plain text with emails embedded or listed.
- Exclusion list is hardcoded but can be easily modified.

## 👨‍💻 Author

Created by Jose de Lima 
For internal use, onboarding, and collaboration facilitation.
