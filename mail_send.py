import smtplib

def mail_send(mail_user, mail_password, mail_to, mail_message, smtp_server, smtp_port):
	try:
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()
		server.login(mail_user, mail_password)
		server.sendmail(mail_user, mail_to, mail_message)
		server.quit()
		done()
	except:
		failed()

def done():
	print('Done!')

def failed():
	print('failed!')
	
mail_user = ''
mail_password = ''
mail_to = ''
mail_message = 'Salut, ceci est un message en Python!'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

mail_send(mail_user, mail_password, mail_to, mail_message, smtp_server, smtp_port)
	
