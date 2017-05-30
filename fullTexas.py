import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup
from itertools import chain
from collections import defaultdict

page = requests.get('http://www.politico.com/2012-election/results/president/texas/')

soup = BeautifulSoup(page.text, "html.parser")
for body in soup("tbody"):
    body.unwrap()

tables = pd.read_html(str(soup), flavor="bs4")

pd.set_option('display.max_rows', len(tables[1]))
data = tables[1]

df2 = data.set_index("County")

asap = df2.loc[:, "Popular Vote"]
lst = []
for i in range(1016):
    lst.append(str(asap.ix[i,1]))
for i in range (762):
    lst.remove('nan')

for i in range(len(lst)):
    lst[i] = lst[i].replace(".0", "")
    lst[i] = int(lst[i])
#lst returns the vote counts for the top vote getter in each County
yuh = df2.loc[:, "% Popular Vote"]
gang = []
junk = []
for i in range(1016):
    gang.append(str(yuh.ix[i,1]))
    if i%4 == 0:
        junk.append(gang[i])
gang.pop(0)
junk.pop(0)
for i in range(len(junk)):
    hoo = junk[i]
    gang.remove(hoo)
n = 3
k = 0
#gang is a list of all of the votes cast organized by county but all in one list
arry= []
for i in range(len(lst)):
    hunt = str(lst[i])
    j = gang[k:n]
    j.insert(0, hunt)
    arry.append(j)
    n = n+3
    k = k+3
log = range(1016)
oof = []
df1 = data.set_index("% Popular Vote")
new = df1.loc[:, "County"]
for i in log[0::4]:
    oof.append(new.ix[i,0])
for i in range(len(oof)):
    oof[i] = oof[i].replace(" 100.0% Reporting", "")
#oof is a list of the counties in texas
lparty = []
for i in log[0::4]:
    party = df1.loc[:, "Party"]
    lparty.append(party.ix[i,0])
page2 = requests.get('https://en.wikipedia.org/wiki/List_of_Texas_locations_by_per_capita_income')
soup2 = BeautifulSoup(page2.text, "html.parser")
for body in soup2("body"):
    body.unwrap()

tables2 = pd.read_html(str(soup2), flavor="bs4")
data2 = tables2[1]
df3 = data2.dropna().set_index(0)
df4 = df3.loc[:, 3]
df04 = df3.loc[:, 1]
median_list = []
real_medians = []
for i in range (1, 255):
    median_list.append(str(df4.ix[i,1]))
for i in range(len(median_list)):
    median_list[i] = median_list[i].replace("$", "")
    median_list[i] = median_list[i].replace(",", "")
    median_list[i] = int(median_list[i])
    real_medians.append([str(df04.ix[i+1,1]), median_list[i], lparty[i]])
smedians = sorted(real_medians)

here = []
clinton_percent_list = []
trump_percent_list = []
for i in range(len(arry)):
    for k in range(4):
        arry[i][k] = int(arry[i][k])
    hank = sum(arry[i])
    smedians[i].append(hank)
    if smedians[i][2] == "GOP":
        trump_percent = int(arry[i][0])/float(hank)
        clinton_percent = int(arry[i][1])/float(hank)
    elif smedians[i][2] == "Dem":
        clinton_percent = int(arry[i][0])/float(hank)
        trump_percent = int(arry[i][1])/float(hank)
    trump_percent_list.append(trump_percent)
    clinton_percent_list.append(clinton_percent)

pge = requests.get('https://www.tsl.texas.gov/ref/abouttx/popcnty201011.html')

sup = BeautifulSoup(pge.text, "html.parser")
for body in sup("body"):
    body.unwrap()

tbles = pd.read_html(str(sup), flavor="bs4")

pd.set_option('display.max_rows', len(tbles[0]))
dta = tbles[0]

population2012 = []
percentage2012 = []
dta0 = dta.set_index(0).sort_index()
dta1 = dta0.loc[:, 3]
for i in range(255):
    population2012.append(str(dta1.ix[i, 1]))
population2012.remove("7/1/2012")
for i in range(len(population2012)):
    population2012[i] = int(population2012[i])
    perc = smedians[i][3]/float(population2012[i])
    smedians[i].append(100*float(perc))
#smedians is a list of lists with the first value in each list being the
    #county name, second being the median income, third being which party
    #won, fourth being the votes cast in that county

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


total_list = []
GF = 0 #Gained Voters and Flipped
LF = 0 #Lost Voters and FLipped
GNF = 0 #Gained Voters and no Flip
LNF = 0 #Lost Voters and no Flip
LIF = 0
GVHI = 0
LLIF = 0
FD = 0
FR = 0
FDL = 0
FRL = 0
LVLI = 0
LVHI = 0
GVLI = 0
LP = 0
LV = 0
for i in range(len(smedians)):
    perc_change = smedians3[i][3] - smedians[i][4]
    difference = smedians3[i][2] - smedians[i][3]
    if perc_change < 0:
        LP = LP + 1
    else:
        pass
    if difference > 0:
        if smedians[i][1] > 46876:
            GVHI = GVHI + 1
        else:
            GVLI = GVLI +1
    else:
        LV = LV + 1
        if smedians[i][1] < 46876:
            LVLI = LVLI +1
        else:
            LVHI = LVHI + 1
    if who_won_list3[i] == smedians[i][2]:
        flip = "No Flip"
        if smedians3[i][2] > smedians[i][3]:
            GNF = GNF + 1
        #    flip = "Gained Voters and No Flip"
        else:
            LNF = LNF + 1
        #    flip = "Lost Voters and No Flip"
    else:
        flip = "Flipped"
        if who_won_list3[i] == "Dem":
            #Flippped to Dem
            FD = FD + 1
        else:
            #Flipped to GOP
            FR = FR + 1
        if smedians3[i][2] > smedians[i][3]:
            GF = GF + 1
        #    flip = "Gained Voters and Flipped"
        else:
            LF = LF + 1
        #    flip = "Lost Voters and Flipped"
            if who_won_list3[i] == "Dem":
                #Flippped to Dem and Lost Voters
                FDL = FDL + 1
            else:
                #Flipped to GOP and Lost Voters
                FRL = FRL + 1
            if smedians[i][1] < 46876: #median income for incomes of wisconsin counties
                LLIF = LLIF + 1
        if smedians[i][1] < 46876: #median income for incomes of wisconsin counties
            LIF = LIF + 1
    total_list.append([oof[i], difference, flip, smedians[i][1], perc_change])
print (total_list)
print ("Lost Voters and No flip: ", LNF)
print ("Gained Voters and No flip: ", GNF)
print ("Lost Voters and Flipped: ", LF)
print ("Gained Voters and Flipped: ", GF)
print ("Low Income Counties that Flipped: ", LIF)
print ("Low Income Counties that Flipped and Lost Voters: ", LLIF)
print ("Gained Voters and High Income: ", GVHI)
print ("Lost Voters and High Income: ", LVHI)
print ("Lost Voters and Low Income: ", LVLI)
print ("Gained Voters and Low Income: ", GVLI)
print ("Flipped Dem: ", FD)
print ("Flipped GOP: ", FR)
print ("Flipped Dem and Lost Voters: ", FDL)
print ("Flipped GOP and Lost Voters: ", FRL)
print ("Lower Percentage of Voters: ", LP)
print ("Lost Voters: ", LV)
#figure out how to determine if it is a substantial number of voters lost and incoroporate it
#also incorporate percentages lost by candidates when voters increased and decreased
