#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyspark.sql import SparkSession, SQLContext, GroupedData
from pyspark.sql.functions import *
from pyspark.sql.functions import date_add as d_add
from pyspark.sql.types import DoubleType

from pyspark.sql.functions import *


class DataModelizer:
    """
    Modelizes the datawarehouse (star schema) from datasets. Creating the facts table and dimension tables.
    """

    def __init__(self, spark, paths):
        self.spark = spark
        self.paths = paths

    def _modelize_demographics(self, demographics):
        """
        Create de demographics dimension table in parquet.
        :param demographics: demographics dataset.
        """
        demographics.write.mode('overwrite').parquet(self.paths["demographics"])

    def _modelize_airports(self, airports):
        """
        Create de airports dimension table in parquet.
        :param airports: airports dataset
        """
        airports.write.mode('overwrite').parquet(self.paths["airports"])

    
     
    def _modelize_facts(self, facts):
        """
        Create facts table from immigration in parquet particioned by arrival_year, arrival_month and arrival_day
        """
        
        facts.write.partitionBy("arrival_year", "arrival_month", "arrival_day").mode('overwrite').parquet(
            self.paths["facts"])

    		
    def modelize(self, facts, dim_demographics, dim_airports):
        """
        Create the Star Schema for the Data Warwhouse
        :param facts: facts table, immigration dataset
        :param dim_demographics: dimension demographics
        :param dim_airports: dimension airports
        """
        facts = facts.join(dim_demographics, facts["cod_state"] == dim_demographics["State_Code"], "left_semi")\
        .join(dim_airports, facts["cod_port"] == dim_airports["local_code"], "left_semi") 

        self._modelize_demographics(dim_demographics)
        self._modelize_airports(dim_airports)
        self._modelize_facts(facts)
