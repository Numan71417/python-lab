import requests
from bs4 import BeautifulSoup

url = 'https://m.imdb.com/chart/top/'
url2 = 'https://m.imdb.com/'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def getTitles(soup):
    movie_titles =  soup.find_all('h3' , class_='ipc-title__text')[1:11] 
    return [ title.text for title in movie_titles ]


def getYears(soup):
    years = []
    years_div = soup.find_all('div',class_='sc-b189961a-7 feoqjK cli-title-metadata')[:11]

    for i in years_div:
        movie_year = i.find('span', class_='sc-b189961a-8 kLaxqf cli-title-metadata-item')
        years.append(movie_year.text)

    return years


def getSummary(link):
    new_url = url2 + link

    response  = requests.get(new_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    summ = soup.find('span', class_='sc-7193fc79-0 ftEVcu')
    return summ.text
    

def getMovieDetails():
    response  = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    movie_titles =  getTitles(soup=soup)
    movie_years =  getYears(soup=soup)

    summary_links = soup.find_all('a', class_='ipc-title-link-wrapper')[:11]
    summary_links = [ links['href'] for links in summary_links ]

    movie_summary = []
    for link in summary_links:
        movie_summary.append(getSummary(link))

    return list(zip(movie_titles,movie_years,movie_summary))


result = getMovieDetails()

for n in result:
    print(n)
    print()

