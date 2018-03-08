# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 15:15:10 2018

@author: jhervas
"""

from time import gmtime, strftime
import requests, json, os

#Config

months_ids = {
        "2017-10": "835148ef-e839-4a49-a794-f8ebe204eb8b",
        "2017-11": "ba2b3ef0-846f-477d-ad72-59a36dc806a3",
        "2017-12": "ae5d38f9-b47c-4390-a9d7-698979142050",
        "2018-01": "106e94c9-3e95-4d1e-be4e-917137845cc0",
        "2018-02": "2df09282-d7aa-48c5-b616-964b4ef97a1e",
        "2018-03": "0e2506ae-37a3-4a9d-98b0-18750628bdc9"
        }

base_url = "http://opendata-ajuntament.barcelona.cat/data/api/action/datastore_search?resource_id="

destination_file = "origin_data_"

aux_logs_filename = "AUX_LOGS.txt"

num_jumps = 100 #Number of lines on each call. The higher the jump, the quicker the answer but also the more iterations

#Logs texts
connection_error_msg = "ERROR: Unable to reach the endpoint: " 
data_error_msg = "ERROR: Data has not the 'success' flag or is not a valid json. \nFull response:\n"
file_error_msg = "ERROR: Could not open file: "
success_msg = "Data updated at: "

#main
def extract(base_url, month, offset, jumps):
    time_now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    api_endpoint = base_url+months_ids[month]+'&offset='+str(offset)
    #Block 1: Retrieve data
    try:
        call_result = requests.get(api_endpoint).text
        #Data quality
        try:
            data = json.loads(call_result)
            if data['success']: 
                max_lines = data['result']['total']
                records = data['result']['records']
                new_entry =  [str(record['data'])+';'+
                             str(record['_id'])+';'+
                             str(record['idTram'])+';'+
                             str(record['estatActual'])+';'+
                             str(record['estatPrevist'])
                             for record in records]
                new_entry = '\n'.join(str(e) for e in new_entry)
            else:
                new_entry = data_error_msg + call_result
        except:
            new_entry = data_error_msg + call_result
    except:
        new_entry = connection_error_msg + api_endpoint + 'at: ' + time_now + '\n'
    
    #Block 2: Store results
    try:
        with open(destination_file+month+".csv", "a") as myfile:
            myfile.write(new_entry+'\n')
            myfile.close()
        log = success_msg + time_now + '\n'
    except:
        log = file_error_msg + destination_file+month+".csv" + '\n'

    #Block 3: Add logs
    with open(aux_logs_filename, "a") as myfile:
        myfile.write(log)
        myfile.close()
        
    #Block 4: Recursive
    if (max_lines):
        if (max_lines > (offset + jumps)):
            os.system('cls||clear')
            print('\n========================================')
            print('Calling to: ', base_url+months_ids[month])
            print('\nNumber of lines fetched: '+str(offset)+' of ' +str(max_lines))
            print('\nGo and enjoy a good cup of coffe in the meanwhile.')
            extract(base_url, month, offset + jumps, jumps)
        else:
            print('RESOURCE ' + month + ' FINISHED.')
    else:
        print('ERROR DURING PROCESS')
        

#genesis
for month, resource in months_ids.items():
    extract(base_url,month, 0, num_jumps)    