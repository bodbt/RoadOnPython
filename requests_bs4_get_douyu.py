import requests
from bs4 import BeautifulSoup

url='https://www.douyu.com/directory/game/How'
r = requests.get(url, verify=False)
content = r.content

#print(content)

soup = BeautifulSoup(content, "lxml")

live_list = soup.find_all("li", attrs={'data-cid' : True})

game_list = []

try:
    for i in live_list:
    #print(i)

        all_game = i.find('a')
        #print(all_game)

        game_count = all_game.find('span', attrs = {'class' : 'dy-num fr'}).text
        #print(game_count)

        if '万' in game_count:
            game_count = float(game_count[0:-1]) * 10000

        if float(game_count) > 8000:
            game_link = 'https;//www.douyu.com/' + all_game['href']
            game_title = all_game['title']
            game_picture = all_game.find('img')['data-original']
            game_nickname = all_game.find('span', attrs = {'class' : 'dy-name ellipsis fl'}).text

        game_dic = {}
        game_dic['game_link'] = game_link
        game_dic['game_title'] = game_title
        game_dic['game_picture'] = game_picture
        game_dic['game_nickname'] = game_nickname
        game_dic['game_count'] = game_count
        game_list.append(game_dic)
except:
    print("exception!")
else:
    print("analyzing finished...")
    output_flag = True

if output_flag:
    print(game_list)