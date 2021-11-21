from pyspark.sql import SparkSession



class SourceData:
    """
    Get the sources and return dataframes
    """

    def __init__(self, spark, paths):
        self.spark = spark
        self.paths = paths

    def _get_standard_csv(self, filepath, delimiter=","):
        """
        Get sources in CSV format
        :param filepath: csv file path
        :param delimiter: delimiter
        :return: dataframe
        """
        return self.spark.read.format("csv").option("header", "true").option("delimiter", delimiter).load(filepath)

    def get_demographics_raw(self):
        """
        Get demographics dataset
        :return: demographics dataset
        """
        return self._get_standard_csv(filepath=self.paths["demographics"], delimiter=";")

    def get_airports_raw(self):
        """
        Get airports dataset
        :return: airports dataset
        """
        return self._get_standard_csv(self.paths["airportcode"])

    def get_immigration_raw(self):
        """
        Get inmigration dataset.
        :return: inmigration dataset
        """
        return self.spark.read.parquet(self.paths["i94_path"])

    