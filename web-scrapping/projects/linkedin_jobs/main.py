### Pachages to be installed
# python -m pip install beautifulsoup4, python -m pip install requests, python -m pip install lxml

import time
from bs4 import BeautifulSoup
import requests
from csv import writer

print('Enter "1" for Actively Hiring Jobs')
print('Enter "2" for Early Applicant Jobs')
user_choice = input('>')
print('Filtering data based on your search')
search_with_status = {
    "1": "Actively",
    "2": "early"
}

if(user_choice != '1' and user_choice != '2'):
    print('You Pick Invalid Choice')
    exit()

def find_jobs():
    with open('web-scrapping/linkedin_jobs/jobs.csv', 'w', encoding='utf8') as file:
        the_writer = writer(file)
        header = ['Job Title', 'Company Name', 'Hiring Status', 'Job Post Link']
        the_writer.writerow(header)

        ## Scrapper code starts from here
        html_text = requests.get('https://www.linkedin.com/jobs/search/?currentJobId=3261637060&distance=25&f_WT=2&geoId=103644278&keywords=reactjs%20nodejs').text
        soup = BeautifulSoup(html_text, 'lxml')
        remote_us_jobs = soup.find_all('div', class_="base-card")

        for job in remote_us_jobs:
            job_title = job.find('h3', class_='base-search-card__title').text.strip()
            company_name = job.find('h4', class_='base-search-card__subtitle').text.strip()
            more_info = job.find('a', class_='base-card__full-link')['href']

            hiring_status = ''
            try:
                hiring_status = job.find('div', class_='job-search-card__benefits').text.strip()
            except AttributeError:
                hiring_status = ''

            if search_with_status[user_choice] in hiring_status:
                print(f'Job Title: {job_title}')
                print(f'Company Name: {company_name}')
                print(f'Hiring Status: {hiring_status}')
                print(f'More Info: {more_info}')
                print('')

                ## Add rows in csv file
                info = [job_title, company_name, hiring_status, more_info]
                the_writer.writerow(info)

## find_jobs() will run again after every 10 mins
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait_in_mins = 10
        print(f'Waiting {time_wait_in_mins} minutes...')
        time.sleep(time_wait_in_mins * 60)