import requests
import praw
from bs4 import BeautifulSoup as Bs


def injuries(timestamp):

    reddit = praw.Reddit(client_id="",
                         client_secret="",
                         password="",
                         user_agent="",
                         username="")

    widgets = reddit.subreddit("lcfc").widgets

    url = "https://www.premierinjuries.com/injury-table.php"
    page = requests.get(url)
    source_string = "[Source](" + url + ")"

    soup = Bs(page.content, "lxml")
    results = soup.find_all(class_="player-row team_10")
    thetable = "**Player**|**Injury**|**Detail**\n:--|:--|:--:"

    for i in range(len(results)):
        name = (str(results[i]).split("Player</div>")[1].split('</td')[0]).split(' ')[-1]
        reason = str(results[i]).split("Reason</div>")[1].split('</td')[0]
        detail = str(results[i]).split("Detail</div>")[1].split('</td')[0]
        thetable += "\n" + "| " + str(name) + " | " + "*" + str(reason) + "*" + " | " + str(detail) + " |"

    save = '\n\n'.join([thetable, source_string, timestamp])
    print("\nInserting following table to sidebar:\n")
    print(save)
    widgets.sidebar[7].mod.update(text=save)
