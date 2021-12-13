from bs4 import BeautifulSoup
import requests
from requests.api import head

li = []
html_text = requests.get('https://www.youtube.com/playlist?list=PLirAqAtl_h2r5g8xGajEwdXd3x1sZh8hC').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
# print(soup)
# headlines = soup.find('div',class_ = "style-scope ytd-playlist-video-renderer")
# print(headlines)
# a = headlines.find('div', class_ = "style-scope ytd-app")
# print(a)
# for headline in headlines:
# #     title = headline.find('a',class_ = "yt-simple-endpoint style-scope ytd-playlist-video-renderer").text
# #     # for char in score:
#     #     print(char)
#     #     if(char.isdigit()==True):
#     #         print(char)            
# print(headlines)
# print("")
# //*[@id="contents"]/ytd-playlist-video-renderer[1]
for i, tr in enumerate(soup.select('tr.pl-video')):
    print('{}. {}'.format(i + 1, tr['data-title']))
    print('https://www.youtube.com' + tr.a['href'])
    print('-' * 80)