import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression as lr
import numpy as np
from scipy.stats import linregress as lr
import kennzahlen
plt.style.use("ggplot")


plt.rcParams.update({'font.size': 7})
df = pd.read_csv("ressources/gdp_unempl_pov.csv")
c_index = pd.read_csv("ressources/nameCodeIndex.csv", comment="#")


#print(pov_2015_filt[["POV_VALUE_2015", "HAP_VALUE_2015"]])
#pov = pov_2015_filt["POV_VALUE_2015"]
#hap = pov_2015_filt["HAP_VALUE_2015"]
#print("corr =" +str(pov.corr(hap)))

#Unemployment:

unemp_2016_filt=df[df["UNEMP_VALUE_2016"]!=-1]
x=unemp_2016_filt["UNEMP_VALUE_2016"].tolist()
y=unemp_2016_filt["HAP_VALUE_2016"].tolist()
y_descr="Happiness Score, year 2016"
x_descr="unemployed % of total workforce"
filtered_vals=unemp_2016_filt
key="UNEMP_VALUE_2016"
countries=unemp_2016_filt["CNAME"]
xtickspos=[5,10,15,20,25]
xticks=list(map(lambda x:str(x)+"%",xtickspos))
kennzahlen.calc_all(unemp_2016_filt["UNEMP_VALUE_2016"])

'''
#GDP:
gdp_2016_filt=df[df["GDP_VALUE_2016"]!=-1]
x=gdp_2016_filt["GDP_VALUE_2016"].tolist()
y=gdp_2016_filt["HAP_VALUE_2016"].tolist()
y_descr="Happiness Score, year 2016"
x_descr="gdp/capita in USD PPP"
filtered_vals=gdp_2016_filt
kennzahlen.calc_all(gdp_2016_filt["GDP_VALUE_2016"])
key="GDP_VALUE_2016"
countries=gdp_2016_filt["CNAME"]
'''
'''
#Poverty:
pov_2015_filt = df[df["POV_VALUE_2015"] !=-1]
x=list(map(lambda x: x*100,pov_2015_filt["POV_VALUE_2015"].tolist()))
y=pov_2015_filt["HAP_VALUE_2015"].tolist()
y_descr="Happiness Score, year 2015"
x_descr="% of population living below poverty threshold"
filtered_vals=pov_2015_filt
key="POV_VALUE_2015"
countries=pov_2015_filt["CNAME"]
xtickspos=[5,10,15,20,25]
xticks=list(map(lambda x: str(x)+"%",xtickspos))
kennzahlen.calc_all(pov_2015_filt["POV_VALUE_2015"])
'''
print("corr="+str(pd.Series(x).corr(pd.Series(y))))
reg=np.polyfit(x,y,1)
z = list(map((lambda x: x * reg[0] + reg[1]), x))


print("Lin Reg mit scipi "+str(lr(x,y)))
#print("Lin Reg mit scipi dummy "+str(lr([1,1,1,1],[2,9,4,3])))
plt.plot(x,z)
top2 = filtered_vals.sort_values(key, ascending=False).head(3)["CNAME"].tolist()
bot2 = filtered_vals.sort_values(key, ascending=False).tail(3)["CNAME"].tolist()
for i, val in enumerate(countries):
    if (val in top2 or val in bot2):
        plt.annotate(val, (x[i], y[i]))

plt.scatter(x,y)
plt.xticks(xtickspos,xticks)
plt.ylabel(y_descr)
plt.xlabel(x_descr)
plt.savefig("outDoku/unemp.png")

#x = [1.0, 2.0, 3.0, 4.0]
#y = [2.0, 4.0, 6.0, 9.0]
ysum=0
for v in y:
    ysum+=v
yavg=ysum/len(y)
#reg = np.polyfit(x, y, 1)
#print(reg)
#plt.plot(x, z)
#plt.scatter(x, y)
#plt.show()
num = 0.0
for i, xval in enumerate(x):
   # print((y[i] - (reg[0] * xval + reg[1])))
    num += ((y[i] - (reg[0] * xval + reg[1]))**2)

#print(num)
denom=0.0

for yval in y:
    denom+=((yval-yavg)**2)
print("Num="+str(num))
print("Denum="+str(denom))
print(1-num/(denom))
print((-0.48622421944474137)**2)

# model.fit(pov_2015_filt["POV_VALUE_2015"].tolist(),pov_2015_filt["HAP_VALUE_2015"].tolist())
'''
print(len(pov_2015_filt))
plt.scatter(pov_2015_filt["POV_VALUE_2015"], pov_2015_filt["HAP_VALUE_2015"])

pear_corr=round(pov_2015_filt["POV_VALUE_2015"].corr(pov_2015_filt["HAP_VALUE_2015"]),3)
print("Pearson: "+str(pov_2015_filt["POV_VALUE_2015"].corr(pov_2015_filt["HAP_VALUE_2015"])))
print("Spearman: "+str(pov_2015_filt["POV_VALUE_2015"].corr(pov_2015_filt["HAP_VALUE_2015"],method="spearman")))
mean=round(pov_2015_filt["POV_VALUE_2015"].mean(),3)
print(mean)
var=round(pov_2015_filt["POV_VALUE_2015"].var(),3)
print(var)
print(pear_corr)
plt.title("Pearson-Coeff.= "+str(pear_corr)+"\nPoverty_mean= "+str(mean)+"\nPoverty_variance= "+str(var))
for i, c in enumerate(pov_2015_filt["CNAME"]):
    if i % 2 == 0:
        plt.annotate(c, (pov_2015_filt["POV_VALUE_2015"].tolist()[i], pov_2015_filt["HAP_VALUE_2015"].tolist()[i]))
plt.xlabel("part of population below poverty threshold in 2015")
plt.ylabel("Happiness Score 2015")


plt.savefig("output/poverty.png")
'''
'''
print(gdp_2016.mean())
print(gdp_2016.std())
print(gdp_2016.var())
print(gdp_2016.quantile(0.75))

unempl=df[df["UNEMP_VALUE_2016"]!=-1.0]["UNEMP_VALUE_2016"]
print(unempl)
print(unempl.mean(skipna=True))
print(unempl.mean(skipna=False))
'''
# py.bar(countries,gdp_2016)
# py.show()
