import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup

page3 = requests.get('https://en.wikipedia.org/wiki/United_States_presidential_election_in_Texas,_2016')

soup3 = BeautifulSoup(page3.text, "html.parser")
for body in soup3("body"):
    body.unwrap()

tables3 = pd.read_html(str(soup3), flavor="bs4")

pd.set_option('display.max_rows', len(tables3))
data3 = tables3[25]

df32 = data3.set_index(7) #county is index
asap3 = df32.loc[:, 0] #countydf
juju3 = df32.loc[:, 11]
oof3 = []
for i in range(1, 255):
    oof3.append(str(asap3.ix[i,1]))
#oof is a sorted list of the counties in WI

trump_votes3 = []
clinton_votes3 = []
trump_df3 = df32.loc[:, 1]
clinton_df3 = df32.loc[:, 3]
who_won_list3 = []
clinton_percent_list3 = []
trump_percent_list3 = []
total_votes3 = []
smedians3 = []
for i in range(1, 255):
    total_votes3.append(str(juju3.ix[i,1]))
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
#print (smedians3)
#smedians3 is a list of lists with the first value in each list being the county
    #name,second being which party won, third being the votes cast in that county
pge3 = requests.get('https://www.texas-demographics.com/counties_by_population')

sup3 = BeautifulSoup(pge3.text, "html.parser")
for body in sup3("body"):
    body.unwrap()

tbles3 = pd.read_html(str(sup3), flavor="bs4")

pd.set_option('display.max_rows', len(tbles3[0]))
dta3 = tbles3[0]
jinx3 = dta3.set_index(1).sort_index()
jinx4 = jinx3.loc[:, 2]
population2016 = []
for i in range(255):
    population2016.append(str(jinx4.ix[i,1]))
population2016.remove("Population")
population2016.insert(25, "17760")
population2016.remove("nan")
for i in range(len(population2016)):
    population2016[i] = int(population2016[i])
    perc3 = smedians3[i][2]/float(population2016[i])
    smedians3[i].append(100*float(perc3))
print (smedians3)

#####LOOK AT VOTER TURNOUT PERCENTAGE INSTEAD OF JUST RAW NUMBERS
#####LOW, MIDDLE, and HIGH INCOME FOR INCOME DATAS
