
from GAN_Data_Prep import Data_prep
from sdv.constraints import UniqueCombinations
from sdv.tabular import TVAE


model = Data_prep(DATA_Prep = False, Sample_data_prop = 100, GAN_data_path="DATA.CSV")
# Data prep for Gan model
data = model.model()

# forming the constraints
unique_Train_constraint = UniqueCombinations(columns=['From_station', 'To_station','Train_no'], handling_strategy='reject_sampling')
constraints = [unique_Train_constraint]

# defining a model
model = TVAE(constraints= constraints)

# training
model.fit(data)

# sample genration
num_samples = 1000000
samples = model.sample(num_samples)