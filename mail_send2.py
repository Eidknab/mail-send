import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def mail_send(mail_user, mail_password, mail_to, mail_subject, mail_body, filename, smtp_server='smtp.gmail.com', smtp_port=587):
	try:
		attachment = open(filename, 'rb')

		mail_message = MIMEMultipart()
		mail_message['From'] = mail_user
		mail_message['To'] = mail_to
		mail_message['Subject'] = mail_subject
		mail_message.attach(MIMEText (mail_body, 'plain'))

		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition',"attachment; filename= "+filename)

		mail_message.attach(part)
		mail_message = mail_message.as_string()

		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()
		server.login(mail_user, mail_password)
		server.sendmail(mail_user, mail_to, mail_message)
		server.quit()
	except AttributeError:
		print("Input Error! (int)")
	except TypeError:
		print("Input Error! (empty var)")
	except smtplib.SMTPAuthenticationError:
		print("Authentification Error! (wrong user: {} or password: {})".format(mail_user, mail_password))
	except FileNotFoundError:
		print("Attachement {} Not Found!".format(filename))
	except smtplib.SMTPServerDisconnected:
		print("Smtp Connexion Error!")
	except TimeoutError:
		print("Timeout Error! (wrong smtp port)")
	except:
		failed()
	else:
		done()
		
def done():
	print('Done!')

def failed():
	print('Failed!')
	
mail_user = ''
mail_password = ''
mail_to = ''
mail_subject = 'Python!'
mail_body = 'Salut, ceci est un message en Python!'
filename = 'file1.txt'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
mail_send(mail_user, mail_password, mail_to, mail_subject, mail_body, filename, smtp_server, smtp_port)

	
