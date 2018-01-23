import smtplib
fromaddr = 'test"gmail.com'
toaddrs  = 'testOther@gmail.com'
msg = "\r\n".join([
  "From: test@gmail.com",
  "To: testOther@gmail.com",
  "Subject: Test",
  "",
  "test"
  ])
username = 'test@gmail.com'
password = 'password'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
