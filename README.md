Here are some simple, but cool scripts for extract, transform and load data from the <a href="http://opendata-ajuntament.barcelona.cat">Barcelona open data platform</a>.

Specifically, I'm retrieving data from the <a href="http://opendata-ajuntament.barcelona.cat/data/es/dataset/itineraris">itineraris</a> and the <a href="http://opendata-ajuntament.barcelona.cat/data/es/dataset/trams">trams</a> public databases.

The objective is to analyze the patterns of the traffic on the city of Barcelona. I'm using the traffic states as an indirect metric of the traffic habits.

### File list

At this moment, the available scripts are:

- <strong>Extractor</strong>: this script connects with the APIs of the database and stores the information on one different `.txt` file for each API endpoint. I've choosen the text format because I want to add error messages and warnings to the file. Another valid approach would be to use special codes for the errors, but I wanted to keep things simple. After the extraction, a transformer file will be responsible for apply the correct formats to the exported data.

- <strong>Bootstrap</strong>: since Nov 2017, the <a href="http://opendata-ajuntament.barcelona.cat">Open Data platform</a> offers the possibility to extract the historic data (without retrospectivity). With the bootstrap script we can extract all the  data in one single process. 

### Use

Install the requirements and run the scripts you need. In my personal project, I'm deploying the extractor files on AWS lambda functions, and I'm storing the results on S3.

Please, use these scripts with <strong>responsability</strong>: when you make a ETL process over an API, you're making multiple calls to the server in a loop, and the infrastructure will have to deal with all your petitions. If you don't have technical details about the limits of the back-end infrastructure you're calling, you may want to hold the number of calls per minute to a secure level. 

<strong>PS</strong>: If you're making a big extraction, sending an email to the sysadmins to prevent them will also be a friendly practice, and I'm sure they will be grateful to you :)

### License
Of course! MIT License <3

have fun!
