import re
from typing import overload
from fabric import Connection, Config
import getpass

password = getpass.getpass("Enter your root password: ")

config = Config(overrides= {'sudo': {'password': password}})
conn =  Connection("", user = "username", config=config)

result = conn.run("ls -la", hide = True) #can store the output in a variable

print(result.stdout) #stdout can show output in the terminal
conn.run("pwd") 
#we cannot change directories using run func
# we use cd function to change directories

with conn.cd("/usr/local/etc"):
    conn.run("touch myfile.txt") #run touch command

#sudo has its own func and cannot run through run func
conn.sudo("apt install vim")
#runs neofetch command
conn.run("neofetch")
#fetcb ipaddress and only show inet 1st line and valid ip address using regular expression
result = conn.run("ifconfig")

lines = result.stdout.split("\n")
inet_lines = [i for l in lines if "inet " in l and "127.0.0.1" not in l]
span = re.search("inet ([0-9]+\.){3}[1-9]+"), inet_lines.span()
ip_address = inet_lines[0][span[0]+5: span[1]]
print(span)
