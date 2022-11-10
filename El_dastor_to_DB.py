import requests
from bs4 import BeautifulSoup
import sqlite3
import time
import itertools


start = time.perf_counter()

#3 Head Data
lst_set = []
lst_total = []
lst_percent = []
#7 Detils Data
lst_name = []
lst_school = []
lst_educational_management = []
lst_student_status = []
lst_kind_of_educational = []
lst_division = []
#13 Degree
lst_arabic = []
lst_first_forign_language = []
lst_second_forign_language = []
lst_pure_mathematics = []
lst_history = []
lst_geography = []
lst_philosophy_logic = []
lst_psychology_sociology = []
lst_chemistry = []
lst_biology = []
lst_geology_environmental_sciences = []
lst_applied_mathematics = []
lst_physics  = []
#input
start_set = int(input("Enter the start set number: "))
end_set = int(input("Enter the end set number: "))
start_name = start_set
lst_valid_sets = []
lst = []

while start_set <= end_set:  
    start_set += 1
    lst.append(start_set-1)
print(lst)
for i in lst:
    try:
        headers = {

            'Referer': 'http://natega.dostor.org/'
        }

        data = {
            'seating_no': i,
        }

        response = requests.post('http://natega.dostor.org/Home/Result', headers=headers, data=data, verify=False)

        #print(response.text)
        #print(response)

        soup = BeautifulSoup(response.content, "lxml")
        #print(soup)
        #3 Head Data

        set_number = soup.find_all('h1')[0].get_text() 
        print("Valid set number")
        lst_valid_sets.append(i)
    except:
        print("invalid set number")
        
    

print(lst_valid_sets)

for x in lst_valid_sets:
    
    headers = {

        'Referer': 'http://natega.dostor.org/'
    }

    data = {
        'seating_no': x,
    }

    response = requests.post('http://natega.dostor.org/Home/Result', headers=headers, data=data, verify=False)

    #print(response.text)
    #print(response)

    soup = BeautifulSoup(response.content, "lxml")
    #print(soup)
    #3 Head Data
    
    set_number = soup.find_all('h1')[0].get_text() 
    #print(set_number)
    lst_set.append(set_number)
    total_number = soup.find_all('h1')[1].get_text()
    #print(total_number)
    lst_total.append(total_number)
    percentage = float(soup.find_all('h1')[2].get_text()[:5]) 
    #print(percentage)
    lst_percent.append(percentage)

    #7 Detils Data

    name = soup.find(id ='pills-tab', attrs={'class': 'nav-pills mb-3'}).find_all('span')[1].get_text() 
    #print(name)
    lst_name.append(name)
    school = soup.find(id ='pills-tab', attrs={'class': 'nav-pills mb-3'}).find_all('span')[3].get_text() 
    #print(school)
    lst_school.append(school)
    educational_management = soup.find(id ='pills-tab', attrs={'class': 'nav-pills mb-3'}).find_all('span')[5].get_text() 
    #print(educational_management)
    lst_educational_management.append(educational_management)
    student_status = soup.find(id ='pills-tab', attrs={'class': 'nav-pills mb-3'}).find_all('span')[9].get_text() 
    #print(student_status)
    lst_student_status.append(student_status)
    kind_of_educational = soup.find(id ='pills-tab', attrs={'class': 'nav-pills mb-3'}).find_all('span')[11].get_text() 
    #print(kind_of_educational)
    lst_kind_of_educational.append(kind_of_educational)
    division = soup.find(id ='pills-tab', attrs={'class': 'nav-pills mb-3'}).find_all('span')[13].get_text()
    #print(division)
    lst_division.append(division)

    #Degree

    arabic = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[1].get_text()
    #print(arbic)
    lst_arabic.append(arabic)
    first_forign_language = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[3].get_text()
    #print(first_forign_language)
    lst_first_forign_language.append(first_forign_language)
    second_forign_language = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[5].get_text()
    #print(second_forign_language)
    lst_second_forign_language.append(second_forign_language)
    pure_mathematics = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[7].get_text()
    #print(pure_mathematics)
    lst_pure_mathematics.append(pure_mathematics)
    history = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[9].get_text()
    #print(history)
    lst_history.append(history)
    geography = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[11].get_text()
    #print(geography)
    lst_geography.append(geography)
    philosophy_logic = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[13].get_text()
    #print(philosophy_logic)
    lst_philosophy_logic.append(philosophy_logic)
    psychology_sociology = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[15].get_text()
    #print(psychology_sociology)
    lst_psychology_sociology.append(psychology_sociology)
    chemistry = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[17].get_text()
    #print(chemistry)
    lst_chemistry.append(chemistry)
    biology = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[19].get_text()
    #print(biology)
    lst_biology.append(biology)
    geology_environmental_sciences = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[21].get_text()
    #print(geology_environmental_sciences)
    lst_geology_environmental_sciences.append(geology_environmental_sciences)
    applied_mathematics = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[23].get_text()
    #print(applied_mathematics)
    lst_applied_mathematics.append(applied_mathematics)
    physics = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[25].get_text()
    #print(physics)
    lst_physics.append(physics)
    

    # Another subjects

    #religious_education = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[1].get_text()
    #print(religious_education)


