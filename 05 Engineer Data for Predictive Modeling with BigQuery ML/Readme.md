# Course topics
- building data transformation pipelines to BigQuery using Dataprep by Trifacta;
- using Cloud Storage, Dataflow, and BigQuery to build extract, transform, and load (ETL) workflows;
- and building machine learning models using BigQuery ML.
  
## I. Creating a Data Transformation Pipeline with Cloud Dataprep
#### Task 1. Open Dataprep in the Google Cloud console
```
#Create cloud identity
gcloud beta services identity create --service=dataprep.googleapis.com
```

<img width="1600" height="676" alt="image" src="https://github.com/user-attachments/assets/67b07632-8d63-4ac5-b7ec-25d74e11a63a" />

#### Task 2. Creating a BigQuery dataset
Create BigQuery  dataset `ecommerce`
```
#standardSQL
 CREATE OR REPLACE TABLE ecommerce.all_sessions_raw_dataprep
 OPTIONS(
   description="Raw data from analyst team to ingest into Cloud Dataprep"
 ) AS
 SELECT * FROM `data-to-insights.ecommerce.all_sessions_raw`
 WHERE date = '20170801'; # limiting to one day of data 56k rows for this lab
```

#### Task 3. Connecting BigQuery data to Cloud Dataprep
- Create new flow `Ecommerce Analytics Pipeline`

#### Task 4. Exploring ecommerce data fields with the UI




## II. ETL Processing on Google Cloud Using Dataflow and BigQuery (Python)

#### Task 1. Download the starter code
```
gcloud storage cp -r gs://spls/gsp290/dataflow-python-examples .
export PROJECT=qwiklabs-gcp-04-13a7b788ff3f
gcloud config set project $PROJECT
```
#### Task 2. Create a Cloud Storage bucket and copy files to the bucket
```
gcloud storage cp gs://spls/gsp290/data_files/usa_names.csv gs://$PROJECT/data_files/
gcloud storage cp gs://spls/gsp290/data_files/head_usa_names.csv gs://$PROJECT/data_files/
```
#### Task 3. Create a BigQuery dataset
```
bq mk lake
```

### Task 4. Review and run the data ingestion pipeline
The data ingestion pipeline ingests data from Cloud Storage into the BigQuery table using a TextIO source and a BigQueryIO destination. Specifically, the pipeline:

- Ingests the files from Cloud Storage.
- Filters out the header row in the files.
- Converts the lines read to dictionary objects.
- Outputs the rows to BigQuery.

Review the Python code for the data ingestion pipeline. Navigate to dataflow_python_examples > dataflow_python_examples, and open the data_ingestion.py file.

Set up the Docker container for the Dataflow jobs
```
cd ~
docker run -it -e PROJECT=$PROJECT -v $(pwd)/dataflow-python-examples:/dataflow python:3.8 /bin/bash

pip install apache-beam[gcp]==2.59.0
#Next, in the running container in the Cloud Shell, change directories into where you linked the source code:
cd dataflow/
export PROJECT=qwiklabs-gcp-04-13a7b788ff3f

python dataflow_python_examples/data_ingestion.py \
  --project=$PROJECT \
  --region=europe-west1 \
  --runner=DataflowRunner \
  --machine_type=e2-standard-2 \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --input gs://$PROJECT/data_files/head_usa_names.csv \
  --save_main_session
```

