import requests
from lxml import html

shots_url = 'http://stats.nba.com/stats/playerdashptshotlog?'+ \
            'DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&' + \
            'Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&' + \
            'PlayerID=202322&Season=2014-15&SeasonSegment=&' + \
            'SeasonType=Regular+Season&TeamID=0&VsConference=&VsDivision='

cisco_url = 'https://tools.cisco.com/security/center/productBoxData.x?prodType=NONCISCO'

sectrk_url = 'http://securitytracker.com/id/1036999'

# request the URL and parse the JSON
response = requests.get(sectrk_url)
response.raise_for_status() # raise exception if invalid response
#shots = response.json()['resultSets'][0]['rowSet']
shots = html.fromstring(response.content)

# do whatever we want with the shots data
print(shots)
