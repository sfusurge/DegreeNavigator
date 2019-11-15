# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:04:53 2019

@author: Shea
"""
import requests  
r = requests.get('https://www.sfu.ca/students/calendar/2020/spring/courses.html')

from bs4 import BeautifulSoup  
soup = BeautifulSoup(r.text, 'html.parser')
names = []
credits = []
WQB = []
prerequisitesText = []
courseTypes = []

#Course Types
results = soup.find_all('li')
for result in results:
    result = result.text
    if "(" in result:
        courseTypes.append(result[result.find("(") + 1:result.find(")")])

r = requests.get('http://www.sfu.ca/students/calendar/2020/spring/programs/computing-science/major/bachelor-of-science-or-bachelor-of-arts.html')
soup = BeautifulSoup(r.text, 'html.parser')
#Names
results = soup.find_all('a', attrs={'class':'course-link'}) 
for result in results:  
    names.append(str(result.text).strip()[0:9].strip())

#Credits
results = soup.find_all('span', attrs={'class':'units'})
for result in results:
    result = result.text.replace('\n','')
    result = result.strip('\t ()')
    if result.isdigit():
        credits.append(int(result))

#Prerequisites
results = soup.find_all('div', attrs={'class':'course-description'})
for result in results:
    text = result.find('p',attrs={}).text
    text = text[text.find("Prerequisite")+14:text.find("Corequisite")]
    text = text[:text.find(".")]
    prerequisitesText.append(text)
    #getOrder(text)
    #extractPrereqs2(text)

#WQB
for result in results:
    text = result.find('p',attrs={}).text
    text = text.split(".")
    wqb = []
    if len(text) >= 2:
        text = text[-2]
        if "Quantitative" in text:
            wqb.append("Q")
        if "Science" in text and "Breadth" in text:
            wqb.append("B-Sci")
        if "Hum" in text and "Breadth" in text:
            wqb.append("B-Hum")
        if "Social Sci" in text and "Breadth" in text:
            wqb.append("B-Soc")
    WQB.append(wqb)

for a in range(len(names)):
    print("COURSE NAME:", names[a], " CREDITS:",credits[a], "WQB:",WQB[a]," PREREQUISITES:",prerequisitesText[a])