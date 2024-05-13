from project.summerization.text_summerization.src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from project.summerization.text_summerization.src.textSummarizer.logging import logging as logger

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e