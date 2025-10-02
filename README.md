# user-add

A simple script to automate user creation / user management in Linux environments.  

## Overview

The `user-add` tool is designed to streamline adding new users to a Linux system. It encapsulates typical tasks such as:

- creating a user account  
- setting up default permissions or groups
- handling password  

It aims to reduce manual repetition and avoid mistakes when onboarding new users on servers or in development environments.

## Prerequisites

- A Linux (or Unix-like) system  
- Python
- Root privileges (or `sudo`) to manage users  
- Bash  
- Standard Linux tools: `useradd`, `passwd`, etc.  

## Usage

Clone this repository:
```bash
git clone https://github.com/jonikola/user-add.git
cd user-add
```

Make the script executable:
```bash
chmod +x user-add.py
```

You can also optionally install it into your system path (e.g. /usr/local/bin) for convenience:
```bash
sudo cp user-add.py /usr/local/bin/user-add
```

Create text file with usernames and groups that are assigned to them in format `username:group1, group2, etc.`

Run the script with:
```bash
./user-add.py path_to_text_file
```
or
```bash
python user-add.py path_to_text_file
```