import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup

page3 = requests.get('https://en.wikipedia.org/wiki/United_States_presidential_election,_2016')

soup3 = BeautifulSoup(page3.text, "html.parser")
for body in soup3("body"):
    body.unwrap()

tables3 = pd.read_html(str(soup3), flavor="bs4")

pd.set_option('display.max_rows', len(tables3))
data3 = tables3[30]
df32 = data3.set_index(3)
asap3 = df32.loc[:, 0]
juju3 = df32.loc[:, 2]
boop3 = df32.loc[:, 5]
totals_df3 = df32.loc[:, 22]
therange3 = range(2,58)
state_place3 = []
dem_raw_votes3 = []
gop_raw_votes3 = []
allthevotes3 = []
dem_perc3 = []
gop_perc3 = []
for i in therange3:
    state_place3.append(str(asap3.ix[i, 1]))
#(state_place3.index('Maine, 2nd')) #Maine is from 19 to 21
#(state_place3.index('Nebraska (at-lrg)')) #Nebraska is from 29 to 32
    dem_raw_votes3.append(str(juju3.ix[i, 1]))
    gop_raw_votes3.append(str(boop3.ix[i, 1]))
    allthevotes3.append(str(totals_df3.ix[i, 1]))
del dem_raw_votes3[32]
del dem_raw_votes3[31]
del dem_raw_votes3[30]
del dem_raw_votes3[21]
del dem_raw_votes3[20]
del gop_raw_votes3[32]
del gop_raw_votes3[31]
del gop_raw_votes3[30]
del gop_raw_votes3[21]
del gop_raw_votes3[20]
del allthevotes3[32]
del allthevotes3[31]
del allthevotes3[30]
del allthevotes3[21]
del allthevotes3[20]
del state_place3[32]
del state_place3[31]
del state_place3[30]
del state_place3[21]
del state_place3[20]

pge3 = requests.get('https://dilemma-x.net/2016/12/21/u-s-state-populations-2016-most-populous-states/')

sup3 = BeautifulSoup(pge3.text, "html.parser")
for body in sup3("body"):
    body.unwrap()

tbles3 = pd.read_html(str(sup3), flavor="bs4")

pd.set_option('display.max_rows', len(tbles3[0]))

dta3  = tbles3[4]

thebasic_df = dta3.set_index(0)
thepop_df = thebasic_df.loc[:, 2]
state_pop2016 = []

us2016totals = []
therange32 = range(6,57)
for i in therange32:
    state_pop2016.append(str(thepop_df.ix[i, 1]))
for i in range(len(state_pop2016)):
    gop_raw_votes3[i] = int(gop_raw_votes3[i])
    dem_raw_votes3[i] = int(dem_raw_votes3[i])
    allthevotes3[i] = int (allthevotes3[i])
    state_pop2016[i] = int(state_pop2016[i])
    gop_perc3.append((gop_raw_votes3[i]/float(state_pop2016[i]))*float(100))
    dem_perc3.append((dem_raw_votes3[i]/float(state_pop2016[i]))*float(100))
    if gop_raw_votes3[i] > dem_raw_votes3[i]:
        winner = 'GOP'
    else:
        winner = "Dem"
    state_perc3 = (allthevotes3[i]/float(state_pop2016[i]))*float(100)
    state_place3[i] = state_place3[i].replace(" (at-lrg)", "")
    state_place3[i] = state_place3[i].replace(" (at-large)", "")
    us2016totals.append([state_place3[i], winner, allthevotes3[i], state_perc3])
#print (us2016totals)
#us2016totals is a list of lists where in each list item 1 is the state name,
    #item 2 is the party that won the state in the presedential race, item 3 is
    #the total number of votes in the state, item 4 is the turnout percentage
