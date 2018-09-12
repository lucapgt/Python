import urllib.request
import ftplib
import io
import schedule
import time


def job():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    print(external_ip)
    session = ftplib.FTP('ftp.lucabaratti.it', 'lucabaratti.it', 'Domotica01')
    buf = io.BytesIO()
    buf.write(external_ip.encode('utf8'))
    buf.seek(0)
    session.storbinary("STOR ip.txt", buf)
    session.quit()

#schedule.every(5).minutes.do(job)
schedule.every(1).hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
