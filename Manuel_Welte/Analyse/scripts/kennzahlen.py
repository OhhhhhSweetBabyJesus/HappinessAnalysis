import pandas as pd


def calc_all(l):
    result = ""
    result += "Standardabweichung= " + str(round(l.std(), 4))
    result += ", Varianz= " + str(round(l.var(), 4))

    result += ", Arithmetisches Mittel= " + str(round(l.mean(), 4))
    result += ", 0.25-Quantil= " + str(round(l.quantile(0.25), 4))
    result += ", 0.75-Quantil= " + str(round(l.quantile(0.75), 4))
    result += ", Maximum= " + str(round(l.sort_values(ascending=False).head(1).iloc[0], 4))
    result += ", Minimum= " + str(round(l.sort_values(ascending=False).tail(1).iloc[0], 4))
    print(result)
def test():
    print("TETSTSTTSTST")