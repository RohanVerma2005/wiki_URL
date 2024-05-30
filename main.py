from bs4 import BeautifulSoup
import requests

def web_scrape_wikipedia(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    Title = soup.find('h1', id='firstHeading').text.strip()

    def first_paragraph_finder(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content_paragraphs = soup.find_all('p')
        first_paragraph = content_paragraphs[1].text
        return first_paragraph

    first_paragraph_data = first_paragraph_finder(url)

    External_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http') and not href.startswith('https://en.wikipedia.org'):
            External_links.append(href)

    Images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        alt = img.get('alt')
        Images.append({'src': src, 'alt': alt})


    return{
        'Title': Title,
        'First_paragraph': first_paragraph_data,
        'External_links': External_links,
        'Images': Images
         }


user_url = input("Enter a URL: ")
data = web_scrape_wikipedia(user_url)

print("Page Title:", data['Title'])
print("First Paragraph:", data['First_paragraph'])
print("External Links:")
for link in data['External_links']:
    print(link)
print("Images:")
for img in data['Images']:
    print(f"{img['src']}({img['alt']})")

