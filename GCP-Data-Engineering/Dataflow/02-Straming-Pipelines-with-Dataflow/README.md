

bkt-dataflow-stream-0001

projects/playground-s-11-31963abe/topics/tweeps

projects/playground-s-11-31963abe/subscriptions/tweep-reader

```

python pipelines.py --streaming flag
```


Remember to activate the virtual Python environment in any terminal you use:
```
  cd tweeper
  source bin/activate
```
Activate the Tweep feed:
```
  python tweeper.py
```
Test the pipeline locally:
```
  python pipeline.py --streaming
```
Run the pipeline with Cloud Dataflow:
```
  python pipeline.py --streaming --runner DataflowRunner \
  --project <YOUR_PROJECT_NAME> \
  --temp_location gs://<YOUR_BUCKET_NAME>/temp \
  --staging_location gs://<YOUR_BUCKET_NAME>/staging \
  --region us-central1 \
  --job_name tweeps

  python pipelines.py --streaming --runner DataflowRunner \
  --project playground-s-11-31963abe \
  --temp_location gs://bkt-dataflow-stream-0001/temp \
  --staging_location gs://bkt-dataflow-stream-0001/staging \
  --region us-central1 \
  --job_name tweeps  
```