
from GAN_Data_Prep import Data_prep
from sdv.constraints import UniqueCombinations
from sdv.tabular import TVAE


model = Data_prep(DATA_Prep = True, Sample_data_prop = 100, GAN_data_path=None)
# Data prep for Gan model
data = model.model()

# forming the constraints
unique_Train_constraint = UniqueCombinations(columns=['Fromstation', 'Tostation','TrainNo'], handling_strategy='reject_sampling')
constraints = [unique_Train_constraint]

# defining a model
model = TVAE(constraints= constraints)

# training
model.fit(data)

# sample genration
num_samples = 1000000
samples = model.sample(num_samples)