import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("simonfong6@gmail.com", "!1BeerCoke")
 
msg = "YOUR MESSAGE!"
server.sendmail("simonfong@gmail.com", "scf001@ucsd.edu", msg)
server.quit()
