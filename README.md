# Train-Data-Model

## Model inputs. 

•	We have 26 stations on Nambu line, for coding purpose we have named as s1, s2, s3……. s26. along with the station names we also have daily passenger count for up trains and down trains for both IN and OUT. 

•	For the train information, we have 325 trains with their timings. 

•	We also have Google Places data which gives us the approximate distribution of passengers on station during the entire day. Note: as of now we don’t have distribution of all stations, to which we had made substitutions and assumptions.

## Math Model

In Analytical model we use certain formulas to generate data for our models. 

1st step in our Analytical model was to get Trip distribution of the data. In get words to get the count of travellers from station si to sj or contribution of Station Ins to outs of next stations on train line. 

Formulae to calculate contribution of each station. 

![alt text](https://github.com/poojith28/Train-Data-Model/blob/main/pic.png)

Note: In the above formulae k and l are 1 if it’s a down train and it will 26 and backwards count if it’s up trains.

From the numbers we got from the above formulae we create a simple program which uses google data and train data to distribute these numbers to the trains,

For example, let’s assume we have one train Ta at 4 o’clock from station 1 to station 26, 
Then we use the below formulas to get the data 

V_s1_T1_s4 = s1_s4* google_data_of_s1_at_4
V_s2_T1_s4 = s2_s4* google_data_of_s2_at_4

s1_in = V_s1_T1_s2 + V_s1_T1_s3 + V_s1_T1_s4 + V_s1_T1_s5 +….. + V_s1_T1_s26
s4_out = = V_s1_T1_s4 + V_s2_T1_s4 + V_s3_T1_s4 

## Genrating Train Data Using the Math Model

Librabry Recquirements
  * Pandas 
  * numpy 
  * python3 or greater
  * populartimes (if using google API)
  
### Steps to execute code 

### Step 1 : import math Model as shown below
##### >>>>> from Math_Model import Math_model

### Step 2 : Creating Instance Objects, and giving paths to read Data files, by default paths are referred to same document as the python files.
##### >>>>> Model = Math_model(Train_data_path = "TrainData4.csv",station_data_path = "Station_data.csv", Google_path_ = "Google_Station.csv") 

Note : If google Data is not avilable we have, we a function to get them, steps are as follows.

### Step A : Import the function 
##### >>>>> from Google_API import Get_GoogleData

### Step B : Calling the Function 
##### >>>>> Data = Get_GoogleData(Place_key = "", API_KEY = "", Normailze=True, day=0)

Place_key = str; unique google maps id; retrievable via populartimes.get() or https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder

API_KEY = str; api key from google places web service; e.g. "your-api-key"  https://developers.google.com/places/web-service/get-api-key

Normailze = True or False, by default it is True, it returns Normalized popular times data. 

day = 0 to 6 , by default it is 0(monday), 0 = monday, 1 = tuesday, 2 = wednesday, 3 = thursday, 4 = friday, 5= saturday, 6 = sunday.

###  Step 3 : Preping the data for the Algorithm
##### >>>>> Model.google_data_prep()
##### >>>>> Model.GET_STATION_TRIAIN_PER_HOUR() 

### Step 4 : Calling Algorith Funtion 
##### >>>>> Data = Model.Algorithm()


## Preping Train Data For the GAN Training.

Librabry Recquirements
  * Pandas 
  * numpy 
  * python3 or greater
  * populartimes (if using google API)
  
### Step 1 : import GAN_Data_Prep as shown below
##### >>>>> from GAN_Data_Prep import Data_prep

  
### Step 2 : Creating Instance Objects with initialization. 
##### >>>>> model = Data_prep(DATA_Prep = True, Sample_data_prop = 100, GAN_data_path=None) 

DATA_Prep = True or False, by default it is set to True, which means, we ask Math maodel to generate data for GAN Model. if it is set false, we need to give GAN_data_path.

Sample_data_prop = 1 to 100, by default it is set to 100, which means we take 100% of data for train, Sample_data_prop allows us to take percentage of sample data to be taken for training.

### Step 3 : Calling function to get Data

##### >>>>> data = model.model()

## GAN Training.

Due to compatability, we mainly look at three models, 

1) TGAN
2) CTGAN - (Allows to add constraints)
4) TVAE - (Allows to add constraints)

For TGAN, install **tgan** package, for CTGAN and TVAE, install **sdv** package

## Training TGAN MODEL

for trining the TGAN model, our next step would be to import TGAN and create an instance of the model.
### Step 1 : Creating an instance of the model

This will create a TGAN instance with the default parameters:
##### >>>>> from tgan.model import TGANModel
##### >>>>> continuous_columns = [] 
Note : continuous_columns is empty if we are not using any continuous data. if we are training model with hour, continuous_columns = ["hour"] 
##### >>>>> Tgan = TGANModel(continuous_columns)

### Step 2 : Fit the model to the training data.

