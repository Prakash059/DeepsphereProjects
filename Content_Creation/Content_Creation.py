import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
        
def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.in/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.',
                      'https://www.youtube.',
                     'https://www.edureka.',
                     'http://www.edureka.',
                     'https://www.coursera.',
                     'http://www.coursera.',
                     'https://www.udacity.',
                     'https://www.datacamp.',
                     'https://www.udemy.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

#word = "tutorials"
Topic = input("Please input the topic here: ")
df1 = pd.DataFrame(scrape_google(Topic), columns = ['link'])
#df1 = pd.DataFrame(scrape_google(Topic + ' ' + word), columns = ['link'])
df = df1[~df1['link'].str.contains('cours', na=False)]
#for x in df['link']:
#    print(x)

#def get_results(query):
#    
#    query = urllib.parse.quote_plus(query)
#    response = get_source("https://www.google.co.in/search?q=" + query)
#    
#    return response
#
#def parse_results(response):
#    
#    css_identifier_result = ".tF2Cxc"
#    css_identifier_title = "h3"
#    css_identifier_link = ".yuRUbf a"
#    css_identifier_text = ".IsZvec"
#    
#    results = response.html.find(css_identifier_result)
#
#    output = []
#    
#    for result in results:
#
#        item = {
#            'title': result.find(css_identifier_title, first=True).text,
#            'link': result.find(css_identifier_link, first=True).attrs['href'],
#            'text': result.find(css_identifier_text, first=True).text
#        }
#        
#        output.append(item)
#        
#    return output
#
#def google_search(query):
#    response = get_results(query)
#    return parse_results(response)

#Topic = input("Please input the topic here: ")
#results = google_search(Topic)
#results = google_search(Topic + " " + word)
#results1 = list(results)
#df = pd.DataFrame(results1)
# print(df)

list2 = []
import trafilatura
for url in df['link']:
    downloaded = trafilatura.fetch_url(url)
    trafilatura.extract(downloaded)
    # outputs main content and comments as plain text ...
    list1 = trafilatura.extract(downloaded, include_comments=False)
    # outputs main content without comments as XML ...
    list2.append(list1)
    list3 = ''.join(filter(None, list2))
#    print(list3)

import re
text2 = re.compile('[.!?] ').split(list3)
print("\n No. of extracted sentences: ")
print(len(text2))

print("\n \n Below are the scraped urls:")

for x in df['link']:
    print("\n", x)

print("\n Below are the extracted texts from the above urls: ")

for x in text2:
    print("\n", x)
