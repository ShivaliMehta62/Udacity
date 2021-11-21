#!/usr/bin/env python
# coding: utf-8
from pyspark.sql import SparkSession, SQLContext, GroupedData
from pyspark.sql.functions import *
from pyspark.sql.functions import date_add as d_add
from pyspark.sql.types import DoubleType

# In[ ]:
class CleaningData:
    """
    Cleaning the original dataset
    """
    @staticmethod
    def get_demographics(demographics):
        """
        Clean demographics dataset, filling null values with 0 and grouping by city and state and pivot
        Race in diferent columns.
        returns cleaned demographics dataset
        """
        demogr = demographics.groupBy(col("City"), col("State"), col("Median Age"), col("male population"),
                                     col("female population") \
                                     , col("total population"), col("number of veterans"), col("foreign-born"),
                                     col("average household size") \
                                     , col("state code")).pivot("race").agg(sum("count").cast("integer")) \
            .fillna({"American Indian and Alaska Native": 0,
                     "Asian": 0,
                     "Black or African-American": 0,
                     "Hispanic or Latino": 0,
                     "White": 0})

        return demogr

    @staticmethod
    def get_airportcode(airports):
        """
        Clean airports dataset filtering only US airports and discarding anything else that is not an airport.
        Extract iso regions and cast as float elevation feet.
        returns cleaned airports dataframe 
        """
        airports = airports \
            .where(
            (col("iso_country") == "US") & (col("type").isin("large_airport", "medium_airport", "small_airport"))) \
            .withColumn("iso_region", substring(col("iso_region"), 4, 2)) \
            .withColumn("elevation_ft", col("elevation_ft").cast("float"))

        return airports

    @staticmethod
    def get_immigrations(immigration):
        """
        Clean the inmigrantion dataset. Rename columns with understandable names. Put correct formats in dates and s
        elect only important columns 
        returns cleaned immigration dataset
        """
        inmigration = immigration \
            .withColumn("cicid", col("cicid").cast("integer")) \
            .withColumnRenamed("i94addr", "cod_state") \
            .withColumnRenamed("i94port", "cod_port") \
            .withColumn("cod_visa", col("i94visa").cast("integer")) \
            .drop("i94visa") \
            .withColumn("cod_mode", col("i94mode").cast("integer")) \
            .drop("i94mode") \
            .withColumn("cod_country_origin", col("i94res").cast("integer")) \
            .drop("i94res") \
            .withColumn("cod_country_cit", col("i94cit").cast("integer")) \
            .drop("i94cit") \
            .withColumn("year", col("i94yr").cast("integer")) \
            .drop("i94yr") \
            .withColumn("month", col("i94mon").cast("integer")) \
            .drop("i94mon") \
            .withColumn("bird_year", col("biryear").cast("integer")) \
            .drop("biryear") \
            .withColumn("age", col("i94bir").cast("integer")) \
            .drop("i94bir") \
            .withColumn("counter", col("count").cast("integer")) \
            .drop("count") \
            .withColumn("data_base_sas", to_date(lit("01/01/1960"), "MM/dd/yyyy")) \
            .withColumn("arrival_date", expr("date_add(data_base_sas, arrdate)")) \
            .withColumn("departure_date", expr("date_add(data_base_sas, depdate)")) \
            .drop("data_base_sas", "arrdate", "depdate")

        return inmigration.select(col("cicid"), col("cod_port"), col("cod_state"), col("visapost"), col("matflag"),
                                  col("dtaddto") \
                                  , col("gender"), col("airline"), col("admnum"), col("fltno"), col("visatype"),
                                  col("cod_visa"), col("cod_mode") \
                                  , col("cod_country_origin"), col("cod_country_cit"), col("year"), col("month"),
                                  col("bird_year") \
                                  , col("age"), col("counter"), col("arrival_date"), col("departure_date"))
