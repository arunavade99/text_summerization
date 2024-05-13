from project.summerization.text_summerization.config.configuration import ConfigurationManager
from project.summerization.text_summerization.src.textSummarizer.conponents.data_ingestion import DataIngestion
from project.summerization.text_summerization.src.textSummarizer.logging import logging as logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()