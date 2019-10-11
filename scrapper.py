import re
import smtplib

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def sendEmail():
    server = smtplib.SMTP_SSL('smtp.yandex.com',465)
    server.ehlo()
    #server.starttls()
    #server.ehlo()
    server.login('jahanxbkhan@yandex.com','istudyiniet1')
    subject = 'Iphone XS price autoBot'
    body = str(nochinese).strip()+ "  Price: RMB ( "+ str(price) +" )"  
    #msg = f"Subject: {subject}\n\n{body}"
    msg = str(subject + " " + body) 
    server.sendmail('jahanxbkhan@yandex.com','jahanxbkhan@hotmail.com',msg)
    print(" Email Sent !!")
    server.quit()


URL = 'https://item.jd.com/100000177748.html'

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:24.0) Gecko/20100101 Firefox/24.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content,'html.parser')




#print(soup.prettify())

title = soup.find("div",{"class":"sku-name"}).text
price_div = soup.find("div",{"class":"summary-price J-summary-price"})
#price = soup.find("span",{"class":"price J-p-s-100000177748"})

print(str(title).strip())
print ("-----")

RE = re.compile(u'[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]',re.UNICODE)
nochinese = RE.sub('',title)
print (nochinese)


print("----")
driver = webdriver.Firefox()
driver.get(URL)
price = driver.find_element_by_css_selector(".p-price .price")
print(price.text)
driver.quit()
sendEmail()

def rmb_pkr():
    return "some bullshit value!!"




