# let’s see how to create and send a simple text message
# import smtplib  # Import smtplib
# from email.message import EmailMessage # Import the email modules
# email = EmailMessage()
# email['to'] = "Harshal Kotadiya"
# email['from'] = 'hkotadiya001@gmail.com'
# email['subject'] = "Hello! I am new here. "
#
# email.set_content('You got me!')
#
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as s:
#
#     s.ehlo()
#     s.starttls()
#     s.login('hkotadiya001@gmail.com', 'Patel@92')  # Turn on less secure account ON

*******************************************************************************
import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "hkotadiya001@gmail.com"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()


try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)

except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()