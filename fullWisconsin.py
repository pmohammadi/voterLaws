import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.politico.com/2012-election/results/president/wisconsin/')

soup = BeautifulSoup(page.text, "html.parser")
for body in soup("tbody"):
    body.unwrap()

tables = pd.read_html(str(soup), flavor="bs4")

pd.set_option('display.max_rows', len(tables[1]))
data = tables[1]

df2 = data.set_index("County")
asap = df2.loc[:, "Popular Vote"]
lst = []
for i in range(504):
    lst.append(str(asap.ix[i,1]))
for i in range (432):
    lst.remove("nan")
for i in range(len(lst)):
    lst[i] = lst[i].replace(".0", "")
    lst[i] = int(lst[i])
#lst returns the vote counts for the top vote getter in each County
yuh = df2.loc[:, "% Popular Vote"]
gang = []
junk = []
for i in range(504):
    gang.append(str(yuh.ix[i,1]))
    if i%7 == 0:
        junk.append(gang[i])
gang.pop(0)
junk.pop(0)
for i in range(len(junk)):
    hoo = junk[i]
    gang.remove(hoo)
n = 5
k = 0
#gang is a list of all of the votes cast organized by county but all in one list
arry= []
for i in range(len(lst)):
    hunt = str(lst[i])
    j = gang[k:n]
    j.insert(0, hunt)
    arry.append(j)
    n = n+6
    k = k+6
log = range(504)
oof = []
df1 = data.set_index("% Popular Vote")
new = df1.loc[:, "County"]
for i in log[0::7]:
    oof.append(new.ix[i,0])
for i in range(len(oof)):
    oof[i] = oof[i].replace(" 100.0% Reporting", "")
    oof[i] = oof[i].replace(" 94.4% Reporting", "")
    oof[i] = oof[i].replace(" 96.6% Reporting", "")
#oof is a sorted list of the counties in WI
lparty = []
for i in log[0::7]:
    party = df1.loc[:, "Party"]
    lparty.append(party.ix[i,0])

page2 = requests.get('https://en.wikipedia.org/wiki/List_of_Wisconsin_locations_by_per_capita_income')
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
for i in range (1, 73):
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
    for k in range(6):
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

pge = requests.get('http://www.us-places.com/Wisconsin/population-by-County.htm')

sup = BeautifulSoup(pge.text, "html.parser")
for body in sup("tbody"):
    body.unwrap()

tbles = pd.read_html(str(sup), flavor="bs4")

pd.set_option('display.max_rows', len(tbles[1]))
dta = tbles[1]

population2012 = []
percentage2012 = []
dta1 = dta.set_index(0).sort_index()
for i in range(73):
    population2012.append(str(dta1.ix[i,1]))
population2012.remove('Total Population')
for i in range(len(population2012)):
    population2012[i] = int(population2012[i])
    perc = smedians[i][3]/float(population2012[i])
    smedians[i].append(100*float(perc))

#smedians is a list of lists with the first value in each list being the county
    #name, second being the median income, third being which party won, fourth
    #being the votes cast in that county. All for 2012

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
#smedians3 is a list of lists with the first value in each list being the county
    #name,second being which party won, third being the votes cast in that county
    #for 2016

paper = requests.get('https://www.indexmundi.com/facts/united-states/quick-facts/Wisconsin/black-population-percentage#table')

tomato = BeautifulSoup(paper.text, "html.parser")
for body in tomato("body"):
    body.unwrap()

chair = pd.read_html(str(tomato), flavor="bs4")

