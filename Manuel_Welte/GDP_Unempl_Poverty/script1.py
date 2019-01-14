import pandas as pd

gdp_df = pd.read_csv("ressources/GDP.csv")
poverty_df = pd.read_csv("ressources/POVERTY.csv")
unempl_df = pd.read_csv("ressources/UNEMPLOYMENT.csv")

###### country_codes.csv => codes.csv#####
codes = pd.read_csv("ressources/country_codes.csv")
codes_country_names = codes["Country or Area"]
codes_country_codes = codes["ISO-alpha3 Code"]
new_df = pd.DataFrame()
new_df["Country or Area"] = codes_country_names
new_df["Code"] = codes_country_codes
new_df.to_csv("ressources/codes.csv", index=False)

# nameCodeIndex.csv erstellen(hap_name->country_code)
hap_2015 = pd.read_csv("ressources/2015.csv")
hap_2015_country_names = hap_2015["Country"]
hap_2016 = pd.read_csv("ressources/2016.csv")
hap_2016_country_names = hap_2016["Country"]
index = pd.DataFrame()
index["country"] = hap_2016_country_names
codeList = []
'''
for name in hap_country_names:
    col = codes[codes["Country or Area"] == name]["ISO-alpha3 Code"]
    l = col.tolist()
    if len(l) is not 0:
        codeList.append(l[0])
    else:
        codeList.append("NONE")
index["code"] = pd.Series(codeList).astype(str)
index.to_csv("output/nameCodeIndexTest.csv", index=False)
print(index[index["code"]=="null"])
'''

index_df = pd.read_csv("output/nameCodeIndex.csv", comment="#")

# happiness score 2016 anfügen
l_2016 = []
for gdp_code in gdp_df["LOCATION"]:
    found = False
    for index_code in index_df["code"]:
        if index_code == gdp_code:
            x = index_df[index_df["code"] == index_code]["country"].iloc[0]
            y = round(hap_2016[hap_2016["Country"] == x]["Happiness Score"].iloc[0], 3)
            l_2016.append(y)
            found = True
    if not found:
        l_2016.append(-1)




# happiness 2015 anfügen
l_2015 = []
for gdp_code in gdp_df["LOCATION"]:
    found = False
    for index_code in index_df["code"]:
        if index_code == gdp_code:
            x = index_df[index_df["code"] == index_code]["country"].iloc[0]
            y = round(hap_2015[hap_2015["Country"] == x]["Happiness Score"].iloc[0], 3)
            l_2015.append(y)
            found = True
    if not found:
        l_2015.append(-1)


new_df = pd.DataFrame()
new_df["LOCATION"] = gdp_df["LOCATION"]

l_c = []
for gdp_code in new_df["LOCATION"]:
    found = False
    for index_code in index_df["code"]:
        if index_code == gdp_code:
            l_c.append(index_df[index_df["code"]==index_code]["country"].iloc[0])
            print(index_df[index_df["code"]==index_code]["country"].iloc[0])
            print(index_code)
            print("\n\n")
            found = True
    if not found:
        l_c.append(-1)
new_df["CNAME"]=pd.Series(l_c)
#new_df["YEAR"] = gdp_df["TIME"]
new_df["GDP_VALUE_2016"] = gdp_df["Value"].round(3)
new_df["HAP_VALUE_2015"] = pd.Series(l_2015).astype(float)
new_df["HAP_VALUE_2016"] = pd.Series(l_2016).astype(float)

# unemployment anfügen
l_unempl = []
for loc in new_df["LOCATION"]:
    x = unempl_df[unempl_df["LOCATION"] == loc]
    y = x[x["TIME"].str.contains("2016")]["Value"]
    if (len(y) > 0):
        l_unempl.append(round(y.iloc[0], 3))
    else:
        l_unempl.append(-1)
new_df["UNEMP_VALUE_2016"] = pd.Series(l_unempl).astype(float)

# Armutsrate 2014 anfügen, "TOT"=total
pov_filtered = poverty_df[(poverty_df["TIME"] == 2014) & (poverty_df["SUBJECT"] == "TOT")]
l_pov_2014 = []
for loc in new_df["LOCATION"]:
    x = pov_filtered[pov_filtered["LOCATION"] == loc]["Value"]
    if (len(x) > 0):
        l_pov_2014.append(round(x.iloc[0], 3))
    else:
        l_pov_2014.append(-1)

new_df["POV_VALUE_2014"] = pd.Series(l_pov_2014).astype(float)

# Armutsrate 2015 anfügen
pov_filtered = poverty_df[(poverty_df["TIME"] == 2015) & (poverty_df["SUBJECT"] == "TOT")]
l_pov_2015 = []
for loc in new_df["LOCATION"]:
    x = pov_filtered[pov_filtered["LOCATION"] == loc]["Value"]
    if (len(x) > 0):
        l_pov_2015.append(round(x.iloc[0], 3))
    else:
        l_pov_2015.append(-1)
new_df["POV_VALUE_2015"] = pd.Series(l_pov_2015).astype(float)
new_df=new_df[new_df["CNAME"]!=-1]
new_df.to_csv("output/gdp_unempl_pov.csv", index=False)

