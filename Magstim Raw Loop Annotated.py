# This code is used to analyze the data from the Magstim twitch and tetanus
# experiments. This converts the exported .csv files from the Biometrics 
# DataLink into a suitable form for import into MatLab to be processed for 
#  twitch peak identification
import pandas as pd
import glob
import os

def tic(): # Tic and Toc are included to measure the processing time on different 
           # machines
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():

    import time
    if 'startTime_for_tictoc' in globals():
        print ("Elapsed time was " + str(time.time() - startTime_for_tictoc) + " seconds.")
    else:
        print ("Toc: start time not set")

tic() # starts the timer

# change the current working directory to the desired folder, and print the
# current working directory. 

os.chdir("C:/Users/mmduv/Desktop/") 
cwd = os.getcwd()
# print(cwd)

# For loop to cycle through the specified directory, and perform the data 
# cleaning below
for f in glob.glob('*.csv'):   

    data = pd.read_table(f, header=None, sep=",,,", engine='python') #read data 
    datasubset = data.drop(data.index[0:4])      # drop first four lines to 
                                                 # eliminate the header formatting 
    datasubsets = datasubset.shift(-2, axis = 0) # Shift the desired data to 
                                                 # the left two columns
    df = datasubsets.iloc[::2]                   # define variable df for the
                                                 # raw data 
    dfs = df.reset_index(drop=True)              # reset the index for the 
                                                 # dataset
    dfs.index = dfs.index + 1                    # make the index start at one
    dfs1= dfs[:-3]                               # drop the last three rows
                                                 # of the index
    dfs1.to_csv(f, header=False, index=True)     # export last dataframe to csv
toc()                                            # stops the timer