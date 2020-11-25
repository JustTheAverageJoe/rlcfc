import requests
import praw
from bs4 import BeautifulSoup as Bs


def topscorers(update_time):
    
    reddit = praw.Reddit(client_id="",
                         client_secret="",
                         password="",
                         user_agent="",
                         username="")

    widgets = reddit.subreddit("lcfc").widgets

    mastDict = {}

    url = "https://fbref.com/en/squads/a2d435b3/Leicester-City-Stats"
    page = requests.get(url)
    source_string = "[Source](" + url + ")"

    soup = Bs(page.content, "html5lib")
    results = soup.find(id='div_stats_standard_10728')

    block = results.find_all('tbody')

    players = block[0].find_all('tr')
    for i in range(len(players)-1):
        name = str(players[i]).split("data-append-csv=")[1].split('"')[1].split("-")[1]
        goals = int(str(players[i]).split('goals">')[1].split("<")[0])
        assists = int(str(players[i]).split('assists">')[1].split("<")[0])
        games = -int(str(players[i]).split('games">')[1].split("<")[0])

        if goals != 0:
            mastDict[name] = [goals, assists, games]
        elif assists != 0:
            mastDict[name] = [goals, assists, games]

    sortMastDict = {k: v for k, v in sorted(mastDict.items(), key=lambda item: item[1], reverse=True)}

    for key in sortMastDict:
        sortMastDict[key][2] = -sortMastDict[key][2]

    thetable = "\#|P|G|A|MP\n:--|:--|:--:|:--:|:--:|:--:\n"
    i = 0
    for key in sortMastDict:
        thetable += "| " + str(i+1) + " | " + str(key) + " | " + str(sortMastDict.get(key)[0]) + " | " + str(sortMastDict.get(key)[1]) + " | " + str(sortMastDict.get(key)[2]) + "\n"
        i += 1
    save = '\n\n'.join([thetable, source_string, update_time])
    print("\nInserting following table to sidebar:\n")
    print(save)
    widgets.sidebar[6].mod.update(text=save)
