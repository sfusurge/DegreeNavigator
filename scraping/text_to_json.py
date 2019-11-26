file_reader = open('all_courses_output.txt', 'r')
lines = file_reader.readlines()
a = 0
Science = ['ACMA', 'BISC', 'BPK', 'CHEM', 'EASC', 'MATH', 'MBB', 'PHYS', 'SCI', 'STAT']
AppliedScience = ['CMPT','ENSC','MACM',"MSE",'TEKX']
SocialScience = ['COGS', 'CRIM', 'ECON', 'ENGL', 'FNST', 'FREN', 'GA', 'GERO', 'GSWS', 'HIST',
 'HS', 'HUM', 'IS', 'LAS', 'LBST', 'LING', 'PHIL', 'POL', 'PSYC', 'SA', 'WL']
Communication = ['CA,"CMNS','IAT','PUB']
Environment = ['ARCH', 'ENV', 'EVSC', 'GEOG', 'PLAN', 'REM', 'SD']
scienceTypes = []
appliedScienceTypes = []
socialScienceTypes = []
communicationTypes = []
environmentTypes = []
otherTypes = []
while a < len(lines):
    courseType = {}
    currentType = eval(lines[a])[0]
    courseLevels = []
    while a < len(lines) and eval(lines[a])[0] == currentType:
        courseLevel = {}
        currentLevel = eval(lines[a])[1][0]
        courses = []
        while a < len(lines) and eval(lines[a])[1][0] == currentLevel and eval(lines[a])[0] == currentType:
            course = {}
            course["name"] = currentType + ' ' + eval(lines[a])[1]
            course["title"] = eval(lines[a])[2]
            course["description"] = eval(lines[a])[3]
            course["credits"] = eval(lines[a])[4]
            course["WQB"] = eval(lines[a])[5]
            courses.append(course)
            a += 1
        courseLevel["name"] = currentLevel + "XX"
        courseLevel["children"] = courses
        courseLevels.append(courseLevel)
    courseType["name"] = currentType
    courseType["children"] = courseLevels
    if courseType["name"] in Science:
        scienceTypes.append(courseType)
    elif courseType["name"] in AppliedScience:
        appliedScienceTypes.append(courseType)
    elif courseType["name"] in SocialScience:
        socialScienceTypes.append(courseType)
    elif courseType["name"] in Communication:
        communicationTypes.append(courseType)
    elif courseType["name"] in Environment:
        environmentTypes.append(courseType)
    else:
        otherTypes.append(courseType)
    
allCourses = {}
allCourses["name"] = "Courses"
allCourses["children"] = [{'name':'Faculty of Science', 'children': scienceTypes},{'name':'Faculty of Applied Science', 'children':appliedScienceTypes},
{'name':'Faculty of Arts and Social Science', 'children': socialScienceTypes},{'name':'Faculty of Communication, Art, and Technology', 'children': communicationTypes},
{'name':'Faculty of Environment', 'children': environmentTypes}, {'name':'Other Courses', 'children': otherTypes}]

#This code puts the dictionary in the json file

import json
with open('Courses_File2.json', 'w') as fp:
    json.dump(allCourses, fp)
