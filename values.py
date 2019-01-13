import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import linregress as lr

hap_2015 = pd.read_csv("ressources/2015.csv")
hap_2016 = pd.read_csv("ressources/2016.csv")
hap_2017 = pd.read_csv("ressources/2017.csv")
pgh_15_17 = pd.read_csv("ressources/perceived good health 15-17.csv")
hw_15_17 = pd.read_csv("ressources/hours worked 15-17.csv")
awjd_15_17 = pd.read_csv("ressources/average_wages_dollar.csv")
le_15_17 = pd.read_csv("ressources/life_expectancy.csv")

hap_df_15 = pd.read_csv("output/hap_15.csv")
hap_df_15 = pd.read_csv("output/hap_16.csv")
hap_df_15 = pd.read_csv("output/hap_17.csv")

hw_df_15 = pd.read_csv("output/hours_worked_15.csv")
hw_df_16 = pd.read_csv("output/hours_worked_16.csv")
hw_df_17 = pd.read_csv("output/hours_worked_17.csv")
hw_hap_15_17 = pd.read_csv("output/hours_worked_hap_15_17.csv")
hw_hap_16 = pd.read_csv("output/hw_hap_16.csv")

pgh_df_15 = pd.read_csv("output/perceived_health_15.csv")
pgh_df_16 = pd.read_csv("output/perceived_health_16.csv")
pgh_df_17 = pd.read_csv("output/perceived_health_17.csv")
pgh_hap_15_17 = pd.read_csv("output/perceived_health_hap_15_17.csv")
pgh_hap_15 = pd.read_csv("output/perceived_health_hap_15.csv")

le_df_15 = pd.read_csv("output/le_15.csv")
le_df_16 = pd.read_csv("output/le_16.csv")
le_df_17 = pd.read_csv("output/le_17.csv")
le_hap_15_17 = pd.read_csv("output/le_hap_15_17.csv")
le_hap_15 = pd.read_csv("output/le_hap_15.csv")

awppp_df_15 = pd.read_csv("output/wages_ppp_15.csv")
awppp_df_16 = pd.read_csv("output/wages_ppp_16.csv")
awppp_df_17 = pd.read_csv("output/wages_ppp_17.csv")
awppp_hap_df_15_17 = pd.read_csv("output/wages_ppp_hap_15_17.csv")
awppp_hap_17 = pd.read_csv("output/wages_ppp_hap_17.csv")

#############################################
# key figures: mean(), std(), var(), corr()
#############################################

############################## hours worked

print("hours worked")

# mean
print("mean")
hw_df_15_mean = hw_df_15.mean()
hw_df_16_mean = hw_df_16.mean()
hw_df_17_mean = hw_df_17.mean()
print(hw_df_15_mean)
print(hw_df_16_mean)
print(hw_df_17_mean)

# varianz
print("Varianz")
hw_df_15_var = hw_df_15.var()
hw_df_16_var = hw_df_16.var()
hw_df_17_var = hw_df_17.var()
print(hw_df_15_var)
print(hw_df_16_var)
print(hw_df_17_var)

# standardabweichung
print("Standardabweichung")
hw_df_15_std = hw_df_15.std()
hw_df_16_std = hw_df_16.std()
hw_df_17_std = hw_df_17.std()
print(hw_df_15_std)
print(hw_df_16_std)
print(hw_df_17_std)

print("Korrelation")
hw_hap_15_corr = hw_hap_15_17["WORKINGHOURS_15"].corr(hw_hap_15_17["HAP_15"])
hw_hap_16_corr = hw_hap_15_17["WORKINGHOURS_16"].corr(hw_hap_15_17["HAP_16"])
hw_hap_17_corr = hw_hap_15_17["WORKINGHOURS_17"].corr(hw_hap_15_17["HAP_17"])
print(hw_hap_15_corr)
print(hw_hap_16_corr)
print(hw_hap_17_corr)

print("hw 16 quantile")

hw_df_16_min = hw_df_16["WORKINGHOURS_16"].min()
hw_df_16_25 = hw_df_16["WORKINGHOURS_16"].quantile(0.25)
hw_df_16_median = hw_df_16["WORKINGHOURS_16"].median()
hw_df_16_75 = hw_df_16["WORKINGHOURS_16"].quantile(0.75)
hw_df_16_max = hw_df_16["WORKINGHOURS_16"].max()
print(hw_df_16_min)
print(hw_df_16_25)
print(hw_df_16_median)
print(hw_df_16_75)
print(hw_df_16_max)

############################## perceived good health

print("perceived good health")
# mean
print("mean")
pgh_df_15_mean = pgh_df_15.mean()
pgh_df_16_mean = pgh_df_16.mean()
pgh_df_17_mean = pgh_df_17.mean()
print(pgh_df_15_mean)
print(pgh_df_16_mean)
print(pgh_df_17_mean)

