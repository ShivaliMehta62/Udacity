#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyspark.sql.functions import *


class Data_Quality_Check:
    """
    Validate and checks the model and data.
    """

    def __init__(self, spark, paths):
        self.spark = spark
        self.paths = paths

    def _get_demographics(self):
        """
        Get demographics dimension
        return demographics dimension
        """
        return self.spark.read.parquet(self.paths["demographics"])

    def _get_airports(self):
        """
        Get airports dimension
        return airports dimension
        """
        return self.spark.read.parquet(self.paths["airports"])

   
    def get_facts(self):
        """
        Get facts table
        :return: facts table
        """
        return self.spark.read.parquet(self.paths["facts"])

    def get_dimensions(self):
        """
        Get all dimensions of the model
        :return: all dimensions
        """
        return self._get_demographics(), self._get_airports()

    def exists_rows(self, dataframe):
        """
        Checks if there is any data in a dataframe
        :param dataframe: dataframe
        :return: true or false if the dataset has any row
        """
        return dataframe.count() > 0

    def check_integrity(self, fact, dim_demographics, dim_airports):
        """
        Check the integrity of the model. Checks if all the facts columns joined with the dimensions has correct values 
        :param fact: fact table
        :param dim_demographics: demographics dimension
        :param dim_airports: airports dimension
        :return: true or false if integrity is correct.
        """
        data_check_demo=fact.select(col("cod_state")).distinct().join(dim_demographics, fact["cod_state"]==dim_demographics\
        ["State_Code"],"left_anti").count()==0
        
        data_check_airport=fact.select(col("cod_port")).distinct().join(dim_airports, fact["cod_port"]==dim_airports\
        ["local_code"],"left_anti").count()==0
        
        
        return data_check_demo & data_check_airport

