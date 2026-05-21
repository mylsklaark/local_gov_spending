# Ingestion script: downloads OCC spending CSVs and loads them into DuckDB
import requests
import pathlib
from bs4 import BeautifulSoup
import openpyxl

def get_headings(headings):
    spend_headings = []
    for h in headings:
        if "monthly spending" in h.text.lower():
            spend_headings.append(h)
    return spend_headings

def get_urls(spend_headings):
    urls = []
    for h in spend_headings:
            ul = h.find_next_sibling("ul")
            for a in ul.find_all("a"):
                href = a.get("href")
                if href.endswith(".xlsx"):
                    link = "https://www.oxfordshire.gov.uk" + href
                    urls.append(link)
    return urls

def download_files(urls):
    path = pathlib.Path(__file__).parent / "data"
    path.mkdir(exist_ok=True)
    for url in urls:
        filename = url.split("/")[-1]
        response = requests.get(url)
        with open(path / filename, "wb") as f:
            f.write(response.content)
            
def main():
    url = "https://www.oxfordshire.gov.uk/council/about-your-council/council-tax-and-finance/financial-transparency"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    headings = soup.find_all("h3")
    spend_headings = get_headings(headings)
    urls = get_urls(spend_headings)
    download_files(urls)
    
if __name__ == "__main__":
    main()