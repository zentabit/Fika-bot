import smtplib, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

def send(to):
    json_data=open("credentials.json").read()
    data = json.loads(json_data)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(data["uname"], data["pass"])
 
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Glöm inte att baka!"
    msg['From'] = data["uname"]
    msg['To'] = to
    msg.attach(MIMEText("Glöm inte att baka till tisdag!", 'plain'))
    
    with open('email.html', encoding='utf8') as f:
        html = f.read()

    html = MIMEText(html, 'html')
    msg.attach(html)

    server.sendmail(data["uname"], to, msg.as_string())
    server.quit()

    return "ok"

def read(file):
    with open(file) as f:
        bakers = eval(f.read())
    week = date.today().isocalendar()[1] + 1
    baker = bakers[week]
    return baker

send(read("data.txt"))