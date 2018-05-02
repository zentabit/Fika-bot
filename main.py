import smtplib
from email.mime.text import MIMEText

class Program:
    def __init__(self):
        self.adress = 'jakob.ristner@itggot.se'
        self.read()
        self.running = True
        with open('password.txt', encoding='ascii') as f:
            self.password = f.read()


    def update(self):
        sample = "Zero Two is best girl"
        


       

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.adress, self.password)
        
        msg = sample
        s.sendmail(self.adress, 'fredrik.tauer@itggot.se', msg)
        s.quit()


    def read(self):
        with open('data.txt', encoding='ascii') as f:
            data = f.read().split("\n")
            self.bakers = dict()
            for line in data:
                self.bakers.update({int(line.split(",")[0]) : line.split(",")[1]})
            print(self.bakers)
                
    
    def send(self, text, recepient):
        pass

program = Program()
while program.running:
    program.update()

