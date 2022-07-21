import requests
from bs4 import BeautifulSoup
import pandas as pd
import random 


url = 'https://rss.nytimes.com/services/xml/rss/nyt/US.xml'
xml_data = requests.get(url).content 


def parse_xml(xml_data):
      # Initializing soup variable
    soup = BeautifulSoup(xml_data, 'xml')

  # Creating column for table
    df = pd.DataFrame(columns=['guid', 'title', 'pubDate', 'description'])

  # Iterating through item tag and extracting elements
    all_items = soup.find_all('item')
    items_length = len(all_items)
    
    for index, item in enumerate(all_items):
        guid = item.find('guid').text
        title = item.find('title').text
        pub_date = item.find('pubDate').text
        description = item.find('description').text
        likes = str(random.randint(1,1000)).format("0.f")

        

       # Adding extracted elements to rows in table
        row = {
            'guid': guid,
            'title': title,
            'pubDate': pub_date,
            'description': description,
            'likes':likes
        }

        df = df.append(row, ignore_index=True)
        print(f'Appending row %s of %s' % (index+1, items_length))

    return df

df = parse_xml(xml_data)
df.to_csv('news1.csv')
    