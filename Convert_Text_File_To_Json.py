file_reader = open('Courses_File.txt', 'r')
lines = file_reader.readlines()
courseTypes = {}
a = 0
while a < len(lines):
    currentType = eval(lines[a])[0]
    courseLevels = {}
    while a < len(lines) and eval(lines[a])[0] == currentType:
        currentLevel = eval(lines[a])[1][0]
        courses = {}
        while a < len(lines) and eval(lines[a])[1][0] == currentLevel:
            courses[currentType + ' ' + eval(lines[a])[1]] = [eval(lines[a])[2], eval(lines[a])[3], eval(lines[a])[4], eval(lines[a])[5]]
            a += 1
        courseLevels[currentLevel + "XX"] = courses
    courseTypes[currentType] = courseLevels


#This code puts the dictionary in the json file
'''
import json
with open('Courses_File.json', 'w') as fp:
    json.dump(courseTypes, fp)
'''