# varianz
print("Varianz")
pgh_df_15_var = pgh_df_15.var()
pgh_df_16_var = pgh_df_16.var()
pgh_df_17_var = pgh_df_17.var()
print(pgh_df_15_var)
print(pgh_df_16_var)
print(pgh_df_17_var)

# standardabweichung
print("Standardabweichung")
pgh_df_15_std = pgh_df_15.std()
pgh_df_16_std = pgh_df_16.std()
pgh_df_17_std = pgh_df_17.std()
print(pgh_df_15_std)
print(pgh_df_16_std)
print(pgh_df_17_std)


print("Korrelation")
pgh_hap_15_corr = pgh_hap_15_17["P_2015"].corr(pgh_hap_15_17["HAP_15"])
pgh_hap_16_corr = pgh_hap_15_17["P_2016"].corr(pgh_hap_15_17["HAP_16"])

# 2017 just got 1 value
#pgh_hap_17_corr = pgh_hap_15_17["P_2017"].corr(pgh_hap_15_17["HAP_17"])

print(pgh_hap_15_corr)
print(pgh_hap_16_corr)

#print(pgh_hap_17_corr)


print("pgh 15 quantile")
pgh_df_15_min = pgh_df_15["P_2015"].min()
pgh_df_15_25 = pgh_df_15["P_2015"].quantile(0.25)
pgh_df_15_median = pgh_df_15["P_2015"].median()
pgh_df_15_75 = pgh_df_15["P_2015"].quantile(0.75)
pgh_df_15_max = pgh_df_15["P_2015"].max()
print(pgh_df_15_min)
print(pgh_df_15_25)
print(pgh_df_15_median)
print(pgh_df_15_75)
print(pgh_df_15_max)


############################## average wages PPP in US_Dollar

print("average wages ppp")
# mean
print("mean")
awppp_df_15_mean = awppp_df_15.mean()
awppp_df_16_mean = awppp_df_16.mean()
awppp_df_17_mean = awppp_df_17.mean()
print(awppp_df_15_mean)
print(awppp_df_16_mean)
print(awppp_df_17_mean)

# varianz
print("Varianz")
awppp_df_15_var = awppp_df_15.var()
awppp_df_16_var = awppp_df_16.var()
awppp_df_17_var = awppp_df_17.var()
print(awppp_df_15_var)
print(awppp_df_16_var)
print(awppp_df_17_var)

# standardabweichung
print("Standardabweichung")
awppp_df_15_std = awppp_df_15.std()
awppp_df_16_std = awppp_df_16.std()
awppp_df_17_std = awppp_df_17.std()
print(awppp_df_15_std)
print(awppp_df_16_std)
print(awppp_df_17_std)

print("Korrelation")
awppp_hap_15_corr = awppp_hap_df_15_17["AVRG_WAGE_15"].corr(awppp_hap_df_15_17["HAP_15"])
awppp_hap_16_corr = awppp_hap_df_15_17["AVRG_WAGE_16"].corr(awppp_hap_df_15_17["HAP_16"])
awppp_hap_17_corr = awppp_hap_df_15_17["AVRG_WAGE_17"].corr(awppp_hap_df_15_17["HAP_17"])
print(awppp_hap_15_corr)
print(awppp_hap_16_corr)
print(awppp_hap_17_corr)

print("awppp 17 quantile")
awppp_df_17_min = awppp_df_17["AVRG_WAGE_17"].min()
awppp_df_17_25 = awppp_df_17["AVRG_WAGE_17"].quantile(0.25)
awppp_df_17_median = awppp_df_17["AVRG_WAGE_17"].median()
awppp_df_17_75 = awppp_df_17["AVRG_WAGE_17"].quantile(0.75)
awppp_df_17_max = awppp_df_17["AVRG_WAGE_17"].max()
print(awppp_df_17_min)
print(awppp_df_17_25)
print(awppp_df_17_median)
print(awppp_df_17_75)
print(awppp_df_17_max)


############################## life expectancy

print("life expectancy")
# mean
print("mean")
le_df_15_mean = le_df_15.mean()
le_df_16_mean = le_df_16.mean()
le_df_17_mean = le_df_17.mean()
print(le_df_15_mean)
print(le_df_16_mean)
print(le_df_17_mean)

# varianz
print("Varianz")
le_df_15_var = le_df_15.var()
le_df_16_var = le_df_16.var()
le_df_17_var = le_df_17.var()
print(le_df_15_var)
print(le_df_16_var)
print(le_df_17_var)

# standardabweichung
print("Standardabweichung")
le_df_15_std = le_df_15.std()
le_df_16_std = le_df_16.std()
le_df_17_std = le_df_17.std()
print(le_df_15_std)
print(le_df_16_std)
print(le_df_17_std)

