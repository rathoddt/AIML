# Course topics
- building data transformation pipelines to BigQuery using Dataprep by Trifacta;
- using Cloud Storage, Dataflow, and BigQuery to build extract, transform, and load (ETL) workflows;
- and building machine learning models using BigQuery ML.
  
## Creating a Data Transformation Pipeline with Cloud Dataprep
### Task 1. Open Dataprep in the Google Cloud console
```
#Create cloud identity
gcloud beta services identity create --service=dataprep.googleapis.com
```

<img width="1600" height="676" alt="image" src="https://github.com/user-attachments/assets/67b07632-8d63-4ac5-b7ec-25d74e11a63a" />

### Task 2. Creating a BigQuery dataset
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

### Task 3. Connecting BigQuery data to Cloud Dataprep
- Create new flow `Ecommerce Analytics Pipeline`

### Task 4. Exploring ecommerce data fields with the UI

