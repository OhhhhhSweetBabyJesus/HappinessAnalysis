import pandas as pd
from matplotlib import pyplot as plt

# ressources
hap_2015 = pd.read_csv("ressources/2015.csv")
hap_2016 = pd.read_csv("ressources/2016.csv")
hap_2017 = pd.read_csv("ressources/2017.csv")
pgh_15_17 = pd.read_csv("ressources/perceived good health 15-17.csv")
hw_15_17 = pd.read_csv("ressources/hours worked 15-17.csv")
awjd_15_17 = pd.read_csv("ressources/average_wages_dollar.csv")
le_15_17 = pd.read_csv("ressources/life_expectancy.csv")



#########################
# Happinessscore 15 16 17
#########################

# created csv with countryname and happiness score for 2015/2016/2017

hap_df_15 = pd.DataFrame()
hap_df_15["LOCATION"] = hap_2015["Country"]
hap_df_15["HAP_15"] = hap_2015["Happiness Score"]
hap_df_15.to_csv("output/hap_15.csv", index=False)

hap_df_16 = pd.DataFrame()
hap_df_16["LOCATION"] = hap_2016["Country"]
hap_df_16["HAP_16"] = hap_2016["Happiness Score"]
hap_df_15.to_csv("output/hap_16.csv", index=False)

hap_df_17 = pd.DataFrame()
hap_df_17["LOCATION"] = hap_2017["Country"]
hap_df_17["HAP_17"] = hap_2017["Happiness.Score"]
hap_df_15.to_csv("output/hap_17.csv", index=False)

###########################
# perceived good Health 15 16 17
###########################

# created csv with countryname and perceived good health status for 2015/2016/2017
# merged each dataframe with the dataframe of the happiness score from the same year
# merged all 3 dataframes (perceived good health + happiness score)

pgh_df_15 = pd.DataFrame()
pgh_hap_15 = pd.DataFrame()
pgh_df_15["LOCATION"] = pgh_15_17[(pgh_15_17["Year"] == 2015)]["Country"]
pgh_df_15["P_2015"] = pgh_15_17[(pgh_15_17["Year"] == 2015)]["Value"]
pgh_df_15.to_csv("output/perceived_health_15.csv", index=False)
pgh_hap_15 = pd.merge(pgh_df_15, hap_df_15, how='inner', on='LOCATION')
pgh_hap_15.to_csv("output/perceived_health_hap_15.csv", index=False)

pgh_df_16 = pd.DataFrame()
pgh_hap_16 = pd.DataFrame()
pgh_df_16["LOCATION"] = pgh_15_17[(pgh_15_17["Year"] == 2016)]["Country"]
pgh_df_16["P_2016"] = pgh_15_17[(pgh_15_17["Year"] == 2016)]["Value"]
pgh_df_16.to_csv("output/perceived_health_16.csv", index=False)
pgh_hap_16 = pd.merge(pgh_df_16, hap_df_16, how='inner', on='LOCATION')

pgh_df_17 = pd.DataFrame()
pgh_hap_17 = pd.DataFrame()
pgh_df_17["LOCATION"] = pgh_15_17[(pgh_15_17["Year"] == 2017)]["Country"]
pgh_df_17["P_17"] = pgh_15_17[(pgh_15_17["Year"] == 2017)]["Value"]
pgh_df_17.to_csv("output/perceived_health_17.csv", index=False)
pgh_hap_17 = pd.merge(pgh_df_17, hap_df_17, how='inner', on='LOCATION')

pgh = pd.DataFrame()
pgh = pd.merge(pgh_hap_15, pgh_hap_16, how='outer', on='LOCATION')
pgh = pd.merge(pgh, pgh_hap_17, how='outer', on='LOCATION')
pgh.to_csv("output/perceived_health_hap_15_17.csv", index=False)

##########################
# hours worked 15 16 17
##########################

# created csv with countryname and hours worked for 2015/2016/2017
# merged each dataframe with the dataframe of the happiness score from the same year
# merged all 3 dataframes (hours worked + happiness score)

hw_df_15 = pd.DataFrame()
hw_hap_15 = pd.DataFrame()
hw_df_15["LOCATION"] = hw_15_17[(hw_15_17["EMPSTAT"] == "TE") & (hw_15_17["TIME"] == 2015)]["Country"]
hw_df_15["WORKINGHOURS_15"] = hw_15_17[(hw_15_17["EMPSTAT"] == "TE") & (hw_15_17["TIME"] == 2015)]["Value"]
hw_df_15.to_csv("output/hours_worked_15.csv", index=False)
hw_hap_15 = pd.merge(hw_df_15, hap_df_15, how='inner', on='LOCATION')


hw_df_16 = pd.DataFrame()
hw_hap_16 = pd.DataFrame()
hw_df_16["LOCATION"] = hw_15_17[(hw_15_17["EMPSTAT"] == "TE") & (hw_15_17["TIME"] == 2016)]["Country"]
hw_df_16["WORKINGHOURS_16"] = hw_15_17[(hw_15_17["EMPSTAT"] == "TE") & (hw_15_17["TIME"] == 2016)]["Value"]
hw_df_16.to_csv("output/hours_worked_16.csv", index=False)
hw_hap_16 = pd.merge(hw_df_16, hap_df_16, how='inner', on='LOCATION')
hw_hap_16.to_csv("output/hw_hap_16.csv")

