import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html= Template(Path("index.html").read_text())
email= EmailMessage()
email['from']= "preksha.chaudhary05@gmail.com"
email['to']= "ayushr.patil@gmail.com"
email['subject']= 'SALE!!!'
email.set_content(html.substitute({'name': 'Preksha'}), 'html')

with smtplib.SMTP( host="smtp.gmail.com", port='587') as smp:
        smp.ehlo()
        smp.starttls()
        smp.login('preksha.chaudhary05@gmail.com', "fgzw mgwf trzl cizo")
        smp.send_message(email)
        
