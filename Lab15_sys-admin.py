import os
os.system("ls") 
#takes a string argument and run a Bash command
import subprocess
"""
#subprocess module is used to spawn new processes,/ connect to input/output/error pipes, and obtain error codes
subprocess.run(["ls"])
#bash command to show the content 
subprocess.run(["ls","-l"])
subprocess.run(["ls","-l","README.md"])

#calling the uname command to get sygtem information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
"""
command="ps"
# variable command set to ps - 
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])