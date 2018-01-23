import smtplib
fromaddr = 'testemail@gmail.com'
toaddrs  = 'othertestemail@decoariescorp.com'
msg = "\r\n".join([
  "From: testemail@gmail.com",
  "To: othertestemail@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])
username = 'testemail@gmail.com'
password = 'password'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
