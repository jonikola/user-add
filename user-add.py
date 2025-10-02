#!/usr/bin/python
import subprocess
import sys

def add_user(username):
    check = subprocess.run(['id', username], capture_output=True)
    if check.returncode != 0:
        print(f"Adding user '{username}'.")
        subprocess.run(['sudo', 'useradd', username], capture_output=True)
        subprocess.run(['sudo', 'passwd', '-d', username], capture_output=True)
        subprocess.run(['sudo', 'passwd', '-e', username], capture_output=True)
    else:
        print(f"User '{username}' already exists. Skipping it.")

def add_group(group):
    check = subprocess.run(['grep', group, '/etc/group'], capture_output=True)
    if check.returncode != 0:
        print(f"Adding group '{group}'.")
        subprocess.run(['sudo', 'groupadd', group], capture_output=True)

def add_user_group(username, groups):
    group = groups.strip().split(',')
    for g in group:
        add_group(g)
    print(f"Adding user '{username}' to groups '{groups}'")
    subprocess.run(['sudo', 'usermod', '-aG', groups.replace(' ', ''), username], capture_output=True)

if len(sys.argv) > 1:
    file = sys.argv[1]

    try:
        with open(file, 'r') as f:
            for line in f:
                data = line.strip().split(':')
                add_user(data[0])
                if len(data) > 1:
                    add_user_group(data[0], data[1])
    except FileNotFoundError:
        print(f"Error: The file {file} was not found.")
else:
    print("No file specified.")