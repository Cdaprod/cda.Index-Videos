import pandas as pd

data = {
    "Ansible": [
        "ansible/roles/weaviate/tasks/main.yml",
        "ansible/roles/postgres/tasks/main.yml",
        "ansible/roles/airflow_master/tasks/main.yml",
        "ansible/roles/airflow_worker/tasks/main.yml",
        "ansible/roles/papermill/tasks/main.yml",
        "ansible/playbook.yml"
    ],
    "Terraform": [
        "terraform/provider.tf",
        "terraform/vpc.tf",
        "terraform/compute_resources.tf",
        "terraform/storage_resources.tf",
        "terraform/dns.tf",
        "terraform/variables.tf",
        "terraform/outputs.tf"
    ],
    "Airflow": [
        "airflow/dags/weaviate_dag.py",
        "airflow/dags/postgres_dag.py",
        "airflow/dags/custom_api_dag.py",
        "airflow/plugins/weaviate_operator.py",
        "airflow/plugins/postgres_operator.py",
        "airflow/plugins/custom_api_operator.py"
    ],
    "Papermill": [
        "papermill/notebooks/babyagi_template.ipynb",
        "papermill/notebooks/qa_vectorstore_template.ipynb",
        "papermill/notebooks/streamlit_frontend_template.ipynb",
        "papermill/execute_notebooks.py"
    ],
    "Integrations": [
        "integrations/weaviate/client.py",
        "integrations/postgres/client.py",
        "integrations/airtable/client.py",
        "integrations/customAPI/client.py"
    ],
    "Sample Projects": [
        "samples/video_archive/ingestion.py",
        "samples/video_archive/indexing.py",
        "samples/video_archive/metadata_generation.py",
        "samples/social_media_automation/social_media_pipeline.py"
    ]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame.from_dict(data, orient='index').transpose()

# Save the dataframe to a CSV file
csv_path = "/mnt/data/files_structure.csv"
df.to_csv(csv_path, index=False)

csv_path
