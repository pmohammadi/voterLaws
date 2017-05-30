import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup

page3 = requests.get('https://en.wikipedia.org/wiki/United_States_presidential_election_in_Wisconsin,_2016')

soup3 = BeautifulSoup(page3.text, "html.parser")
for body in soup3("body"):
    body.unwrap()

tables3 = pd.read_html(str(soup3), flavor="bs4")

pd.set_option('display.max_rows', len(tables3))
data3 = tables3[14]

df32 = data3.set_index(1)
asap3 = df32.loc[:, 0]
juju3 = df32.loc[:, 7]
oof3 = []
hi3 = range(146)
for i in hi3[2::2]:
    oof3.append(str(asap3.ix[i,1]))
#oof is a sorted list of the counties in WI

trump_votes3 = []
clinton_votes3 = []
trump_df3 = df32.loc[:, 2]
clinton_df3 = df32.loc[:, 3]
who_won_list3 = []
clinton_percent_list3 = []
trump_percent_list3 = []
total_votes3 = []
smedians3 = []
for i in hi3[2::2]:
    total_votes3.append(str(juju3.ix[i,1]).replace(".0", ""))
for i in hi3[2::2]:
    trump_votes3.append(str(trump_df3.ix[i,1]))
    clinton_votes3.append(str(clinton_df3.ix[i,1]))
for i in range(len(clinton_votes3)):
    clinton_votes3[i] = int(clinton_votes3[i])
    trump_votes3[i] = int(trump_votes3[i])
    if trump_votes3[i] > clinton_votes3[i]:
        who_won_list3.append("GOP")
    else:
        who_won_list3.append("Dem")
    trump_percent3 = int(trump_votes3[i])/float(int(total_votes3[i]))
    trump_percent_list3.append(trump_percent3)
    clinton_percent3 = int(clinton_votes3[i])/float(int(total_votes3[i]))
    clinton_percent_list3.append(clinton_percent3)
    smedians3.append([oof3[i], who_won_list3[i], int(total_votes3[i])])


pge3 = requests.get('https://www.wisconsin-demographics.com/counties_by_population')

sup3 = BeautifulSoup(pge3.text, "html.parser")
for body in sup3("body"):
    body.unwrap()

tbles3 = pd.read_html(str(sup3), flavor="bs4")

pd.set_option('display.max_rows', len(tbles3[0]))

dta3  = tbles3[0]
jinx3 = dta3.set_index(1).sort_index()
jinx4 = jinx3.loc[:, 2]
population2016 = []
for i in range(73):
    population2016.append(str(jinx4.ix[i,1]))
population2016.remove("Population")
for i in range(len(population2016)):
    population2016[i] = int(population2016[i])
    perc3 = smedians3[i][2]/float(population2016[i])
    smedians3[i].append(100*float(perc3))
print (smedians3)
#print (smedians3)
#smedians3 is a list of lists with the first value in each list being the county
    #name,second being which party won, third being the votes cast in that county,
    #fourth being the percentage of people that voted
