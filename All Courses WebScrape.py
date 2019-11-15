'''
Degree Navigator
Shea Janke
'''
def getPageInfo(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    #NAMES & CREDITS
    results = soup.find_all('h3')
    courseType = ""
    for result in results:
        words = result.text.split()
        for word in words:
            word = word.strip('\n\t,;')
            if word.isalpha():
                if word.upper() == word:
                    courseType = word
            elif word.strip('WXABCDEF').isdigit() and len(word.strip('WABCDEF')) == 3:
                names.append(courseType + ' ' + word)
            elif word[0] == "(" and word.strip('()').isdigit():
                credits.append(word.strip('()'))
        if len(credits) < len(names):
            credits.append(0)

    #WQB
    results = soup.find_all('p')
    for result in results:
        text = result.text
        if text[0] == '\n':
            text = text.split('.')
            wqb = []
            if len(text) >= 2:
                text = text[-2]
                if "Quantitative" in text:
                    wqb.append("Q")
                if "Writing" in text:
                    wqb.append("W")
                if "Science" in text and "Breadth" in text:
                    wqb.append("B-Sci")
                if "Hum" in text and "Breadth" in text:
                    wqb.append("B-Hum")
                if "Social Sci" in text and "Breadth" in text:
                    wqb.append("B-Soc")
            WQB.append(wqb)


import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.sfu.ca/students/calendar/2020/spring/courses.html')
soup = BeautifulSoup(r.text,'html.parser')
names = []
credits = []
WQB = []
results = soup.find_all('li')
count = 0
for result in results:
    try:
        result = result.find('a')['href']
        if '/students/calendar/2020/spring/courses/' in result and count < 20:
            getPageInfo('https://www.sfu.ca' + result)
            count +=1
    except:
        continue
for a in range(len(names)):
    wqb = ""
    for b in WQB[a]:
        wqb += b + ","

for a in range (100):
    print(names[a],credits[a],WQB[a])