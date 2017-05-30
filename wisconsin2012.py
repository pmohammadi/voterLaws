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
print (smedians)
#smedians is a list of lists with the first value in each list being the county
    #name, second being the median income, third being which party won, fourth
    #being the votes cast in that county, fifth being the percentage that voted in the election
