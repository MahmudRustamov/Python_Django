# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# sender_email = "sanjarbeksocial@gmail.com"
# password = "ajvd xsnx jowk hujh"
#
# subject = "Test Email"
# body = "Nima gap"
#
# receiver_email = "rustamov.mahmud.05@gmail.com"
#
# msg = MIMEMultipart()
# msg['From'] = sender_email
# msg['To'] = receiver_email
# msg['Subject'] = subject
# msg.attach(MIMEText(body, 'plain'))
#
# try:
#     with smtplib.SMTP('smtp.gmail.com', 587) as server:
#         server.starttls()
#         server.login(sender_email, password)
#         text = msg.as_string()
#         server.sendmail(sender_email, receiver_email, text)
#         print("Email sent successfully!")
#
# except Exception as e:
#     print(f"Failed to send email. Error: {e}")
