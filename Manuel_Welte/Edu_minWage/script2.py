import pandas as pd

edu_df = pd.read_csv("ressources/education.csv")
index_df = pd.read_csv("ressources/nameCodeIndex.csv", comment="#")
hap_2015 = pd.read_csv("ressources/2015.csv")
health_2015_df = pd.read_csv("ressources/pop_public_healthcare.csv")
min_wage_2015_df = pd.read_csv("ressources/minimum_wages_pppusd.csv")
poverty_df=pd.read_csv("ressources/POVERTY.csv")
new_df = pd.DataFrame()

new_df["LOCATION"] = edu_df[(edu_df["TIME"] == 2015) & (edu_df["SUBJECT"] == "PUB")]["LOCATION"]



#fillna() setzt den Wert der verwendet wird falls keine richtige Zahl gefunden wird
#normalerweise "nan", hier setzte ich ihn auf -1
new_df["EDU_PUB"] = edu_df[(edu_df["TIME"] == 2015) & (edu_df["SUBJECT"] == "PUB")]["Value"].fillna(-1).round(3)

priv_2015 = []
for loc in new_df["LOCATION"]:
    priv_2015.append(
        edu_df[(edu_df["TIME"] == 2015) & (edu_df["SUBJECT"] == "PRIV") & (edu_df["LOCATION"] == loc)]["Value"].iloc[0])

#resettet index auf zahlen 0-n
#normalerweise macht er das automatisch weiß nicht warum nicht hier
new_df = new_df.reset_index(drop=True)

new_df["EDU_PRIV"] = pd.Series(priv_2015).fillna(-1).round(3)

health_2015 = []
for loc in new_df["LOCATION"]:
    x = health_2015_df[(health_2015_df["COU"] == loc) & (health_2015_df["Year"] == 2015)]["Value"]
    if (len(x) > 0):
        health_2015.append(x.iloc[0])
    else:
        health_2015.append(-1)
new_df["PUB_HEALTHCARE"] = pd.Series(health_2015).round(3)

mwages_2015 = []
for loc in new_df["LOCATION"]:
    x = min_wage_2015_df[(min_wage_2015_df["COUNTRY"] == loc) & (min_wage_2015_df["TIME"] == 2015)]["Value"]
    if (len(x) > 0):
        mwages_2015.append(x.iloc[0])
    else:
        mwages_2015.append(-1)
new_df["MIN_WAGE"] = pd.Series(mwages_2015).round(3)
l_2015 = []

pov_filtered = poverty_df[(poverty_df["TIME"] == 2015) & (poverty_df["SUBJECT"] == "TOT")]
l_pov_2015 = []
for loc in new_df["LOCATION"]:
    x = pov_filtered[pov_filtered["LOCATION"] == loc]["Value"]
    if (len(x) > 0):
        l_pov_2015.append(round(x.iloc[0], 3))
    else:
        l_pov_2015.append(-1)
new_df["POV_VALUE_2015"] = pd.Series(l_pov_2015).astype(float)


for c_code in new_df["LOCATION"]:
    found = False
    for index_code in index_df["code"]:
        if index_code == c_code:
            x = index_df[index_df["code"] == index_code]["country"].iloc[0]
            y = round(hap_2015[hap_2015["Country"] == x]["Happiness Score"].iloc[0], 3)
            l_2015.append(y)
            found = True
    if not found:
        l_2015.append(-1)

new_df["HAP_2015"] = pd.Series(l_2015)
c_l=[]

for l in new_df["LOCATION"]:
    x=index_df[index_df["code"]==l]["country"]
    if(len(x))>0:
        c_l.append(x.iloc[0])
    else:
        c_l.append(-1)
new_df["CNAME"]=pd.Series(c_l)
new_df.to_csv("output/edu_hlthcare_minwage.csv", index=False)
