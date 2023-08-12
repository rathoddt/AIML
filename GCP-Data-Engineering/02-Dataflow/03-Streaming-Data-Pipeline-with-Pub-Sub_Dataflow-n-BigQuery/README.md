# Create a Streaming Data Pipeline on GCP with Cloud Pub/Sub, Dataflow, and BigQuery
Introduction

This lab will simulate live highway sensor data which will be published to a Cloud Pub/Sub topic. Then, a Cloud Dataflow streaming pipeline will subscribe to it. The pipeline will take the streaming sensor data, transform it, and insert it into a BigQuery table. We will then view the streaming inserts in BigQuery while they are in progress, and attempt to gain some useful insights from the streaming data.

### Solution


### Prepare Your Environment

1. Click the Activate Cloud Shell icon along the top of the page, then click Continue to open Cloud Shell.
2. Enable the pubsub and dataflow APIs:
```
    gcloud services enable dataflow.googleapis.com

    gcloud services enable pubsub.googleapis.com
```    
3. Create a Cloud Storage bucket for Dataflow staging:
```
    gsutil mb gs://$DEVSHELL_PROJECT_ID
```
4. Clone the GitHub repository used for lab resources:
```
    cd ~

    git clone https://github.com/ACloudGuru-Resources/googledataengineer
```

### Create a Pub/Sub Topic

5. Create your topic and name it sandiego:
```
    gcloud pubsub topics create sandiego
```
6. Navigate to the GCP web console in a new tab to verify the topic was created.

7. Click the navigation menu icon in the top left corner, then scroll down to the Big Data section and select Pub/Sub. On the Topics tab, you should see your newly created sandiego topic.

8. Create a BigQuery Dataset to Stream Data Into

    Navigate back to Cloud Shell.

9. Create a BigQuery dataset to stream data into:
```
    bq mk --dataset $DEVSHELL_PROJECT_ID:demos
```
        Note: The table will be named average_speeds. We do not create the table, but Dataflow will create it within the dataset for us.

    Navigate back to the GCP web console to verify the dataset was created.

    Click the navigation menu icon, then scroll down to the Big Data section and select BigQuery. You should see your project name and a dataset called demos.

10. View the Dataflow Template

Navigate back to Cloud Shell.
Review the Apache Beam template Dataflow will use:
```    
    vim googledataengineer/courses/streaming/process/sandiego/src/main/java/com/google/cloud/training/dataanalyst/sandiego/AverageSpeeds.java
```    
Press the Esc key, then type :q! to exit out of the file without making any changes.

Create the Dataflow Streaming Job

Open your cloned GitHub directory:
```    
    cd ~/googledataengineer/courses/streaming/process/sandiego
```    
List the existing files:
    ls
Execute the script that creates the Dataflow streaming job:
```
    ./run_oncloud.sh $DEVSHELL_PROJECT_ID $DEVSHELL_PROJECT_ID AverageSpeeds
```    
 Navigate back to the GCP web console to verify the streaming job was successful.
 

 Click the navigation menu icon, then scroll down to the Big Data section and select Dataflow. You should see your streaming job is waiting for input.
 

 Use the navigation menu to select Pub/Sub, then select Subscriptions in the sidebar menu. Note that your subscription is now subscribed to your Dataflow topic.

Publish Simulated Traffic Sensor Data to Pub/Sub via a Python Script and Pre-Created Dataset

Navigate back to Cloud Shell.
11. Install any requirements for the Python script:
 ```   
 pip3 install google-cloud-pubsub
 ```
 Change directory into the folder that will use the Python script to simulate data:
 ```
    cd ~/googledataengineer/courses/streaming/publish
```
View the existing files:
ls
Download the simulated sensor data:
```
gsutil cp gs://la-gcloud-course-resources/sandiego/sensor_obs2008.csv.gz .
```
View the files again, and note that sensor_obs2008.csv.gz is now listed.
ls
Execute the Python script to publish simulated streaming data to Pub/Sub:
```
./send_sensor_data.py --speedFactor=60 --project=$DEVSHELL_PROJECT_ID
```
### View the Streamed Data in BigQuery

 Navigate back to the GCP web console and use the navigation menu to select Dataflow.
    

 Select your streaming job. You can see all the transforms your data is going through before it is inserted into the BigQuery dataset and table.
 
 Select the navigation menu icon, then scroll down to Big Data and select BigQuery.

Expand your project ID on the left, then expand the demos dataset.
Select the average_speeds table, then review the Details and Preview data. If no data displays, this indicates the data is sitting in the streaming buffer.

Click Query table and run the following query to view the current streamed data:
```
    SELECT *

    FROM `<DATABASE_NAME>.demos.average_speeds` LIMIT 1000
```
Remember that the database name in the query will be different.

Notice the total count of records at the bottom. Wait about a minute and run the same query again (be sure to uncheck use cached results in the query options) and notice that the number has increased.
Use Aggregated Queries to Gain Insights


Run the following query to view which highway lanes have the most sensor counts:
```
    SELECT lane, sum(lane) as total

    FROM `demos.average_speeds`

    GROUP BY lane

    ORDER BY total DESC
```
Run the following query to view which lanes have the highest average speeds:
```
    SELECT lane, avg(speed) as average_speed

    FROM `demos.average_speeds`

    GROUP BY lane

    ORDER BY average_speed DESC
```