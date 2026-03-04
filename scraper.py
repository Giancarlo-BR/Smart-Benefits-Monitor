import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/122.0.0.0 Safari/537.36'
    ),
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

URL = 'https://www.melhorescartoes.com.br/c/cartoes-de-credito'




def extract_last_news():
    """Def to scrap the first page and the additional informations on the news link
    and add to a dictionary the page and article texts"""
    
    page = requests.get(URL, headers=HEADERS, timeout=15)
    page_soup = BeautifulSoup(page.text, 'html.parser')
    news_links = page_soup.find_all('div', class_="post-promo-home-c2")

    news = []
    for div in news_links:
        #All infos from the news
        tittle = div.find('h3').find('a').text
        link = div.find('h3').find('a')['href']
        date = div.find('span', class_='date date_post_home').text.strip()

        #All text in the article
        article = requests.get(link, headers=HEADERS, timeout=15)
        article_soup = BeautifulSoup(article.text, 'html.parser')
        article_body = article_soup.find('div', class_="corpo-artigo")
        paragraphs = article_body.find_all('p')
        full_text = ' '.join([p.text for p in paragraphs])

        #Add on a dic the hole information. Dictionary is important because database.py need to acess wich field by the name
        news.append({
            'titulo': tittle,
            'link': link,
            'data_publicacao': date,
            'texto_completo': full_text
        })
    
    return news