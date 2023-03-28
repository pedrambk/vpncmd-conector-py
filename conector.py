import subprocess

vpncmd = r'" "'
serverip = ''
serverport = ''
serverpassword = ''

command = f'{vpncmd} /server {serverip}:{serverport} /adminhub:DEFAULT /password:{serverpassword} /cmd UserList > userlist.txt'
subprocess.run(command, shell=True)
print('User list saved to userlist.txt')

