import pandas as pd

class Math_model:

    def __init__(self, Train_data_path = "TrainData4.csv", station_data_path = "Station_data.csv",Google_path_ = "Google_Station.csv"):
        import contribution
        self.Train_data = pd.read_csv(Train_data_path)
        self.Station_data = pd.read_csv(station_data_path)
        self.GData = pd.read_csv(Google_path_)
        self.Down_contri = contribution.Up_Contribution_Calculation(self)
        self.Up_contri = contribution.down_Contribution_Calculation(self)
        self.stations_trains_per_hour = []
        self.V_Si_Sj = {}
        self.vdata = pd.DataFrame()

    def google_data_prep(self):
        for i in range(1, len(self.Station_data["S"])+1):
            a = self.Station_data["S"][i-1]
            globals()[self.Station_data["S"][i-1]] = self.GData[a].to_frame()
            globals()[self.Station_data["S"][i-1]][0]= globals()[self.Station_data["S"][i-1]][self.Station_data["S"][i-1]]


    def GET_STATION_TRIAIN_PER_HOUR(self):
        for station in range(0, len(self.Station_data["S"])):
            train_per_hour = {}
            for hour in range(0, 24):
                train_per_hour[hour] = self.Train_data[self.Train_data['s' + str(station+1)] == (hour)]
                self.stations_trains_per_hour.append(train_per_hour)

        for si in range(0,len(self.Station_data["S"])):
            for sj in  range(0,len(self.Station_data["S"])):
                if si <= sj:
                    Data =  self.Down_contri
                else:
                    Data = self.Up_contri
                self.V_Si_Sj["s"+str(si+1)+"_"+"s"+str(sj+1)] = globals()["s"+str(sj+1)]["s" +str(sj+1)] * Data[Data.S == "s" + str(sj+1)]["s" + str(si+1)].item()


    def Algorithm(self):
        for from_station_id in range(0,len(self.Station_data["S"])):
            for to_station_id in range(0,len(self.Station_data["S"])):
                for hour in range(0,24):

                    trainDaTa = self.stations_trains_per_hour[from_station_id][hour]
                    cntup = 0
                    cntdown = 0
                    validtrains = []

                    for trainNo in trainDaTa["TrainNo"]:

                        train = trainDaTa[trainDaTa.TrainNo == trainNo]
                        length = len(train["St"].item().split(","))
                        Stations = train["St"].item().split(",")

                        if ("s" + str(from_station_id+1) in Stations) and ("s" + str(to_station_id+1) in Stations):

                            fromstationindex =  Stations.index("s" + str(from_station_id+1))
                            tostationindex = Stations.index("s" + str(to_station_id+1))
                            train_type = train["type"].item()

                            if fromstationindex >= 0 and tostationindex >=0 and tostationindex > fromstationindex:
                                if train_type == "Up":
                                    cntup = cntup +1
                                else:
                                    cntdown = cntdown +1

                                validtrains.append(trainNo)
                    if cntup>0:
                        for i in validtrains:
                            train = trainDaTa[trainDaTa.TrainNo == i]
                            train_type = train["type"].item()
                            if train_type == "Up":
                                values = self.V_Si_Sj["s"+str(from_station_id+1)+"_"+"s"+str(to_station_id+1)][hour] /  cntup
                                self.vdata = self.vdata.append({ "train_number" : i,
                                                  "Fromstation" : "s" + str(from_station_id+1),
                                                  "ToStation" : "s" + str(to_station_id+1),
                                                  "Passenger_count" : values,
                                                  "Train_hour" : hour,
                                                  "Type" : train_type} , ignore_index=True )


                    if cntdown>0:
                        for i in validtrains:
                            train = trainDaTa[trainDaTa.TrainNo == i]
                            train_type = train["type"].item()
                            if train_type == "Down":
                                values = self.V_Si_Sj["s"+str(from_station_id+1)+"_"+"s"+str(to_station_id+1)][hour] /cntdown
                                self.vdata = self.vdata.append({ "train_number" : i,
                                                  "Fromstation" : "s" + str(from_station_id+1),
                                                  "ToStation" : "s" + str(to_station_id+1),
                                                  "Passenger_count" : values,
                                                  "Train_hour" : hour,
                                                  "Type" : train_type} , ignore_index=True)

        return self.vdata



