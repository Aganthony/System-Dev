import subprocess

# run a command in the terminal
# Is -I means list files and folders with details
# Is -I uses lowercase L, not 1 (one)
subprocess.run(["ls", "-1"])

# run some git commands.
# The arguments are enterd as seperate items in the list
subprocess.run(["git", "--version"])
subprocess.run(["git", "status"])
