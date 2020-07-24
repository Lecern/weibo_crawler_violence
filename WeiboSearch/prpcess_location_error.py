import pymongo
import requests
from bs4 import BeautifulSoup
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import Tree

if __name__ == '__main__':
    client = pymongo.MongoClient()
    collection = client['covid_domestic_violence']['weibo_zh']
    query = {"place": {
        u"$ne": None
    }}
    cursor = collection.find(query)
    try:
        for doc in cursor:
            if doc['place'] is True or doc['place'] == '':
                url = doc['weibo_url'].replace('.com', '.cn')
                html = requests.get(url)
                soup = BeautifulSoup(html.text.encode('utf-8', 'ignore'), 'html.parser')
                print(soup.title)
    finally:
        client.close()