#/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li[1]/span[1]
#/html/body/div[1]/div[5]/div[5]/div/ul/li[1]/span[1]
print(lst_set, lst_total, lst_percent)
print(lst_name, lst_school, lst_educational_management, lst_student_status, lst_kind_of_educational, lst_division)
print(lst_arabic, lst_first_forign_language, lst_second_forign_language, lst_pure_mathematics, lst_history, lst_geography, lst_philosophy_logic,
 lst_psychology_sociology, lst_chemistry, lst_biology, lst_geology_environmental_sciences, lst_applied_mathematics, lst_physics)

#Store in datebase
#Create Database and connect
db = sqlite3.connect(f"thanwey_{str(start_name)}_to_{str(end_set)}_data.db")

#Setting up The Cursor
cr = db.cursor()

#Create Table and fields(Columns)
cr.execute("CREATE TABLE  IF NOT EXISTS students(user_id INTEGER, set_number INTEGER, name TEXT, school TEXT, educational_management TEXT, student_status TEXT, kind_of_educational TEXT, division TEXT, arabic INTEGER, first_forign_language INTEGER, second_forign_language INTEGER, pure_mathematics INTEGER, history INTEGER, geography INTEGER, philosophy_logic INTEGER, psychology_sociology INTEGER, chemistry INTEGER, biology INTEGER, geology_environmental_sciences INTEGER, applied_mathematics INTEGER, physics INTEGER, totla_degree INTEGER, percentage FLOAT)")

for key, (set, nam, sch, em, ss, koe, di, ara, ffl, sfl, pm, his, geo, pl, ps, ch, bi, ges, am, ph, tot, pe) in enumerate(itertools.zip_longest(lst_set, lst_name, lst_school, lst_educational_management, lst_student_status, lst_kind_of_educational, lst_division, lst_arabic, lst_first_forign_language, lst_second_forign_language, lst_pure_mathematics, lst_history, lst_geography, lst_philosophy_logic, lst_psychology_sociology, lst_chemistry, lst_biology, lst_geology_environmental_sciences, lst_applied_mathematics, lst_physics, lst_total, lst_percent)):
    cr.execute(f"INSERT INTO students(user_id, set_number, name, school, educational_management, student_status, kind_of_educational, division, arabic, first_forign_language, second_forign_language, pure_mathematics, history, geography, philosophy_logic, psychology_sociology, chemistry, biology, geology_environmental_sciences, applied_mathematics, physics, totla_degree, percentage) VALUES({key +1}, '{set}', '{nam}', '{sch}', '{em}', '{ss}', '{koe}', '{di}', '{ara}', '{ffl}', '{sfl}', '{pm}', '{his}', '{geo}', '{pl}', '{ps}', '{ch}', '{bi}', '{geo}', '{am}', '{ph}', '{tot}', '{pe}')")

#for index, (value1, value2) in enumerate(zip(data1, data2)): #only work in two lists

#Save (Commit) changes
db.commit()
#Close Database
db.close()



finish = time.perf_counter()

#print(f'Finished in {round(finish-start, 2)} secound')
print('Finished in {} secound'.format(round(finish-start, 2)))
