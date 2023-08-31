# BigQuery


Search for top 5 most expensive products
```
SELECT product, retailPrice FROM `<YOUR_PROJECT>.<YOUR_DATASET>.products` ORDER BY retailPrice DESC LIMIT 5;
```
Search for happy customer comments
```
SELECT name, email, customer_id, comment FROM `<YOUR_PROJECT>.<YOUR_DATASET>.comments` WHERE rating = 5 LIMIT 5;
```
Compare unit and retail prices
```
SELECT SKU, supplier, unitPrice, retailPrice FROM `<YOUR_PROJECT>.<YOUR_DATASET>.products`;
```



Loading CSV data from Cloud Storage
https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv

Loading JSON data from Cloud Storage
https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json