hw_df_17 = pd.DataFrame()
hw_hap_17 = pd.DataFrame()
hw_df_17["LOCATION"] = hw_15_17[(hw_15_17["EMPSTAT"] == "TE") & (hw_15_17["TIME"] == 2017)]["Country"]
hw_df_17["WORKINGHOURS_17"] = hw_15_17[(hw_15_17["EMPSTAT"] == "TE") & (hw_15_17["TIME"] == 2017)]["Value"]
hw_df_17.to_csv("output/hours_worked_17.csv", index=False)
hw_hap_17 = pd.merge(hw_df_17, hap_df_17, how='inner', on='LOCATION')

hw = pd.DataFrame()
hw = pd.merge(hw_hap_15, hw_hap_16, how='outer', on='LOCATION')
hw = pd.merge(hw, hw_hap_17, how='outer', on='LOCATION')
hw.to_csv("output/hours_worked_hap_15_17.csv", index=False)


###########################
# average Wages PPP in US-Dollar
###########################

# created csv with countryname and average wages (PPP in US-Dollar) for 2015/2016/2017
# merged each dataframe with the dataframe of the happiness score from the same year
# merged all 3 dataframes (average wages ppp in US-Dollar + happiness score)

awppp_df_15 = pd.DataFrame()
awppp_hap_15 = pd.DataFrame()
awppp_df_15["LOCATION"] = awjd_15_17[(awjd_15_17["Time"] == 2015) & (awjd_15_17["SERIES"] == "USDPPP")]["Country"]
awppp_df_15["AVRG_WAGE_15"] = awjd_15_17[(awjd_15_17["TIME"] == 2015) & (awjd_15_17["SERIES"] == "USDPPP")]["Value"]
awppp_df_15.to_csv("output/wages_ppp_15.csv", index=False)
awppp_hap_15 = pd.merge(awppp_df_15, hap_df_15, how='inner', on='LOCATION')
awppp_hap_15.to_csv("output/wages_ppp_hap_15.csv", index=False)

awppp_df_16 = pd.DataFrame()
awppp_hap_16 = pd.DataFrame()
awppp_df_16["LOCATION"] = awjd_15_17[(awjd_15_17["Time"] == 2016) & (awjd_15_17["SERIES"] == "USDPPP")]["Country"]
awppp_df_16["AVRG_WAGE_16"] = awjd_15_17[(awjd_15_17["TIME"] == 2016) & (awjd_15_17["SERIES"] == "USDPPP")]["Value"]
awppp_df_16.to_csv("output/wages_ppp_16.csv", index=False)
awppp_hap_16 = pd.merge(awppp_df_16, hap_df_16, how='inner', on='LOCATION')
awppp_hap_16.to_csv("output/wages_ppp_hap_16.csv", index=False)

awppp_df_17 = pd.DataFrame()
awppp_hap_17 = pd.DataFrame()
awppp_df_17["LOCATION"] = awjd_15_17[(awjd_15_17["Time"] == 2017) & (awjd_15_17["SERIES"] == "USDPPP")]["Country"]
awppp_df_17["AVRG_WAGE_17"] = awjd_15_17[(awjd_15_17["TIME"] == 2017) & (awjd_15_17["SERIES"] == "USDPPP")]["Value"]
awppp_df_17.to_csv("output/wages_ppp_17.csv", index=False)
awppp_hap_17 = pd.merge(awppp_df_17, hap_df_17, how='inner', on='LOCATION')
awppp_hap_17.to_csv("output/wages_ppp_hap_17.csv", index=False)

awppp = pd.DataFrame()
awppp = pd.merge(awppp_hap_15, awppp_hap_16, how='outer', on='LOCATION')
awppp.to_csv("output/wages_ppp_hap_15_16.csv", index=False)

awppp = pd.merge(awppp, awppp_hap_17, how='outer', on='LOCATION')
awppp.to_csv("output/wages_ppp_hap_15_17.csv", index=False)

##########################
# life expectancy 15 16 17
##########################

# created csv with countryname and life expectancy for 2015/2016/2017
# merged each dataframe with the dataframe of the happiness score from the same year
# merged all 3 dataframes (life expectancy + happiness score)

le_df_15 = pd.DataFrame()
le_hap_15 = pd.DataFrame()
le_df_15["LOCATION"] = le_15_17[(le_15_17["YEA"] == 2015)]["Country"]
le_df_15["LE_15"] = le_15_17[(le_15_17["YEA"] == 2015)]["Value"]
le_df_15.to_csv("output/le_15.csv", index=False)
le_hap_15 = pd.merge(le_df_15, hap_df_15, how='inner', on='LOCATION')
le_hap_15.to_csv("output/le_hap_15.csv")

le_df_16 = pd.DataFrame()
le_hap_16 = pd.DataFrame()
le_df_16["LOCATION"] = le_15_17[(le_15_17["YEA"] == 2016)]["Country"]
le_df_16["LE_16"] = le_15_17[(le_15_17["YEA"] == 2016)]["Value"]
le_df_16.to_csv("output/le_16.csv", index=False)
le_hap_16 = pd.merge(le_df_16, hap_df_16, how='inner', on='LOCATION')
le_hap_16.to_csv("output/le_hap_16.csv")

le_df_17 = pd.DataFrame()
le_hap_17 = pd.DataFrame()
le_df_17["LOCATION"] = le_15_17[(le_15_17["YEA"] == 2017)]["Country"]
le_df_17["LE_17"] = le_15_17[(le_15_17["YEA"] == 2017)]["Value"]
le_df_17.to_csv("output/le_17.csv", index=False)
le_hap_17 = pd.merge(le_df_17, hap_df_17, how='inner', on='LOCATION')

le = pd.DataFrame()
le = pd.merge(le_hap_15, le_hap_16, how='outer', on='LOCATION')
le = pd.merge(le, le_hap_17, how='outer', on='LOCATION')
le.to_csv("output/le_hap_15_17.csv", index=False)
