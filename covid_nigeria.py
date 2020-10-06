######••••••••••######___________________________________________
# Scrape data from NCDC website
#_______________________________________________________________

import requests
import pandas as pd

from bs4 import BeautifulSoup

page = requests.get("https://covid19.ncdc.gov.ng/report/")

if page.status_code == 200:
    print("Page download is successful!")
else:
    print("Couldn\'t download page")

soup = BeautifulSoup(page.content, 'html.parser')



print(soup.title.text)

table = soup.find('table', attrs={"id" : "custom1"})

trs = table.select("tbody tr")

#_______Extract one row to see how the data is stored______

tr1 = trs[3] # table row

# Extracting number of cases, deaths, etc

td1 = tr1.find_all("td")
print(td1)

print(td1[0].text, 
      td1[1].text, 
      td1[2].text,
      td1[3].text,
      td1[4].text)


'''
Some values preceeded by '/n' used for new line in the HTML code. replace() function is used to get 
rid of it.
'''

#__________Write the same code in a loop to extract values for all the countries.

States= []
Cases_lab = []
Cases_adm = []
Discharged = []
Deaths= []


for tr in trs:
    tds = tr.find_all("td")
    
    States.append(tds[0].text.replace("\n", "").strip())
    Cases_lab.append(tds[1].text.replace("\n", "").strip())
    Cases_adm.append(tds[2].text.replace("\n", "").strip())
    Discharged.append(tds[3].text.replace("\n", "").strip())
    Deaths.append(tds[4].text.replace("\n", "").strip())

#______ Store in dataframe

data = list(zip(States, Cases_lab, Cases_adm, Discharged, Deaths))

data_covid = pd.DataFrame(data, columns=['States_affected', 'Confirmed_cases', 'Active_cases',
                                         'Discharged_cases', 'Deaths'])
data_covid
