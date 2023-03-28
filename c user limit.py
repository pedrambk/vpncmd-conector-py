import subprocess

vpncmd = r'" "'
serverip = ' '
serverport = ' '
serverpassword = ' '


command = f'{vpncmd} /server {serverip}:{serverport} /adminhub:DEFAULT /password:{serverpassword} /cmd UserList > userlist.txt'
subprocess.run(command, shell=True)

# باز کردن فایل و پردازش اطلاعات آن
with open('userlist.txt', 'r') as f, open('user.txt', 'w') as out:
    for line in f:
        if 'User Name' in line:
            username = line.split('|')[1].strip() 
        if 'Transfer Bytes' in line:
            transfer_bytes = int(line.split('|')[1].strip().replace(',', ''))  # Transfer Bytes 

            
            if transfer_bytes > 1000000000:
                out.write(f'{username}\n')
                
                
                





