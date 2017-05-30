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
    state_perc = ((allthevotes[i]/float(population2012[i]))*float(100))
    us2012totals.append([state_place[i], winner, allthevotes[i], state_perc])
#print (us2012totals)
#US2012totals is a list of lists where in each list item 1 is the state name,
    #item 2 is the party that won the state in the presedential race, item 3 is
    #the total number of votes in the state, item 4 is the turnout percentage


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

us_full_lst = []
strict_id_laws = ["Georgia", "Indiana", "Kansas", "Mississippi", "Tennessee", "Virginia", "Wisconsin", "Arizona", "Ohio"]
similar_to_wi = ["Michigan", 'Minnesota', "Illinois"]
similar_lst = []
for i in range(len(us2016totals)):
    perc_change = us2016totals[i][3] - float(us2012totals[i][3])
    difference = us2016totals[i][2] - float(us2012totals[i][2])
    if us2012totals[i][1] == us2016totals[i][1]:
        flip = "No Flip"
    else:
        flip = "Flip"
    if state_place[i] in strict_id_laws:
        strict = "strict laws"
    else:
        strict = "not strict"
    hoo = [state_place[i], flip, strict, difference, perc_change]
    us_full_lst.append(hoo)
    #us_full_lst is a list of lists with item 1 being the state name, item 2 being
        #if the state flipped, item 3 being if the state has strict id_laws, item 4
        #being the difference in raw votes between 2016 and 2012, item 5 being the
        #change in voter turnout percentage between 2016 and 2012
    hoo.append(i)
    if state_place[i] in similar_to_wi:
        similar_lst.append(hoo)
rest_of_us_total_2012 = 0
rest_of_us_pop_2012 = 0
rest_of_us_pop_2016 = 0
rest_of_us_total_2016 = 0
for i in range(len(population2012)):
    rest_of_us_pop_2012 = rest_of_us_pop_2012 + population2012[i]
    rest_of_us_total_2012 = rest_of_us_total_2012 + us2012totals[i][2]
    rest_of_us_pop_2016 = rest_of_us_pop_2016 + state_pop2016[i]
    rest_of_us_total_2016 = rest_of_us_total_2016 + us2016totals[i][2]
rest_of_us_pop_2012 = rest_of_us_pop_2012 - population2012[49]
rest_of_us_total_2012 = rest_of_us_total_2012 - us2012totals[49][2]
rest_of_us_pop_2016 = rest_of_us_pop_2016 - state_pop2016[49]
rest_of_us_total_2016 = rest_of_us_total_2016 - us2016totals[49][2]
rest_perc_2012 = rest_of_us_total_2012/float(rest_of_us_pop_2012)
rest_perc_2016 = rest_of_us_total_2016/float(rest_of_us_pop_2016)
rest_perc_change = (float(rest_perc_2016) - float(rest_perc_2012))*float(100)
rest_total_change =  rest_of_us_total_2016 - float(rest_of_us_total_2012)
print (us_full_lst)
similar_pop_2012 = 0
similar_total_2012 = 0
similar_pop_2016 = 0
similar_total_2016 = 0
for i in range(len(similar_lst)):
    where = int(similar_lst[i][5])
    similar_pop_2012 = similar_pop_2012 + population2012[where]
    similar_pop_2016 = similar_pop_2016 + state_pop2016[where]
    similar_total_2012 = similar_total_2012 + us2012totals[similar_lst[i][5]][2]
    similar_total_2016 = similar_total_2016 + us2016totals[similar_lst[i][5]][2]
similar_perc_2012 = similar_total_2012/float(similar_pop_2012)
similar_perc_2016 = similar_total_2016/float(similar_pop_2016)
similar_perc_change = (float(similar_perc_2016) - float(similar_perc_2012))*float(100)
similar_total_change = similar_total_2016 - float(similar_total_2012)
print ("states similar to wisconsin changed this percent:", similar_perc_change) #states most similar w/o voter ID laws
print ("rest of US excluding WI changed this percent: ", rest_perc_change)
wayne_county_2016_votes = 517842 + 228908 + 18787 + 7764 + 1714 + 435
wayne_county_2012_votes = 595253 + 213586 + 2748 + 1832 + 689
wayne_county_2016_pop = 1749366
wayne_county_2012_pop = 1792514
wayne_county_2012_perc = wayne_county_2012_votes/float(wayne_county_2012_pop)
wayne_county_2016_perc = wayne_county_2016_votes/float(wayne_county_2016_pop)
wayne_county_diff = (float(wayne_county_2016_perc) - float(wayne_county_2012_perc))*float(100)
print ("highest percent African American county in Michigan changed this percent: ", wayne_county_diff)
#https://www.indexmundi.com/facts/united-states/quick-facts/michigan/black-population-percentage#chart is the link for this data
#39.6% of Wayne County is black. Only Michigan county > 30%
#for illinois, Alexander, Pulaski, and St. Clair all above 30% black, Cook is big and 24.6% black
IL_2016_votes = 1496 + 1292 + 48 + 14 + 60756 + 53857 + 4181 + 1473 + 1675 + 962 + 55 + 20
IL_2016_pop = 262759 + 5619 + 6478
IL_2012_votes = 3501 + 3012 + 119827
IL_2012_pop = 5960 + 7752 + 268714
IL_2012_perc = IL_2012_votes/float(IL_2012_pop)
IL_2016_perc = IL_2016_votes/float(IL_2016_pop)
IL_perc_change = (float(IL_2016_perc) - float(IL_2012_perc))*float(100)
print ("highest percent African American counties in Illinois changed this percent: ", IL_perc_change)
#https://www.indexmundi.com/facts/united-states/quick-facts/Illinois/black-population-percentage#chart is the link for this data
#along with politico and website with populations
#Milwaukee as of 2013, was approximately 28% black, but for the other states, I only took counties that are > 30% black
sim_counties_2016_votes = 1496 + 1292 + 48 + 14 + 60756 + 53857 + 4181 + 1473 + 1675 + 962 + 55 + 20 + wayne_county_2016_votes
sim_counties_2016_pop = 262759 + 5619 + 6478 + wayne_county_2016_pop
sim_counties_2012_votes = 3501 + 3012 + 119827 + wayne_county_2012_votes
sim_counties_2012_pop = 5960 + 7752 + 268714 + wayne_county_2012_pop
sim_counties_2012_perc = sim_counties_2012_votes/float(sim_counties_2012_pop)
sim_counties_2016_perc = sim_counties_2016_votes/float(sim_counties_2016_pop)
sim_counties_perc_change = (float(sim_counties_2016_perc) - float(sim_counties_2012_perc))*float(100)
print ("highest percent African American counties in similar states counties changed this percent: ", sim_counties_perc_change)
