# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 23:25:29 2018
@author: Jose Hervas <jhervasdiaz@gmail.com>
"""

from time import gmtime, strftime
import requests, re

#Config
api_endpoints = ["http://www.bcn.cat/transit/dades/dadesitineraris.dat",
                 "http://www.bcn.cat/transit/dades/dadestrams.dat34234"]

destination_files = ["itineraris",
                     "trams"]

data_format = ["^[0-9]+#[0-9]+#[0-9]+#[0-9]+#[0-9]+#[0-9]+#[0-9]+#[0-9]+$",
               "^[0-9]+#[0-9]+#[0-9]+#[0-9]+$"]

#Logs texts
connection_error_msg = "ERROR: Unable to reach the endpoint at: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
data_error_msg = "ERROR: Data retrieved has not the right format. \nFull data text: \n"
file_error_msg = "ERROR: Could not open file: "
success_msg = "Data updated at: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())

#main
def extract(Index):
    #Block 1: Retrieve data
    try:
        call_result = requests.get(api_endpoints[Index]).text
        #Data quality
        data_sample = call_result.split('\n')[0]
        if bool(re.match(data_format[Index], data_sample)):
            new_entry = call_result
        else:
            new_entry = data_error_msg + call_result
    except:
        new_entry = connection_error_msg + '\n'

    #Block 2: Store results
    try:
        with open(destination_files[Index]+".txt", "a") as myfile:
            myfile.write(new_entry)
            myfile.close()
        log = success_msg + '\n'
    except:
        log = file_error_msg + destination_files[Index]+".txt" + '\n'

    #Block 3: Add logs
    with open("AUX_LOGS.txt", "a") as myfile:
        myfile.write(log)
        myfile.close()

#job
for i in range(len(api_endpoints)):
    extract(i)
