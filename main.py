import os
import psutil
import smtplib
import datetime

# Server details
server_name = "Server1"
server_ip = "192.168.1.1"

# Email details
email_username = "example@gmail.com"
email_password = "password"
email_to = "admin@example.com"

# Check server uptime
uptime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

# Check CPU usage
cpu_percent = psutil.cpu_percent()

# Check memory usage
memory = psutil.virtual_memory()
memory_percent = memory.percent

# Check disk usage
disk = psutil.disk_usage('/')
disk_percent = disk.percent

# Prepare the message
message = f'Server Name: {server_name}\nServer IP: {server_ip}\nUptime: {uptime}\nCPU Usage: {cpu_percent}%\nMemory Usage: {memory_percent}%\nDisk Usage: {disk_percent}%'

# Send the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_username, email_password)
    server.sendmail(email_username, email_to, message)
    print("Email sent successfully")
except Exception as e:
    print(f'Error sending email: {e}')
finally:
    server.quit()