##### >>>>> Tgan.fit(data)

Note: this will not return anyting, however progress of fitting will be displayed, based on the system performance and data size, it take few hours to train the model.

### Step 3 : Generating Sample Data. 

##### >>>>> num_samples = 1000000   (sample data size we want to Generate)
##### >>>>> samples = Tgan.sample(num_samples)


Note : if we want to change model parameters such as **epchos**, **learning_rate**, or **batch size** they can passed when creating a instance.


TGAN Parameters 

* max_epoch (int, default=100): Number of epochs to use during training.
* steps_per_epoch (int, default=10000): Number of steps to run on each epoch.
* save_checkpoints(bool, default=True): Whether or not to store checkpoints of the model after each training epoch.
* restore_session(bool, default=True): Whether or not continue training from the last checkpoint.
* batch_size (int, default=200): Size of the batch to feed the model at each step.
* z_dim (int, default=100): Number of dimensions in the noise input for the generator.
* noise (float, default=0.2): Upper bound to the gaussian noise added to categorical columns.
* l2norm (float, default=0.00001): L2 reguralization coefficient when computing losses.
* learning_rate (float, default=0.001): Learning rate for the optimizer.
* num_gen_rnn (int, default=400): Number of units in rnn cell in generator.
* num_gen_feature (int, default=100): Number of units in fully connected layer in generator.
* num_dis_layers (int, default=2): Number of layers in discriminator.
* num_dis_hidden (int, default=200): Number of units per layer in discriminator.
* optimizer (str, default=AdamOptimizer): Name of the optimizer to use during fit, possible values are: [GradientDescentOptimizer, AdamOptimizer, AdadeltaOptimizer].

## Training CTGAN MODEL or TVAE MODEL

Steps of Training CTGAN andTVAE are almost similar to TGAN, they are as follows.

##### >>>>>from sdv.tabular import CTGAN

##### >>>>> model = CTGAN()

##### >>>>> model.fit(data)

**for Creating Sample, it is,** 

##### >>>>>  num_samples = 1000000
##### >>>>> samples = model.sample(num_samples)

### or


##### >>>>>from sdv.tabular import TVAE

##### >>>>> model = TVAE()

##### >>>>> model.fit(data)

**for Creating Sample, it is,** 

##### >>>>>  num_samples = 1000000
##### >>>>> samples = model.sample(num_samples)


unlike TGAN, CTGAN and TVAE allow to add constraints,

## Types of Constraints
### UniqueCombinations Constraint
* This constraint guarantees that the values of a set of columns can only be combined exactly as seen in the original data, and new combinations are not accepted
### GreaterThan Constraint
* This constraint guarantees that one column is always greater than the other one.
### CustomFormula Constraint
* In some cases, one column will need to be computed based on the other columns using a custom formula. 
* In these cases, we need to define a custom function that defines how to compute the value of the column.
* Once we have defined this function, we can use the ColumnFormula constraint by passing it:

## Modeling constraints to the model.

in our case, our data is compatible with UniqueCombinations Constraint,. In order to use this constraint we will need to import it from the sdv.constraints module and create an instance of it indicating:

* the names of the affected columns
* which strategy we want to use: transform or reject_sampling.

##### >>>>> from sdv.constraints import UniqueCombinations

##### >>>>> unique_Train_constraint = UniqueCombinations(columns=['Fromstation', 'Tostation','TrainNo'], handling_strategy='reject_sampling')
##### >>>>> constraints = [unique_Train_constraint]

Now that we have defined the constraints needed to properly describe our dataset, we can pass them to the Tabular Model of our choice. we will see how to pass them in CTGAN and TVAE

##### >>>>> model = CTGAN(constraints= constraints)

##### >>>>> model.fit(data)

for Creating Sample, it is,

##### >>>>>  num_samples = 1000000
##### >>>>> samples = model.sample(num_samples)

## or


##### >>>>>from sdv.tabular import TVAE

##### >>>>> model = TVAE(constraints= constraints)

##### >>>>> model.fit(data)

for Creating Sample, it is,

##### >>>>>  num_samples = 1000000
##### >>>>> samples = model.sample(num_samples)
 
* For parameters of CTGAN, please look here https://sdv.dev/SDV/api_reference/tabular/api/sdv.tabular.ctgan.CTGAN.html#sdv.tabular.ctgan.CTGAN
* For parameters of TVAE, please look here https://sdv.dev/SDV/api_reference/tabular/api/sdv.tabular.ctgan.TVAE.html#sdv.tabular.ctgan.TVAE


## Referance 

Lei Xu, Kalyan Veeramachaneni. 2018. Synthesizing Tabular Data using Generative Adversarial Networks.

Lei Xu, Maria Skoularidou, Alfredo Cuesta-Infante, Kalyan Veeramachaneni. Modeling Tabular data using Conditional GAN. NeurIPS, 2019.









