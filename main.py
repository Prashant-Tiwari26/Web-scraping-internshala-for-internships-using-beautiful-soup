from bs4 import BeautifulSoup
import requests
from time import sleep

def find_internships():
    html = requests.get("https://internshala.com/internships/data-science,machine-learning-internship/stipend-10000/").text
    soup = BeautifulSoup(html, "lxml")
    jobs = soup.find_all('div', class_ = "internship_meta")
    with open('internships.txt', 'w'):
        pass
    for job in jobs:
        company = job.find('a', class_ = 'link_display_like_text view_detail_button').text.replace("  ","")
        profile = job.find('a', class_ = 'view_detail_button').text
        location = job.find(id='location_names').span.a.text
        stipend = job.find('span', class_ = 'stipend')
        if location == 'Work From Home':
            with open('internships.txt', mode = 'a') as file:
                file.write(f"Company : {company.strip()}\nProfile : {profile}\n")
                if stipend is not None:
                    file.write(f'{stipend.text.strip()}\n')
            print(f"Company : {company.strip()}\nProfile : {profile}")
            if stipend is not None:
                print(stipend.text.strip(),'\n\n')

if __name__ == '__main__':
    while True:
        find_internships()
        time_wait = 1 
        print(f"Searching again in {time_wait} minutes")
        sleep(time_wait*60)