pd.set_option('display.max_rows', len(chair[0]))
numbers = chair[0]
chair1 = numbers.set_index('County')
chair2 = numbers.set_index('Value')
blackp = []
for i in range(72):
    wone = str(chair1.ix[i,0])
    one = float(wone)
    blackp.append(one)

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
LPNF = 0
LPNFD = 0
LPNFG = 0
LPF = 0
LPFG = 0
LPFD = 0
GPF = 0
GPFG = 0
GPFD = 0
GPNF = 0
GPNFG = 0
GPNFD = 0
BGFG = 0
BGFD = 0
BGNFG = 0
BGNFD =0
NBGFG = 0
NBGFD = 0
NBGNFG = 0
NBGNFD =0
BLFG = 0
BLFD = 0
BLNFG = 0
BLNFD =0
NBLFG = 0
NBLFD = 0
NBLNFG = 0
NBLNFD =0
for i in range(len(smedians)):
    perc_change = smedians3[i][3] - smedians[i][4]
    difference = smedians3[i][2] - smedians[i][3]
    if perc_change < 0:
        LP = LP + 1
        if who_won_list3[i] == smedians[i][2]:
            LPNF = LPNF + 1
            if who_won_list3[i] == "GOP":
                LPNFG = LPNFG + 1
            else:
                LPNFD = LPNFD + 1
        else:
            LPF = LPF + 1
            if who_won_list3[i] == "GOP":
                LPFG = LPFG + 1
            else:
                LPFD = LPFD + 1
    else:
        if who_won_list3[i] == smedians[i][2]:
            GPNF = GPNF + 1
            if who_won_list3[i] == "GOP":
                GPNFG = GPNFG + 1
            else:
                GPNFD = GPNFD + 1
        else:
            GPF = GPF + 1
            if who_won_list3[i] == "GOP":
                GPFG = GPFG + 1
            else:
                GPFD = GPFD + 1
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
    if blackp[i] > 5.0:
        if perc_change > 0:
            if flip == "Flipped":
                if who_won_list3[i] == "GOP":
                    BGFG = BGFG + 1
                else:
                    BGFD = BGFD + 1
            else:
                if who_won_list3[i] == "GOP":
                    BGNFG = BGNFG + 1
                else:
                    BGNFD = BGNFD + 1
        else:
            if flip == "Flipped":
                if who_won_list3[i] == "GOP":
                    BLFG = BLFG + 1
                else:
                    BLFD = BLFD + 1
            else:
                if who_won_list3[i] == "GOP":
                    BLNFG = BLNFG + 1
                else:
                    BLNFD = BLNFD + 1
    else:
        if perc_change > 0:
            if flip == "Flipped":
                if who_won_list3[i] == "GOP":
                    NBGFG = NBGFG + 1
                else:
                    NBGFD = NBGFD + 1
            else:
                if who_won_list3[i] == "GOP":
                    NBGNFG = NBGNFG + 1
                else:
                    NBGNFD = NBGNFD + 1
        else:
            if flip == "Flipped":
                if who_won_list3[i] == "GOP":
                    NBLFG = NBLFG + 1
                else:
                    NBLFD = NBLFD + 1
            else:
                if who_won_list3[i] == "GOP":
                    NBLNFG = NBLNFG + 1
                else:
                    NBLNFD = NBLNFD + 1
    total_list.append([oof[i], difference, flip, smedians[i][1], perc_change, who_won_list3[i], blackp[i]])
by_blackp = sorted(total_list, key=lambda x: x[6])
#print (total_list)
print (by_blackp)
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
#####FIND PRECINCT VOTES IN MILWAUKEE AND WHO WAS VOTING AT each
###LOOK AT RACE OF SENATE AND HOUSE MEMBERS
###LOOK AT UNEMPLOYMENT NUMBERS ##NO REAL RELATIONS
##SEE IF I CAN WORK IN STATS INTO THIS
perc_change_list= []
for i in range(len(total_list)):
    perc_change_list.append(total_list[i][4])
    #make this more efficient to where it is for the whole state, not average of counties
average_perc_change = sum(perc_change_list)/float(72)
#print (average_perc_change) ####THIS IS WRONG

