# 웹크롤링 프로젝트
# https://h-glacier.tistory.com/


from bs4 import BeautifulSoup
from flask import Flask, render_template
import urllib.request
import datetime 

app = Flask(__name__)

@app.route('/')
def index():
    # 현재 시간 정보 받아오기
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
    soup = BeautifulSoup(webpage, 'html.parser')
    seo_temps = soup.find('span', "todaytemp").get_text()
    seo_cast = soup.find('p', "cast_txt").get_text()

    webpage2 = urllib.request.urlopen('https://search.naver.com/search.naver?query=%EC%95%88%EC%96%91%EB%82%A0%EC%94%A8&ie=utf8&sm=whl_nht')
    soup = BeautifulSoup(webpage2, 'html.parser')
    any_temps = soup.find('span', "todaytemp").get_text()
    any_cast = soup.find('p', "cast_txt").get_text()


    webpage3 = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%EC%82%B0%EB%82%A0%EC%94%A8')
    soup = BeautifulSoup(webpage3, 'html.parser')
    bus_temps = soup.find('span', "todaytemp").get_text()
    bus_cast = soup.find('p', "cast_txt").get_text()

    webpage4 = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%ED%8F%89%EB%82%A0%EC%94%A8')
    soup = BeautifulSoup(webpage4, 'html.parser')
    bup_temps = soup.find('span', "todaytemp").get_text()
    bup_cast = soup.find('p', "cast_txt").get_text()

    return render_template('index.html', 
    nowDate=nowDate, 
    seo_temps=seo_temps, 
    seo_cast=seo_cast,
    any_temps=any_temps,
    any_cast=any_cast,
    bus_temps=bus_temps,
    bus_cast=bus_cast,
    bup_temps=bup_temps,
    bup_cast=bup_cast)





