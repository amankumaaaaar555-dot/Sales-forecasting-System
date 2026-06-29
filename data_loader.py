"""
data_loader.py

Handles loading datasets into pandas DataFrames.

Supported:
- Default project dataset
- User uploaded CSV

Author: Aman Kumar
Project: Sales Forecasting System
"""

import logging
from pathlib import Path

import pandas as pd

from config import (
    DATASET_FOLDER,
    DEFAULT_DATASET_NAME,
)

# ==========================================================
# Logger Configuration
# ==========================================================

logger = logging.getLogger(__name__)


# ==========================================================
# Load Dataset
# ==========================================================

def load_dataset(uploaded_file=None):
    """
    Load a dataset.

    Parameters
    ----------
    uploaded_file : UploadedFile | None

    Returns
    -------
    pandas.DataFrame
    """

    try:

        # ---------------------------------------
        # User Uploaded Dataset
        # ---------------------------------------

        if uploaded_file is not None:

            logger.info("Loading uploaded dataset...")

            df = pd.read_csv(uploaded_file)

            logger.info("Uploaded dataset loaded successfully.")

            return df

        # ---------------------------------------
        # Default Dataset
        # ---------------------------------------

        dataset_path = DATASET_FOLDER / DEFAULT_DATASET_NAME

        if not dataset_path.exists():

            raise FileNotFoundError(
                f"Default dataset '{DEFAULT_DATASET_NAME}' not found."
            )

        logger.info(f"Loading dataset: {dataset_path.name}")

        df = pd.read_csv(dataset_path)

        logger.info("Default dataset loaded successfully.")

        return df

    except Exception as e:

        logger.exception("Dataset loading failed.")

        raise 