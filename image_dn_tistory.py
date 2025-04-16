# -*- coding: utf-8 -*-
import os
import re
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import time
import cv2
from matplotlib import pyplot as plt

target_word = "data/global_q"

overlap=[]
url = 'https://heo2.tistory.com/10/'  #반복되는 곳 사이트 몸통
site = 'https://heo2.tistory.com/10/'   #가져올 사이트 앞부분
rec = "jpg" #반복되는 부분 뒷부분

def Search(getA):
    i=0
    for getLink in getA:
        try:
            data = getLink.get('src')
            if rec in getLink.get("src"):
                if len(data) >= 0 and data not in overlap:
                    overlap.append(data)
                    accessUrl = site + getLinkgit .get("src")
                    print(accessUrl)
                    target = target_word + str(i) + ".jpg"
                    urllib.request.urlretrieve(accessUrl, target)
                    img = cv2.imread(target)
                    fixed_img = cv2.resize(img,(136,63))
                    cv2.imwrite(target, fixed_img)
                    i = i + 1
        except:pass

# request 모듈을 사용하여 웹 페이지의 내용을 가져온다
r = requests.get(url)
print("자료실 요청 : ", r)

# beautiful soup 초기화
soup = BeautifulSoup(r.text, "html.parser")
# 태그로 찾기 (모든 항목)
getA = soup.find_all("img")
print(type(getA))
Search(getA)