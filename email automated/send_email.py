import smtplib
from email.mime.text import MIMEText

sender_email = "sidhu.kandoth@gmail.com"
receiver_email = input("enter receiver: ")
app_password = "hjfo qdkt icfv xqlg"  
x=input("enter body of the email: ")
msg = MIMEText(x)
msg['Subject'] = input("enter subject: ")
msg['From'] = sender_email
msg['To'] = receiver_email

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()  
server.starttls()  
server.ehlo()  

try:
    server.login(sender_email, app_password)
    print("Login successful")

    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully")
except smtplib.SMTPAuthenticationError as e:
    print("SMTP Authentication Error:", e)
finally:
    server.quit()