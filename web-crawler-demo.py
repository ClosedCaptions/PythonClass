from bs4 import BeautifulSoup
from selenium import webdriver


def find_google_doodle():
    url = 'https://www.google.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    code = driver.page_source
    driver.close()
    soup = BeautifulSoup(code, 'html.parser')
    # print(soup)
    line = soup.find('img')
    # print(line)
    print(line['alt'])
    print(url + line['src'])


def get_youtube_trending():
    url_two = 'https://www.youtube.com/feed/trending'
    driver_two = webdriver.Chrome()
    driver_two.get(url_two)
    code_two = driver_two.page_source
    # print(code_two)
    driver_two.close()
    soup_two = BeautifulSoup(code_two, 'html.parser')
    # print(soup_two)
    all_lines_two = soup_two.find_all('yt-formatted-string')
    # for obj in all_lines_two:
    #     print(obj)
    line_two = all_lines_two[4]
    # print(line_two)
    print(line_two.text)
    # all_lines_two = soup_two.find_all('a')
    line_two = soup_two.find('a', {'class', 'yt-simple-endpoint style-scope yt-formatted-string'})
    # print(sth)
    print(line_two.text)
    line_two = soup_two.find(id='video-title')
    print(line_two)
    print('https://www.youtube.com' + line_two['href'])


def switch_prices():
    url = 'https://www.bestbuy.ca/en-ca/collection/nintendo-switch/193142?icmp=mdot_vg_shopby_desc_nintendo_switch_console'
    driver = webdriver.Chrome()
    driver.get(url)
    code_three = driver.page_source
    driver.close()
    soup = BeautifulSoup(code_three, 'html.parser')
    objs = soup.find_all('div', {'class', 'col-xs-8_1VO-Q col-sm-12_1kbJA productItemTextContainer_HocvR'})
    # print(objs)
    for obj in objs:
        # print(obj)
        line = obj.find('div', {'class', 'productItemName_3IZ3c'})
        txt = line.text
        print(txt)
        line = obj.find('span', {'class', 'screenReaderOnly_3anTj large_3aP7Z'})
        txt = line.text
        print(txt)
        # break


switch_prices()
get_youtube_trending()