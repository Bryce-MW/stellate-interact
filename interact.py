#! /usr/bin/env python3

from stellate_auth import password
import psutil
import psycopg2

print("Hello!")
print("Welcome to Stellate!")

con = psycopg2.connect(database="stellate", user="bryce", host="10.29.33.3", password=password)
con.set_session(autocommit=True)
cur = con.cursor()

# SSH_ORIGINAL_COMMAND

# SSH_CMD = os.getenv("SSH_ORIGINAL_COMMAND")

# if SSH_CMD:
#   print("Automated connections are not implemented quite yet")
#   exit(0)

print("\n Here are the hosts that you already have set up:")

cur.execute("""
SELECT type, username, hostname, port FROM hosts INNER JOIN passwd_table ON "user"=uid WHERE username=%s;
""", (psutil.Process().username(),))

for i,line in enumerate(cur):
  print(f" {i}. {line[0]} {line[1]}@{line[2]}:{line[3]}`")

print("\nEnter the connection that you would like to use or \"configure\" to create a new one")
query = input("-> ")

if query.lower() == "configure":
  print("Configuring has not been added yet")
  exit(0)

print("Using a connection has not been added yet")

con.close()
exit(0)
