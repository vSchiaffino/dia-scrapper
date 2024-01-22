import requests
from bs4 import BeautifulSoup

def scrap_dia_kg(url):
    # TODO handle errors
    response = requests.get(url)
    raw_html = response.content.decode('utf-8')
    soup = BeautifulSoup(raw_html, 'html.parser')
    elements = soup.find_all("span", "vtex-product-specifications-1-x-specificationValue vtex-product-specifications-1-x-specificationValue--first vtex-product-specifications-1-x-specificationValue--last")
    if(len(elements) == 0):
        raise Exception("failed scraping " + url)

    element = elements[0]
    price = element["data-specification-value"]



    return float(price)


if __name__ == "__main__":
    import sys
    print(scrap_dia_kg(sys.argv[1]))