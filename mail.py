import smtplib

from config import rules


from email.mime.text import MIMEText


def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "finance@inprobes.com"
    msg['To'] = rules['email']['receiver']

    with smtplib.SMTP('smtp.mailgun.org', 587) as mail_server:
        mail_server.login('postmaster@mg.inprobes.com', 'MAILGUN_APIKEY')
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
        # mail_server.quit()
