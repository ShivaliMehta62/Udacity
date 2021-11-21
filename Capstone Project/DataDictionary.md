## DATA DICTIONARY

### Dimension Tables

#### Airports

| Columns | DataType | Description
| :-: | :-: | :-: |
| iata_code    | VARCHAR Primary Key | IATA Code 
| name         | VARCHAR  | Name
| type         | VARCHAR  | Size Of Airport
| local_code   | VARCHAR  | Local Code
| coordinates  | VARCHAR  | Coordinated
| elevation_ft | FLOAT    | Elevation In Feet
| ident        | VARCHAR  | Airport Id 
| continent    | VARCHAR  | Continent
| iso_country  | VARCHAR  | Country (ISO-2)
| iso_region   | VARCHAR  | Region (ISO-2)
| municipality | VARCHAR  | Municipality
| gps_code     | VARCHAR  | GPS code

#### Demographics

| Columns | DataType | 
| :-: | :-: |
|city 					| VARCHAR    |
|state 					| VARCHAR    |
|median_age 			| FLOAT      |
|male_population 		| numeric    |
|female_population 		| numeric    |
|total_population 		| numeric    |
|state_code   			| VARCHAR(2) |
|American_indian_and_alaskan_native| Long|
|Asian                  | long |
|Black_or_African_American | long |
|Hispanic_or_latino | long |
|White | long |
|male_population_ratio | double |
|female_population_ratio | double |
|American_indian_and_alaskan_native_ratio | double |
|Asian_ratio | double |
|Black_or_African_American_ratio | double |
|Hispanic_or_latino_ratio  | double |
|White_ratio | double |


### Dimension Tables

#### Immigrations
| Columns | DataType | 
| :-: | :-: |
cic_id        	   | integer |
cod_port      	   | string  |
cod_state     	   | string  |
visapost      	   | string  |
matflag       	   | string  |
dtaddto       	   | string  |
gender        	   | string  |
airline       	   | string  |
admnum        	   | double  |
fltno         	   | string  |
visatype      	   | string  |
cod_visa      	   | integer |
cod_mode      	   | integer |
cod_country_origin | integer |
cod_country_cit    | integer |
year               | integer |
month              | integer |
bird_year          | integer |
age                | integer |
counter            | integer |
arrival_date       | date    |
departure_date     | date    |
arrival_year       | integer |
arrival_month      | integer |
arrival_day        | integer |