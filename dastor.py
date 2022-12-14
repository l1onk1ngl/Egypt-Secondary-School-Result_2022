import requests
from bs4 import BeautifulSoup
import pandas as pd
import time




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
lst_arbic = []
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
# Another subjects
lst_religion = []
lst_national_edu = []
lst_stats_eco = []

#input
start_set = int(input("Enter the start set number: "))
end_set = int(input("Enter the end set number: "))
start_name = start_set
lst_valid_sets = []
lst = []
lst_error = []
count = 0



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
        count += 1
        
print(lst_valid_sets)

if len(lst_valid_sets) > 0:
    for x in lst_valid_sets:
        try:    
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

            arbic = soup.find(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'}).find_all('span')[1].get_text()
            #print(arbic)
            lst_arbic.append(arbic)
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

            religion_education = soup.find_all(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'})[1].find_all('span')[1].get_text()
            lst_religion.append(religion_education)            
            #print(religion_education)
            national_education = soup.find_all(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'})[1].find_all('span')[3].get_text()
            lst_national_edu.append(national_education)            
            #print(national_education)
            stats_eco = soup.find_all(id ='pills-tab', attrs={'class': 'nav nav-pills mb-3'})[1].find_all('span')[5].get_text()
            lst_stats_eco.append(stats_eco)            
            #print(stats_eco)

        except:
            print(f"Error happen in {x}")    
            lst_error.append(x)
        
    #print(lst_set, lst_total, lst_percent)
    #print(lst_name, lst_school, lst_educational_management, lst_student_status, lst_kind_of_educational, lst_division)
    #print(lst_arbic, lst_first_forign_language, lst_second_forign_language, lst_pure_mathematics, lst_history, lst_geography, lst_philosophy_logic,
    #lst_psychology_sociology, lst_chemistry, lst_biology, lst_geology_environmental_sciences, lst_applied_mathematics, lst_physics)

    df = pd.DataFrame(
        {'set_number': lst_set,'name': lst_name, 'school': lst_school,
        'educational_management': lst_educational_management, 'student_status': lst_student_status,
        'kind_of_educational': lst_kind_of_educational, 'division': lst_division, 'arabic': lst_arbic, 'first_forign_language': lst_first_forign_language,
        'second_forign_language': lst_second_forign_language, 'pure_mathematics': lst_pure_mathematics, 'history': lst_history,
        'geography': lst_geography, 'philosophy_logic': lst_philosophy_logic, 'psychology_sociology': lst_psychology_sociology,
        'chemistry': lst_chemistry, 'biology': lst_biology, 'geology_environmental_sciences': lst_geology_environmental_sciences,
        'applied_mathematics': lst_applied_mathematics, 'physics': lst_physics, 'religion': lst_religion, 'national': lst_national_edu,
        'stats_eco': lst_stats_eco, 'totla_degree': lst_total, 'percentage':lst_percent})
    print(df)
    df.to_csv(f'thanwey_{str(start_name)}_to_{str(end_set)}_data.csv',encoding="utf-8-sig", index=False)
    #Error text
    if len(lst_error) > 0:        
        file_name = open(f"{str(start_name)}_to_{str(end_set)}_Erorr.txt", "w", encoding="utf-8")
        for e in lst_error:
            file_name.write("\n1-"+f"{e}")
else:
    print("Error no valid data")
    file_name = open(f"{str(start_name)}_to_{str(end_set)}_No_valid_data.txt", "w", encoding="utf-8")
    file_name.write("\n1-"+f"{str(count)}")
finish = time.perf_counter()

#print(f'Finished in {round(finish-start, 2)} secound')
print('Finished in {} secound'.format(round(finish-start, 2)))
