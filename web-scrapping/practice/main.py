### Pachages to be installed
# python -m pip install beautifulsoup4, python -m pip install requests, python -m pip install lxml

from bs4 import BeautifulSoup
import os

with open(f'{os.getcwd()}/home.html', 'r') as html_file:
    content = html_file.read()
    # print(content) # output file data

    soup = BeautifulSoup(content, 'lxml') #lxml is a parser
    # print(soup.prettify()) #output file data after prettifying
    
    ## FIND ONE
    # tag = soup.find('h5') # find 1st h5 tag
    # print('Tag: ',tag)
    # print('TAG TEXT HERE: ', tag.text)
    # print('Attribute: ', tag['class'])

    ## FIND ALL
    # course_html_tags = soup.find_all('h5') # find all h5 tags - return list of tags
    # for course in course_html_tags:
    #     print(course.text)

    ## FIND ALL USING ID
    # vars = soup.find_all('div', id="card-python-for-beginners")
    # print(vars)

    ## CARDS
    # course_cards = soup.find_all('div', class_='card')
    # for card in course_cards:
    ## GET ALL TEXTS IN CARDS
    #     print(card.text)
    ## GET ALL h5 TAGS IN course_cards list
    #     print(course.h5)

    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split(' ')[-1]
        
        print(f'"{course_name}" costs {course_price}')
