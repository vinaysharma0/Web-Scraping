from bs4 import BeautifulSoup

#with open('form.html','r') as file:
   
    #content = file.read()
   # soup = BeautifulSoup(content, 'lxml')
   # tags = soup.find_all('label')
  #  for i in tags:
 #       values = i.text.split()[-1]
#        print(values)
#    
import pandas as pd
import requests


Name = []
Profession = []
KnownMovie = []
About = []

page_number = 1
count = 0
while count <= 122136:
    url = 'https://www.imdb.com/search/name/?gender=male,female&start={}&ref_=rlm'.format(page_number)
    count += 1
    page_number = page_number+50
    html_text = requests.get(url)
    html_text = html_text.text

    soup = BeautifulSoup(html_text, 'lxml')

    contents = soup.find_all('div',class_ = "lister-item-content")
    print('Writing Data......')
    for content in contents : 
        celebName = content.a.text.strip().replace(" ","")
        
        profession = content.p.text.split()[0].strip().replace(" ","")
        
        
        knownmovie = content.p.text.split()[2].strip()
        
        about = content.select('p')[1].text
        
        Name.append(celebName)
        Profession.append(profession)
        KnownMovie.append(knownmovie)
        About.append(about)
    print('Data Writing Completed')
    
    
    
df = pd.DataFrame(list(zip(Name, Profession, KnownMovie, About)), 
                  columns = ['Name', 'Profession', 'KnownMovie', 'About'])   


df.head()

df.to_csv('scraped_IMDB_celeb_data.csv', index = None)