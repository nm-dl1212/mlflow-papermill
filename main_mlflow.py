from datetime import datetime
import papermill as pm

EXPERIMENT_NAME = f"exp_{datetime.now():%Y%m%d%H%M%S}"
NOTEBOOK_NAME = "main.ipynb"
OUTPUT_NOTEBOOK_NAME = "main_out.ipynb"

for i, c in enumerate(["blue", "red", "green"]):
    pm.execute_notebook(
        'main.ipynb',
        'main_out.ipynb',
        parameters=dict(
            EXPERIMENT_NAME=EXPERIMENT_NAME,
            NOTEBOOK_NAME=OUTPUT_NOTEBOOK_NAME,
            PARAMETERS={ 
                "datasetPath": "data/sample.csv",
                "color": c
            }
        )
    )