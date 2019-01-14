import pandas as pd
from matplotlib import pyplot as plt
df_2=pd.read_csv("ressources/gdp_unempl_pov.csv")

df_2=df_2[(df_2["UNEMP_VALUE_2016"]!=-1)&(df_2["HAP_VALUE_2016"]!=-1)]
df=df_2
score_less=df_2["HAP_VALUE_2016"].sort_values(ascending=False)
quantile_25 = score_less.quantile(0.25)
quantile_75 = score_less.quantile(0.75)
print("0.25-Quantil= "+str(quantile_25))
print("0.75-Quantil= "+str(quantile_75))
mean_less=round(score_less.mean(),4)
print("Arithmetisches Mittel="+str(mean_less))
var_less=round(score_less.var(),4)
print("Varianz="+str(var_less))
print("Standardabweichung="+str(round(score_less.std(),4)))
print("Maximum= "+str(score_less.head(1).iloc[0]))
print("Minimum= "+str(score_less.tail(1).iloc[0]))
print(len(score_less.tolist()))
class0 = df[(df["HAP_VALUE_2016"] < 4.0)]
class1 = df[(df["HAP_VALUE_2016"] >= 4.0) & (df["HAP_VALUE_2016"] < 4.5)]
class2 = df[(df["HAP_VALUE_2016"] >= 4.5) & (df["HAP_VALUE_2016"] < 5.5)]
class3 = df[(df["HAP_VALUE_2016"] >= 5.5) & (df["HAP_VALUE_2016"] < 6.5)]
class4 = df[(df["HAP_VALUE_2016"] >= 6.5) & (df["HAP_VALUE_2016"] < 7.5)]
class5 = df[(df["HAP_VALUE_2016"] >= 7.5)]
perc_c0 = len(class0) / len(df) * 100
perc_c1 = len(class1) / len(df) * 100
perc_c2 = len(class2) / len(df) * 100
perc_c3 = len(class3) / len(df) * 100
perc_c4 = len(class4) / len(df) * 100
perc_c5 = len(class5) / len(df) * 100

plt.bar([1, 2, 3, 4, 5, 6], [perc_c0, perc_c1, perc_c2, perc_c3, perc_c4, perc_c5])
plt.xticks([1, 2, 3, 4, 5, 6], ["<4.0","4.0-4.4", "4.5-5.4", "5.5-6.4.", "6.5-7.4", ">=7.5"])
# plt.pie([len(class1),len(class2),len(class3),len(class4),len(class5)],labels=["3.0 or less","3.0-4.5","4.5-6.0","6.0-7.5","7.5 or higher"])
plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40], ["0%", "5%", "10%", "15%", "20%", "25%", "30%", "35%", "40%"])
plt.xlabel("Happiness score 2016 of 39 OECD or similar countries, classified")
plt.ylabel("% of all countries that are part of this class")
plt.savefig("outDoku/happLess.png")


'''

plt.plot(score_less.tolist())
plt.text(30,7,"mean= "+str(mean_less)+"\n"+"var= "+str(var_less))
plt.title("Happiness Score 2016, 39 OECD and similar countries")
plt.tick_params(
    axis='x',
    which='both',
    bottom=False,
    top=False,
    labelbottom=False)

plt.savefig("output/hap_39.png")
'''