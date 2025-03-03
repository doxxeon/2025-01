from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver: # 실행 브라우저
    driver.get('https://news.naver.com')