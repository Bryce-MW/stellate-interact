#! /usr/bin/env python3

from stellate_auth import password
import os
import psycopg2
import getpass

print("Hello!")
print("Welcome to Stellate!")

con = psycopg2.connect(database="stellate", user="bryce", host="10.29.33.3", password=password)
cur = con.cursor()

# SSH_ORIGINAL_COMMAND

SSH_CMD = os.getenv("SSH_ORIGINAL_COMMAND")

if SSH_CMD:
  print("Automated connections are not implemented quite yet")
  exit(0)

print("\n Here are the hosts that you already have set up:")

cur.execute("""
SELECT type, username, hostname, port FROM hosts INNER JOIN passwd_table ON "user"=uid WHERE username=%s
""", (getpass.getuser(),))

for i,line in enumerate(cur):
  print(f" {i}. {line[0]} {line[1]}@{line[2]}:{line[3]}`")
