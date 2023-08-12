# DataProc

dataproc-bkt-00001
dataproc-bkt-00002

```
gcloud dataproc jobs submit pyspark word-count.py --cluster=cluster-d938 --region=us-east1 -- gs://dataproc-bkt-00002/inputs/2600-0.txt gs://dataproc-bkt-00002/outputs/


gsutil gs://dataproc-bkt-00002/outputs/
gsutil ls gs://dataproc-bkt-00002/outputs/
gsutil cp gs://dataproc-bkt-00002/outputs/* .
ls
wc -l part-00000 
wc -l part-00001 
cat part-00001 >> part-00000
wc -l part-00000 
cat part-00000 | sort -k 2
```

### resources
https://www.gutenberg.org/ebooks/2600

