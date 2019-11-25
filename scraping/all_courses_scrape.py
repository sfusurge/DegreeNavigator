'''
Degree Navigator
Shea Janke
'''
def getPageInfo(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    #NAME & TITLE & CREDITS
    results = soup.find_all('h3')
    courseType = ""
    for result in results:
        if len(result.text.split('-')) > 1:
            titles.append(result.text.split('-')[1][1:result.text.split('-')[1].find('\n')])
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
            descriptions.append(result.text.strip('\n\t '))
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
titles = []
credits = []
descriptions = []
WQB = []
results = soup.find_all('li')
count = 0
for result in results:
    try:
        result = result.find('a')['href']
        if '/students/calendar/2020/spring/courses/' in result:
            getPageInfo('https://www.sfu.ca' + result)
            count +=1
    except:
        continue
for a in range(len(names)):
    wqb = ""
    for b in WQB[a]:
        wqb += b + ","

#print(len(names),len(titles),len(descriptions),len(credits),len(WQB))
#Prints the first 100 courses from the website

File = open(r"all_courses_output.txt","w")
for a in range(len(names)):
    File.write(str([names[a].split()[0], names[a].split()[1], titles[a], descriptions[a], credits[a], WQB[a]]))
    File.write('\n')


File.close()