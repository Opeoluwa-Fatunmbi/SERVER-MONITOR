# SERVER-MONITOR

This script will check the uptime, CPU usage, memory usage, and disk usage of the server and send an email to the specified address with the details. 
You will need to replace the server_name, server_ip, email_username, email_password,
and email_to variables with the appropriate values for your server and email account. 
The script uses the psutil library to get the system information and the smtplib library to send the email.

This is a simple example, you can add more functionality like sending SMS, Creating a log file, etc.
