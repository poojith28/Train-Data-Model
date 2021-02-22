import pandas as pd
from Math_Model import Math_model

Model = Math_model()
Model.google_data_prep()
Model.GET_STATION_TRIAIN_PER_HOUR()
data = Model.Algorithm()

print(data)


