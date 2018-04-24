import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
    url = "http://ggsipu.ac.in/ExamResults/ExamResultsmain.htm"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    
    if str(soup).find("Exam (Dec.2017) Result of B.Tech") == -1:
        print ('nhi hua')
        time.sleep(60)

        continue
    elif str(soup).find("Exam (Dec.2017) Result for B.Tech") == -1:    
          print ('nhi hua')
        
        continue
    else:
        msg = 'Subject: This is Tarun script talking, CHECK RESULTS!'
        fromaddr = 'tarunpreet2697@gmail.com'
        toaddrs  = 'tarunpreet2697@gmail.com'
        
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
       
        server.login("tarunpreet2697@gmail.com", "killermanss")
        
        
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        
        
        server.sendmail(fromaddr, toaddrs, msg)
        
        server.quit()
        
        break