import smtplib
fromaddr = 'shadowrs0@gmail.com'
toaddrs  = 'sales@decoariescorp.com'
msg = "\r\n".join([
  "From: shadowrs0@gmail.com",
  "To: shadowrs0@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])
username = 'shadowrs0@gmail.com'
password = 'bfmvreponic'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
