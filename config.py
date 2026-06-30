import os
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 8000

MONGO_USERNAME = "test"
MONGO_PASSWORD = "Velo$123"

MONGO_URL = f"mongodb+srv://test:{MONGO_PASSWORD}@docdb-cluster-20260630-1826.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
db_name = 'test_db'

user_collection_name = 'collection_user'
data_collection_name = "collection_data"
INPUT_DATA_PATH = os.path.join(os.getcwd(), "data", "medical_insurance.csv")
ML_MODEL_PATH = os.path.join(os.getcwd(),"artifacts","linear_reg_med_ins.pkl")

STD_SCALER_FILE_PATH = os.path.join(os.getcwd(), "artifacts", "std_scaler_med_ins.pkl")

INPUT_COLUMN_DATA = os.path.join(os.getcwd(), "artifacts", "med_ins_column_data.json")