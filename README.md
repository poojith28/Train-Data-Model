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
  
#### Steps to execute code 

Step 1 : import math Model as shown below
  
#### from Math_Model import Math_model

Step 2 : Creating Instance Objects, and giving paths to read Data files, by default paths are referred to same document as the python files.

#### Model = Math_model(Train_data_path = "TrainData4.csv",station_data_path = "Station_data.csv", Google_path_ = "Google_Station.csv") 

Note : If google Data is not avilable we have, we a function to get them, steps are as follows.

Step A : Import the function 

#### from Google_API import Get_GoogleData

Step B : Calling the Function 

#### Get_GoogleData(Place_key = "", API_KEY = "", Normailze=False, day=0):
 






Step 3 : Preping the data for the Algorithm

#### Model.google_data_prep()  This preps google data into recquired 
#### Model.GET_STATION_TRIAIN_PER_HOUR() 

