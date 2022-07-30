#파이썬 크롤링 
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")

elements = soup.select_one("#KOSPI_now")

print(elements.text) #text를 붙여줘야 코스피만 깔끔하게 나옴 

                           
                           
  