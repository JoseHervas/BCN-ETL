Here are some simple, but cool scripts for extract, transform and load data from the <a href="http://opendata-ajuntament.barcelona.cat">Barcelona open data platform</a>.

Specifically, I'm retrieving data from the <a href="http://opendata-ajuntament.barcelona.cat/data/es/dataset/itineraris">itineraris</a> and the <a href="http://opendata-ajuntament.barcelona.cat/data/es/dataset/trams">trams</a> public databases.

The objective is to analyze the patterns of the traffic on the city of Barcelona. I'm using the traffic states as an indirect metric of the traffic habits.

#### File list

At this moment, the available scripts are:

- <strong>Unit extractor</strong>: this script connects with the APIs of the database and stores the information on one different `.txt` file for each API endpoint. I've choosen the text format because I want to add error messages and warnings to the file. Another valid approach would be to use special codes for the errors, but I wanted to keep things simple. After the extraction, a transformer file will be responsible for apply the correct formats to the exported data.

- <strong>Aggregated extractor</strong>: since Nov 2017, the Open Data platform offers the possibility to extract the information aggregated by months, so I'm working on a new extractor script which will be more useful to make a initial bootstrap with the full historic data.  

#### Use

Install the requirements and run the scripts you need. In my personal project, I'm deploying the extractor files on AWS lambda functions, and I'm storing the results on S3.

#### License
Of course! MIT License <3

have fun!
