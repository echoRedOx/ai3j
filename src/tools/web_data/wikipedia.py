from json import detect_encoding
import requests
from bs4 import BeautifulSoup
import random
import time
from dotenv import load_dotenv
import re


load_dotenv()


def parse_wikipedia_article(response: requests.Response):
    """
    Parse http response for a wikipedia article.

    :param response: The http response to parse.
    :returns: The title and content of the wikipedia article.
    """
    soup = BeautifulSoup(response.text, 'html.parser')
    page_title = soup.find('title').text
    page_content = soup.find('div', {'id': 'mw-content-text'}).text
    return page_title, page_content


def remove_references(text: str) -> (str):
    """
    Remove citation references from wikipedia article text by removing text between square brackets and the square brackets themselves.

    :param text: The text to remove references from.
    """
    # Remove the square brackets and numbers inside them
    text = re.sub(r'\[\d+\]', '', text)
    return text


def wikipedia_get_random_article() -> None:
    while True:
        response = requests.get(url="https://en.wikipedia.org/wiki/Special:Random")
        page_title, page_content = parse_wikipedia_article(response)
        
        try:
            if detect_encoding(page_content) != 'en':
                print(f"Skipping non-English article: {page_title}")
                continue
        except Exception as e:
            print(f"Skipping article due to error during language detection: {page_title}. Error: {str(e)}")
            time.sleep(random.randint(1, 12))
            continue

        page_content = remove_references(page_content)

        with open(f"wikipedia_{page_title}.txt", "x") as f:
            f.write(page_content)
        
        time.sleep(random.randint(1,12))


def wikipedia_get_search_article(search_query: str) -> None:
    """
    Search Wikipedia for the query and get the first result's title and content.

    :param query: The query to search Wikipedia for.
    :returns: A .txt file containing the article content saved to agent directory.
    """
    response = requests.get(url="https://en.wikipedia.org/wiki/...search...")
    page_title, page_content = parse_wikipedia_article(response)
    
    try:
        if detect_encoding(page_content) != 'en':
            print(f"Skipping non-English article: {page_title}")
            return
    except Exception as e:
        print(f"Skipping article due to error during language detection: {page_title}. Error: {str(e)}")
        return
        
    page_content = remove_references(page_content)

    with open(f"wikipedia_{page_title}.txt", "x") as f:
        f.write(page_content)


def o_wikipedia_get_search_article(query: str) -> None:
    """
    A slightly beefier version of wikipedia_get_search_article() that also saves the article content to a file.

    :param query: The query to search Wikipedia for.
    :returns: A .txt file containing the article content saved to agent directory.
    """
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json"
    search_response = requests.get(search_url).json()
    search_results = search_response.get('query', {}).get('search', [])
    if not search_results:
        print(f"No results found for {query}")
        return

    page_title = search_results[0]['title']

    page_url = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    content = soup.find('div', {'class': 'mw-parser-output'})
    page_content = content.get_text() if content else ""
    
    with open(f"wikipedia_{page_title.replace('/', '_')}.txt", "w") as f:
        f.write(page_content)

    print(f"Article '{page_title}' saved to file.")