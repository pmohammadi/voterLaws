import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/United_States_presidential_election,_2012')

soup = BeautifulSoup(page.text, "html.parser")
for body in soup("tbody"):
    body.unwrap()

tables = pd.read_html(str(soup), flavor="bs4")

pd.set_option('display.max_rows', len(tables[1]))
data = tables[14]

df2 = data.set_index(0)
asap = df2.loc[:, 2]
huh = df2.loc[:, 5]
totals_df = df2.loc[:, 19]
dem_raw_votes = []
dem_perc = []
gop_raw_votes = []
gop_perc = []
allthevotes = []
therange = range(2, 53)
for i in therange: #54 would also include us totals
    dem_raw_votes.append(str(asap.ix[i,1])) #obama raw votes
    gop_raw_votes.append(str(huh.ix[i,1]))
    allthevotes.append(str(totals_df.ix[i,1]))

pge = requests.get('http://www.governing.com/gov-data/state-census-population-migration-births-deaths-estimates.html')

sup = BeautifulSoup(pge.text, "html.parser")
for body in sup("tbody"):
    body.unwrap()

tbles = pd.read_html(str(sup), flavor="bs4")

pd.set_option('display.max_rows', len(tbles[1]))
dta = tbles[1]

df3 = dta.set_index('2011 Estimate')
state_df = df3.loc[:, 'Name']
state_place = []
population2012_df = df3.loc[:, '2012 Estimate']
population2012 = []

for i in range(51):
    state_place.append(str(state_df.iloc[i]))
    population2012.append(str(population2012_df.iloc[i]))

us2012totals = []
for i in range(len(population2012)):
    gop_raw_votes[i] = int(gop_raw_votes[i])
    dem_raw_votes[i] = int(dem_raw_votes[i])
    allthevotes[i] = int (allthevotes[i])
    population2012[i] = int(population2012[i])
    gop_perc.append((gop_raw_votes[i]/float(population2012[i]))*float(100))
    dem_perc.append((dem_raw_votes[i]/float(population2012[i]))*float(100))
    if gop_raw_votes[i] > dem_raw_votes[i]:
        winner = 'GOP'
    else:
        winner = "Dem"
    state_perc = (allthevotes[i]/float(population2012[i]))*float(100)
    us2012totals.append([state_place[i], winner, allthevotes[i], state_perc])
print (state_place)
#print (us2012totals)
#US2012totals is a list of lists where in each list item 1 is the state name,
    #item 2 is the party that won the state in the presedential race, item 3 is
    #the total number of votes in the state, item 4 is the turnout percentage
