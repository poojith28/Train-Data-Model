import numpy as np
import pandas as pd

def get_stations(len):
    stations_name = ""
    for m in range(1, len+1):
        stations_name = stations_name + "s" + str(m) + ","
    stations_name = stations_name.split(",")[0:len]
    return stations_name

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
    self.upmat = np.zeros((len(self.Station_data["S"]), len(self.Station_data["S"])))
    self.upmat = pd.DataFrame(self.upmat)
    for j in range(0, len(self.Station_data["S"])):
        for i in range(0, len(self.Station_data["S"])):
            self.upmat[i][j] = get_Down_value(self, i, j)
    self.upmat = self.upmat.astype(int)
    stations_num = get_stations(len(self.Station_data["S"]))
    self.upmat = self.upmat.set_axis(stations_num, axis="columns")
    self.upmat["S"] = self.Station_data["S"]

    return self.upmat

def down_get_value(self, i, j):
    if i == 0 and j == 1:
        return self.Station_data["Up_out"][len(self.Station_data["S"]) - 1 - j]
    else:
        if i == j or i > j:
            return 0
        else:
            num = self.Station_data["Up_in"][len(self.Station_data["S"]) - 1 - i]
            den = 0
            for k in range(0, j):
                den = den + self.Station_data["Up_in"][len(self.Station_data["S"]) -1 - k]
                num = num - self.downmat[i][k]
                for l in range(0, j - 1):
                    den = den - self.downmat[l][k]
            return num / den * self.Station_data["Up_out"][len(self.Station_data["S"]) - 1 - j]

def down_Contribution_Calculation(self):
    self.downmat = np.zeros((len(self.Station_data["S"]), len(self.Station_data["S"])))
    self.downmat = pd.DataFrame(self.downmat)
    for j in range(0, len(self.Station_data["S"])):
        for i in range(0, len(self.Station_data["S"])):
            self.downmat[i][j] = down_get_value(self, i, j)
    self.downmat = self.downmat.astype(int)
    stations_num = get_stations(len(self.Station_data["S"]))
    self.downmat = self.downmat.set_axis(stations_num[::-1] , axis="columns")
    self.downmat["S"] = self.Station_data["S"].values[::-1]
    return self.downmat