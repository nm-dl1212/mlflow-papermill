import os
import sqlite3
import papermill as pm
import mlflow


for i, c in enumerate(["blue", "red", "green"]):
    pm.execute_notebook(
        'main.ipynb',
        'main_out.ipynb',
        parameters=dict(COLOR=c, EXPERIMENT_NAME=f'exp_{i:02}')
    )