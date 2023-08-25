import paramiko

# Command to execute on the remote server
command = "ls -l /tmp/"

#server's information
host = "hostname"
username = "username"
password = "password"
port = 22

# Create an SSH client instance
client = paramiko.client.SSHClient()

# Automatically add the server's host key
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # connect to the server
    client.connect(hostname=host, port=port, username=username, password=password)  

    # Execute the command
    _stdout = client.exec_command(command)[1]   # to get only stdout
    print(_stdout.read().decode())
except paramiko.AuthenticationException:
    print("Authentication failed!!!")
except paramiko.SSHException as e:
    print(f"SSH error: {e}")
finally:
    # Close the SSH connection
    print("Closing the SSH connection to server!!!")
    client.close()