aa_counties = ['Milwaukee', 'Dane', 'Racine', 'Kenosha', 'Rock', 'Waukesha']
aa_counties_pop_2012 = 0
aa_counties_pop_2016 = 0
aa_counties_votes_2012 = 0
aa_counties_votes_2016 = 0
naa_counties_pop_2012 = 0
naa_counties_pop_2016 = 0
naa_counties_votes_2012 = 0
naa_counties_votes_2016 = 0
for i in range(len(total_list)):
    if total_list[i][0] in aa_counties:
        aa_counties_pop_2012 = aa_counties_pop_2012 + population2012[i]
        aa_counties_pop_2016 = aa_counties_pop_2016 + population2016[i]
        aa_counties_votes_2012 = aa_counties_votes_2012 + smedians[i][3]
        aa_counties_votes_2016 = aa_counties_votes_2016 + smedians3[i][2]
    else:
        naa_counties_pop_2012 = naa_counties_pop_2012 + population2012[i]
        naa_counties_pop_2016 = naa_counties_pop_2016 + population2016[i]
        naa_counties_votes_2012 = naa_counties_votes_2012 + smedians[i][3]
        naa_counties_votes_2016 = naa_counties_votes_2016 + smedians3[i][2]
aa_perc_2012 = aa_counties_votes_2012/float(aa_counties_pop_2012)
aa_perc_2016 = aa_counties_votes_2016/float(aa_counties_pop_2016)
aa_perc_diff = float(100)*(aa_perc_2016 - float(aa_perc_2012))
naa_perc_2012 = naa_counties_votes_2012/float(naa_counties_pop_2012)
naa_perc_2016 = naa_counties_votes_2016/float(naa_counties_pop_2016)
naa_perc_diff = (naa_perc_2016 - float(naa_perc_2012))*float(100)
aa_votes_lost_if_0 = (aa_counties_pop_2016*float(aa_perc_diff))/float(100)
print ("african american percentage change: ", aa_perc_diff)
print ("african american counties total population 2016: ", aa_counties_pop_2016)
print ("not african american percentage change: ", naa_perc_diff)
print ('votes lost in african american counties (if percentages had stayed the same): ', aa_votes_lost_if_0)
print ('votes lost in african american counties (if percentages had matched not african american counties): ', ((aa_counties_pop_2016*float(-naa_perc_diff))/float(100))+aa_votes_lost_if_0)
print ('votes lost in african american counties (if percentages had matched rest of country excluding WI): ', (aa_counties_pop_2016*float(-0.5911030981573233))/float(100) + aa_votes_lost_if_0)

print ("Lost percentage, no flip", LPNF)
print ("Lost percentage, no flip, stayed democratic", LPNFD)
print ("Lost percentage, no flip, stayed GOP", LPNFG)
print ("Lost percentage, flip", LPF)
print ("Lost percentage, flipped toward GOP", LPFG)
print ("Lost percentage, flipped toward Dem", LPFD)
print ("Gained percentage, flipped", GPF)
print ("Gained percentage, flipped towards GOP", GPFG)
print ("Gained percentage, flipped towards Dem", GPFD)
print ("Gained percentage, no flip", GPNF)
print ("Gained percentage, no flip, stayed GOP", GPNFG)
print ("Gained percentage, no flip, stayed Dem", GPNFD)
print ("AA Gained percentage flipped GOP", BGFG)
print ("AA Gained percentage flipped Dem", BGFD)
print ("AA Gained percentage no flip GOP", BGNFG)
print ("AA Gained percentage no flip Dem", BGNFD)
print ("Not AA Gained percentage flipped GOP", NBGFG)
print ("Not AA Gained percentage flipped Dem", NBGFD)
print ("Not AA Gained percentage no flip GOP", NBGNFG)
print ("Not AA Gained percentage no flip Dem", NBGNFD)
print ("AA Lost percentage flipped GOP", BLFG)
print ("AA Lost percentage flipped Dem", BLFD)
print ("AA Lost percentage no flip GOP", BLNFG)
print ("AA Lost percentage no flip Dem", BLNFD)
print ("Not AA Lost percentage flipped GOP", NBLFG)
print ("Not AA Lost percentage flipped Dem", NBLFD)
print ("Not AA Lost percentage no flip GOP", NBLNFG)
print ("Not AA Lost percentage no flip GOP", NBLNFD)
print (blackp)
