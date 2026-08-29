"""
Re-train model using existing artifacts from a previous successful run.
This bypasses the data ingestion step (which requires MongoDB connection).
"""
import sys
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import ModelTrainerConfig, TrainingPipelineConfig
from networksecurity.entity.artifact_entity import DataTransformationArtifact

if __name__ == "__main__":
    try:
        # Use the latest successful artifacts
        LATEST_ARTIFACT = "Artifacts/08_24_2026_22_41_20"

        trainingpipelineconfig = TrainingPipelineConfig()

        # Construct DataTransformationArtifact manually from existing files
        data_transformation_artifact = DataTransformationArtifact(
            transformed_object_file_path=f"{LATEST_ARTIFACT}/data_transformation/transformed_object/preprocessing.pkl",
            transformed_train_file_path=f"{LATEST_ARTIFACT}/data_transformation/transformed/train.npy",
            transformed_test_file_path=f"{LATEST_ARTIFACT}/data_transformation/transformed/test.npy",
        )
        print(f"Using transformation artifacts from: {LATEST_ARTIFACT}")

        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        logging.info("Model training started (retrain using existing artifacts)")
        model_trainer = ModelTrainer(
            model_trainer_config=model_trainer_config,
            data_transformation_artifact=data_transformation_artifact,
        )
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model training completed")
        print(model_trainer_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
