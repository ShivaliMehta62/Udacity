# Capstone Project


## Content
This project aims to enrich the US i94 immigration data with further data such as US airport data, US demographic data to have a wider basis for analysis on the immigration data. The idea is to take multiple disparate data sources, filter the data and process it through the ETL pipeline to produce usable data set for analytics.

Analysis that can be done on final data set:

- For a given port city, how many immigrants enter from which country?
- What are the demographics of the port city?
- When did the highest immigrations happened?
- When did the least number of immigrations happened?
- Which gender had the higher number of immigrations?


## Project Description
In this project, I've built a datawarehouse with Spark in parquet file format. To complete the project, I've defined fact and dimension tables for a star schema for a particular analytic focus, and wrote an ETL pipeline.

## Data Cleaning
- Clean demographics dataset, filling null values with 0 and grouping by city and state and pivot Race in diferent columns.
- Clean airports dataset filtering only US airports and discarding anything else that is not an airport.
- Extract iso regions and cast as float elevation feet.


## Data Model
The schema used in this project is STAR Schema. This model has simple structure and is easy-to-understand, focusing on the fact table(immigrations) to store large transactional and measurable data and two dimension tables (airport and demographics) that store attributes about the data . This project will pull data from all sources and create fact and dimension tables to show movement of immigration in US. The below data dictonary explains the tables that are bring used in this data model.

## Fact Tables

#### Immigrations 
##### Stores all information related to immigrations

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

## Dimension Tables

#### Airports
##### Contains information related to airport data.
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
##### Stores all information related to demographics.
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


## Tools and technologies used
1. Python
2. Spark
3. Jupyter Notebook


# Data Updation
I recommend updating data on monthly basis.

# FAQ: What would I do if

1. The data was increased by 100x.
- Spark can process data efficiently.

2. The data populates a dashboard that must be updated on a daily basis by 7am every day.
- Use Airflow and create DAG that performs the logic of described pipeline. To monitor any failures, Airflow built-in feature to send automated emails can be used. 

3. The database needed to be accessed by 100+ people.
- Amazon Redshift can be used to store large data that can be efficiently accessed by multiple users.
