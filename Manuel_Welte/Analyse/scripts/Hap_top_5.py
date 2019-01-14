import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ressources/2016.csv")
df = df.sort_values("Happiness Score", ascending=False)

head_5 = df.head(5)
head_cnames = head_5["Country"]
head_hvalues = head_5["Happiness Score"]
print(head_5)
print(round(head_hvalues.mean(), 3))
print("maximum="+str(df["Happiness Score"].head(1)))
print("minimum="+str(df["Happiness Score"].tail(1)))
tail_5 = df.tail(5)
tail_cnames = tail_5["Country"]
tail_hvalues = tail_5["Happiness Score"]
print(tail_5[["Country", "Happiness Score"]])
print(round(tail_hvalues.mean(), 3))

score = df["Happiness Score"]
class0 = df[(df["Happiness Score"] < 4.0)]
class1 = df[(df["Happiness Score"] >= 4.0) & (df["Happiness Score"] < 4.5)]
class2 = df[(df["Happiness Score"] >= 4.5) & (df["Happiness Score"] < 5.5)]
class3 = df[(df["Happiness Score"] >= 5.5) & (df["Happiness Score"] < 6.5)]
class4 = df[(df["Happiness Score"] >= 6.5) & (df["Happiness Score"] < 7.5)]
class5 = df[(df["Happiness Score"] >= 7.5)]

print(len(class4))
print(len(class5))
perc_c0 = float(len(class0)) / float(len(df)) * 100
perc_c1 = float(len(class1)) / float(len(df)) * 100
perc_c2 = float(len(class2)) / float(len(df)) * 100
perc_c3 = float(len(class3)) / float(len(df)) * 100
perc_c4 = float(len(class4)) / float(len(df)) * 100
perc_c5 = float(len(class5)) / float(len(df)) * 100

plt.bar([1, 2, 3, 4, 5, 6], [perc_c0, perc_c1, perc_c2, perc_c3, perc_c4, perc_c5])
plt.xticks([1, 2, 3, 4, 5, 6], ["<4.0","4.0-4.4", "4.5-5.4", "5.5-6.4.", "6.5-7.4", ">=7.5"])
# plt.pie([len(class1),len(class2),len(class3),len(class4),len(class5)],labels=["3.0 or less","3.0-4.5","4.5-6.0","6.0-7.5","7.5 or higher"])
plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40], ["0%", "5%", "10%", "15%", "20%", "25%", "30%", "35%", "40%"])
plt.xlabel("Happiness score 2016 of all 157 OECD countries, classified")
plt.ylabel("% of all countries that are part of this class")
plt.savefig("outDoku/hapAll.png")


mean = round(score.mean(), 4)
print("Arithmetisches Mittel="+str(mean))

std = round(score.std(), 4)
print("Standardabweichung=" + str(std))
var = round(score.var(), 4)
print("Varianz= " + str(var))
quantile_25 = score.quantile(0.25)
quantile_75 = score.quantile(0.75)
print("0.25-Quantil= " + str(quantile_25))
print("0.75-Quantil= " + str(quantile_75))
print("Minimum= "+str(score.sort_values(ascending=False).tail(1)))
print("Maximum= "+str(score.sort_values(ascending=False).head(1)))

'''
plt.plot(df["Happiness Score"])
plt.text(120,6.5,"mean= "+str(mean)+"\n"+"var= "+str(var))
plt.title("Happiness Score 2016, all 156 countries")
plt.tick_params(
    axis='x',
    which='both',
    bottom=False,
    top=False,
    labelbottom=False)
plt.savefig("output/hap_all.png")
'''
# plt.boxplot(df["Happiness Score"])
# plt.show()
##########################################################
