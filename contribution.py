import numpy as np
import pandas as pd


def get_Down_value(self, i, j):
    if i == 0 and j == 1:
        return self.Station_data["Down_out"][j]
    else:
        if i == j or i > j:
            return 0
        else:
            num = self.Station_data["Down_in"][i]
            den = 0
            for k in range(0, j):
                den = den + self.Station_data["Down_in"][k]
                num = num - self.upmat[i][k]
                for l in range(0, j - 1):
                    den = den - self.upmat[l][k]
            return num / den * self.Station_data["Down_out"][j]


def Up_Contribution_Calculation(self):
    self.upmat = np.zeros((26, 26))
    self.upmat = pd.DataFrame(self.upmat)
    for j in range(0, 26):
        for i in range(0, 26):
            self.upmat[i][j] = get_Down_value(self, i, j)
    self.upmat = self.upmat.astype(int)
    self.upmat = self.upmat.set_axis(
        ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13", "s14", "s15", "s16",
         "s17", "s18", "s19", "s20", "s21", "s22", "s23", "s24", "s25", "s26"], axis="columns")
    self.upmat["S"] = self.Station_data["S"]

    return self.upmat


def down_get_value(self, i, j):
    if i == 0 and j == 1:
        return self.Station_data["Up_out"][25 - j]
    else:
        if i == j or i > j:
            return 0
        else:
            num = self.Station_data["Up_in"][25 - i]
            den = 0
            for k in range(0, j):
                den = den + self.Station_data["Up_in"][25 - k]
                num = num - self.downmat[i][k]
                for l in range(0, j - 1):
                    den = den - self.downmat[l][k]
            return num / den * self.Station_data["Up_out"][25 - j]


def down_Contribution_Calculation(self):
    self.downmat = np.zeros((26, 26))
    self.downmat = pd.DataFrame(self.downmat)
    for j in range(0, 26):
        for i in range(0, 26):
            self.downmat[i][j] = down_get_value(self, i, j)
    self.downmat = self.downmat.astype(int)
    self.downmat = self.downmat.set_axis(
        ["s26", "s25", "s24", "s23", "s22", "s21", "s20", "s19", "s18", "s17", "s16", "s15", "s14", "s13", "s12", "s11",
         "s10", "s9", "s8", "s7", "s6", "s5", "s4", "s3", "s2", "s1"], axis="columns")
    self.downmat["S"] = self.Station_data["S"].values[::-1]
    return self.downmat

