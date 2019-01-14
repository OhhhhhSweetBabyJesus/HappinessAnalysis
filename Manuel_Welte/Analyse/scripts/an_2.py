import pandas as pd

from matplotlib import pyplot as plt
from scipy.stats import linregress as lr
import kennzahlen
import numpy as np

plt.rcParams.update({'font.size': 7})
df = pd.read_csv("ressources/edu_hlthcare_minwage.csv")
plt.style.use("ggplot")
y_descr = "Happiness Score, Year 2015"
# Education
'''
edu_pub_filter=df[df["EDU_PUB"]!=-1.0]
x=edu_pub_filter["EDU_PUB"].tolist()
y=edu_pub_filter["HAP_2015"].tolist()
x_descr="% of tertiary education costs covered by government"
countries= edu_pub_filter["CNAME"]
filtered_vals=edu_pub_filter
kennzahlen.calc_all(edu_pub_filter["EDU_PUB"])
key="EDU_PUB"

xtickspos=[30,40,50,60,70,80,90,100]
xticks=list(map(lambda x:str(x)+"%",xtickspos))
'''
# Min wage

min_wage_filter = df[df["MIN_WAGE"] != -1.0]
x = min_wage_filter["MIN_WAGE"].tolist()
y = min_wage_filter["HAP_2015"].tolist()
countries = min_wage_filter["CNAME"]
x_descr = "monthly minimum wage in USD PPP"
filtered_vals=min_wage_filter
key="MIN_WAGE"
kennzahlen.calc_all(min_wage_filter["MIN_WAGE"])
print("corr=" + str(pd.Series(x).corr(pd.Series(y))))
reg = np.polyfit(x, y, 1)
z = list(map((lambda x: x * reg[0] + reg[1]), x))

print("Lin Reg mit scipi " + str(lr(x, y)))
# print("Lin Reg mit scipi dummy "+str(lr([1,1,1,1],[2,9,4,3])))
plt.plot(x, z)
plt.scatter(x, y)
#plt.xticks(xtickspos,xticks)
top2 = filtered_vals.sort_values(key, ascending=False).head(3)["CNAME"].tolist()
bot2 = filtered_vals.sort_values(key, ascending=False).tail(3)["CNAME"].tolist()
for i, val in enumerate(countries):
    if (val in top2 or val in bot2):
        plt.annotate(val, (x[i], y[i]))

# plt.annotate(c, (filt["MIN_WAGE"].tolist()[i], filt["HAP_2015"].tolist()[i]))
plt.xlabel(x_descr)

plt.ylabel(y_descr)
plt.savefig("outDoku/minwage.png")

# x = [1.0, 2.0, 3.0, 4.0]
# y = [2.0, 4.0, 6.0, 9.0]
ysum = 0
for v in y:
    ysum += v
yavg = ysum / len(y)
# reg = np.polyfit(x, y, 1)
# print(reg)
# plt.plot(x, z)
# plt.scatter(x, y)
# plt.show()
num = 0.0
for i, xval in enumerate(x):
    # print((y[i] - (reg[0] * xval + reg[1])))
    num += ((y[i] - (reg[0] * xval + reg[1])) ** 2)

# print(num)
denom = 0.0

for yval in y:
    denom += ((yval - yavg) ** 2)
print("Num=" + str(num))
print("Denum=" + str(denom))
print(1 - num / (denom))

'''
edu_pub=edu_pub_filter["EDU_PUB"]
hap_edu_pub_filtered=edu_pub_filter["HAP_2015"]
print(len(hap_edu_pub_filtered))
print(len(edu_pub))
pear_corr=round(hap_edu_pub_filtered.corr(edu_pub),3)
print("Pearson Correlation Public Education: "+str(hap_edu_pub_filtered.corr(edu_pub)))
mean=round(edu_pub.mean(),3)
var=round(edu_pub.var(),3)
print(mean)
print(var)
print(pear_corr)
plt.scatter(edu_pub,hap_edu_pub_filtered)
#plt.title("Pearson-Coeff.= "+str(pear_corr))
#"\n PubEd_mean= "+str(mean)+"%\n  PubEd_variance= "+str(var)+"%"
for i, c in enumerate(edu_pub_filter["CNAME"]):
    if i % 2 == 0:
        plt.annotate(c, (edu_pub.tolist()[i], hap_edu_pub_filtered.tolist()[i]))
plt.xlabel("% of tert. education costs payed by gov. in 2015")
plt.ylabel("Happiness Score 2015")
plt.savefig("output/edu.png")
'''

'''
min_wage_filtered=df[df["MIN_WAGE"]!=-1.0]
hap_min_wage_filtered=min_wage_filtered["HAP_2015"]
min_wage=min_wage_filtered["MIN_WAGE"]
print(len(hap_min_wage_filtered))
print(len(min_wage))
print("Pearson Correlation Minimum Wage:"+str(hap_min_wage_filtered.corr(min_wage)))
plt.style.use("ggplot")
#plt.scatter(min_wage,hap_min_wage_filtered)
#plt.show()

pub_hc_filtered=df[df["PUB_HEALTHCARE"]!=-1]
hap_hc_filtered=pub_hc_filtered["HAP_2015"]
pub_hc=pub_hc_filtered["PUB_HEALTHCARE"]

print("Pearson Correlation Public Healthcare "+ str(pub_hc.corr(hap_hc_filtered)))

x=df[df["POV_VALUE_2015"]!=-1]
filt=x[x["MIN_WAGE"]!=-1]
print("PC MIN_WAGE:"+str(filt["HAP_2015"].corr(filt["MIN_WAGE"])))
plt.scatter(filt["MIN_WAGE"],filt["HAP_2015"])
z=[]
for i,c in enumerate(filt["CNAME"]):
   plt.annotate(c,(filt["MIN_WAGE"].tolist()[i],filt["HAP_2015"].tolist()[i]))


plt.show()
filt2=x[x["EDU_PUB"]!=-1]
'''
# print("PC EDUpub "+str(filt2["HAP_2015"].corr(filt2["EDU_PUB"])))
