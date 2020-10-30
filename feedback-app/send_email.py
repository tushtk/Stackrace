import smtplib
from email.mime.text import MIMEText

def send_mail(user,city,rating,comments):
    port = 2525
    smpt_server = 'smtp.mailtrap.io'
    login  = 'e5ef37ac596f5c'
    password = '581ca0c735271b'
    message = f"<h3>New feedback submission</h3><ul><li>User:{user}</li><li>City:{city}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    sender_email = '07c060b6e3-0a448e@inbox.mailtrap.io'
    receiver_email = 'tusht@gmail.com'
    msg = MIMEText(message,'html')
    msg['Subject'] = "Learning feedback"
    msg['From'] = sender_email
    msg['To'] = receiver_email


    #send email
    with smtplib.SMTP(smpt_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

