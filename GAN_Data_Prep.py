class GAN_model:

    def __init__(self, GAN_TYPE = "TVAE", DATA_Prep = True, Sample_data_prop = 100,GAN_data_path=None):
        import pandas as pd
        self.DATA_Prep = DATA_Prep
        self.Sample_data_prop = Sample_data_prop
        self.df = pd.DataFrame()
        self.GAN_data_path = GAN_data_path

    def model(self):
        from Math_Model import Math_model
        import pandas as pd
        import numpy as np
        if self.DATA_Prep:
            Mdl = Math_model()
            Mdl.google_data_prep()
            Mdl.GET_STATION_TRIAIN_PER_HOUR()
            New_data = Mdl.Algorithm()
            for i in range(0, len(New_data)):
                Train_no = New_data["train_number"][i]
                To_station = New_data["ToStation"][i]
                From_station = New_data["Fromstation"][i]
                passengers = New_data["Passenger_count"][i]
                a = pd.DataFrame({
                    'Train_no': Train_no,
                    'To_station': To_station,
                    'From_station': From_station,
                    'Weight': float(1)}, index=[0])
                if passengers / (100/self.Sample_data_prop) < 1:
                    self.df = self.df.append([a] * 1, ignore_index=True)
                else:
                    self.df = self.df.append([a]*int(passengers) * int(100/self.Sample_data_prop), ignore_index=True)
        if not self.DATA_Prep:
            self.df = pd.read_csv(self.GAN_data_path)

        return self.df
