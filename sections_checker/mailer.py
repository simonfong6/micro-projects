import smtplib

class Mailer:
    def __init__(self):
        self.fromaddr = '@gmail.com'
        self.toaddrs  = '@gmail.com'
        
        self.username = '@ucsd.edu'
        self.password = ''
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.username,self.password)
    
        
    def __del__(self):
        self.server.quit()

    
    def send_full(self):
        msg = "\r\n".join([
          "From: user_me@gmail.com",
          "To: user_you@gmail.com",
          "Subject: SECTIONS FULL",
          "",
          "Why, oh why"
          ])
        self.server.sendmail(self.fromaddr, self.toaddrs, msg)
    
    def send_available(self):
        msg = "\r\n".join([
          "From: user_me@gmail.com",
          "To: user_you@gmail.com",
          "Subject: SECTIONS AVAILABLE",
          "",
          "Why, oh why"
          ])
        self.server.sendmail(self.fromaddr, self.toaddrs, msg)
