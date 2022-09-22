from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import os

email= os.getenv('EMAIL')
password = os.getenv('PASSWORD')


def sendAttackAllert(attackData):

    context = ssl.create_default_context()

    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls(context=context)

    server.login(email, password)

    user_email = email
    message = "Tentativa de ataque feita pelo ip {} pela url {} no dia {}.".format(attackData.ip, attackData.route, attackData.attack_date)


    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = user_email
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Tentativa de Invasão"

    msg.attach(MIMEText(message, "plain"))

    try:
        server.sendmail(email, user_email, msg.as_string() )

        server.quit()

        return True
    except:
        server.quit()
        return False