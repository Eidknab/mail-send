import smtplib

def mail_send(mail_user, mail_password, mail_to, mail_message, smtp_server='smtp.gmail.com', smtp_port=587):
	try:
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()
		server.login(mail_user, mail_password)
		server.sendmail(mail_user, mail_to, mail_message)
		server.quit()
	except AttributeError:
		print("Input Error! (int)")
	except TypeError :
		print("Input Error! (empty var)")
	except smtplib.SMTPAuthenticationError:
		print("Authentification Error! (wrong user: {} or password: {})".format(mail_user, mail_password))
	except smtplib.SMTPServerDisconnected:
		print("Smtp Connexion Error!")
	except TimeoutError:
		print("Timeout Error! (wrong smtp port)")
	except BaseException as e:
		print(e)
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
mail_message = 'Salut, ceci est un message en Python!'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

mail_send(mail_user, mail_password, mail_to, mail_message, smtp_server, smtp_port)
	