print("Korrelation")
le_hap_15_corr = le_hap_15_17["LE_15"].corr(le_hap_15_17["HAP_15"])
le_hap_16_corr = le_hap_15_17["LE_16"].corr(le_hap_15_17["HAP_16"])
# life expectancy 2017 just got 1 value
#le_hap_17_corr = le_hap_15_17["LE_17"].corr(le_hap_15_17["HAP_17"])
print(le_hap_15_corr)
print(le_hap_16_corr)
#print(le_hap_17_corr)

print("le 15 quantile")
le_df_15_min = le_df_15["LE_15"].min()
le_df_15_25 = le_df_15["LE_15"].quantile(0.25)
le_df_15_median = le_df_15["LE_15"].median()
le_df_15_75 = le_df_15["LE_15"].quantile(0.75)
le_df_15_max = le_df_15["LE_15"].max()
print(le_df_15_min)
print(le_df_15_25)
print(le_df_15_median)
print(le_df_15_75)
print(le_df_15_max)



##########
# plott
##########

# working hours 16

plt.scatter(hw_hap_15_17["WORKINGHOURS_16"], hw_hap_15_17["HAP_16"])
plt.xlabel("average hours worked in 2016")
plt.ylabel("Happiness Score in 2016")
plt.savefig('output/hw_hap_16_plott.png')
plt.show()

slope, intercept, r_value, p_value, std_err = lr(hw_hap_16["WORKINGHOURS_16"], hw_hap_16["HAP_16"])
#print(slope, intercept, r_value, p_value, std_err)
x = hw_hap_16["WORKINGHOURS_16"].tolist()
y = hw_hap_16["HAP_16"].tolist()
z = list(map((lambda x: x*slope+intercept), x))
plt.plot(x, z)
plt.scatter(x, y)
plt.xlabel("average hours worked in 2016")
plt.ylabel("Happiness Score in 2016")
plt.savefig('output/hw_hap_16_plott_lin.png')
plt.show()
print(r_value)


# perceived good health 15

plt.scatter(pgh_hap_15["P_2015"],pgh_hap_15["HAP_15"])
plt.xlabel("% of pop. perceived good health in 2015")
plt.ylabel("Happiness Score in 2015")
plt.savefig('output/pgh_hap_15_plott.png')
plt.show()

slope, intercept, r_value, p_value, std_err = lr(pgh_hap_15["P_2015"], pgh_hap_15["HAP_15"])
#print(slope, intercept, r_value, p_value, std_err)
x = pgh_hap_15["P_2015"].tolist()
y = pgh_hap_15["HAP_15"].tolist()
z = list(map((lambda x: x*slope+intercept), x))
plt.plot(x, z)
plt.scatter(x, y)
plt.xlabel("% of pop. perceived good health in 2015")
plt.ylabel("Happiness Score in 2015")
plt.savefig('output/pgh_hap_15_plott_lin.png')
plt.show()
print(r_value)


# average wages 17

plt.scatter(awppp_hap_df_15_17["AVRG_WAGE_17"], awppp_hap_df_15_17["HAP_17"])
plt.xlabel("average wages 2017 (PPP in USD)")
plt.ylabel("Happiness Score in 2017")
plt.savefig('output/awppp_hap_15_plott.png')
plt.show()

slope, intercept, r_value, p_value, std_err = lr(awppp_hap_17["AVRG_WAGE_17"], awppp_hap_17["HAP_17"])
#print(slope, intercept, r_value, p_value, std_err)
x = awppp_hap_17["AVRG_WAGE_17"].tolist()
y = awppp_hap_17["HAP_17"].tolist()
z = list(map((lambda x: x*slope+intercept), x))
plt.plot(x, z)
plt.scatter(x, y)
plt.xlabel("average wages 2017 (PPP in USD)")
plt.ylabel("Happiness Score in 2017")
plt.savefig('output/awppp_hap_17_plott_lin.png')
plt.show()
print(r_value)


# life expectancy 15

plt.scatter(le_hap_15_17["LE_15"], le_hap_15_17["HAP_15"])
plt.xlabel("life expectancy in 2015")
plt.ylabel("Happiness Score in 2015")
plt.savefig('output/le_hap_15_plott.png')
plt.show()

slope, intercept, r_value, p_value, std_err = lr(le_hap_15["LE_15"], le_hap_15["HAP_15"])
#print(slope, intercept, r_value, p_value, std_err)
x = le_hap_15["LE_15"].tolist()
y = le_hap_15["HAP_15"].tolist()
z = list(map((lambda x: x*slope+intercept), x))
plt.plot(x, z)
plt.scatter(x, y)
plt.xlabel("life expectancy in 2015")
plt.ylabel("Happiness Score in 2015")
plt.savefig('output/le_hap_15_plott_lin.png')
plt.show()
print(r_value)

plt.tick_params(
    axis='x',
    which='both',
    bottom=False,
    top=False,
    labelbottom=False)