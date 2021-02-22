
from GAN_Data_Prep import Data_prep

Model = Data_prep(DATA_Prep = True, Sample_data_prop = 100, GAN_data_path=None)

data = Model.model()


