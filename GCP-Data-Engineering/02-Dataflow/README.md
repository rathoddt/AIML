# Dataflow

bkt-dataflow-ftr-0001

- Enbale Dataflow API
```

gcloud config set project   playground-s-11-31963abe

#Download dataflow example usin mvn command below
mvn archetype:generate \
      -DarchetypeGroupId=org.apache.beam \
      -DarchetypeArtifactId=beam-sdks-java-maven-archetypes-examples \
      -DarchetypeVersion=2.8.0 -DgroupId=org.example \
      -DartifactId=dataflow-lab -Dversion="0.1" \
      -Dpackage=org.apache.beam.examples -DinteractiveMode=false


export PROJECT_ID=playground-s-11-31963abe
export BUCKET_NAME=bkt-dataflow-ftr-0001

mvn -Pdataflow-runner compile exec:java \
      -Dexec.mainClass=org.apache.beam.examples.WordCount \
      -Dexec.args="--project=${PROJECT_ID} \
      --stagingLocation=gs://${BUCKET_NAME}/staging/ \
      --output=gs://${BUCKET_NAME}/output \
      --runner=DataflowRunner"
```

### Resources
https://beam.apache.org/documentation/programming-guide/


```
wget https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/wordcount.py

python3 -m \
    apache_beam.examples.wordcount \
    --project <project-name> \
    --runner DataflowRunner \
    --temp_location \
    gs:// <project-name> /temp \
    --output \
    gs:// <project-name> /results/output \
    --job_name dataflow-demo \
    --region australia-southeast1

python3 -m \
    apache_beam.examples.wordcount \
    --project playground-s-11-69d877d4 \
    --runner DataflowRunner \
    --temp_location \
    gs://gcp-pca-301410-69d877d4/temp \
    --output \
    gs://gcp-pca-301410-69d877d4/results/output \
    --job_name dataflow-demo \
    --region us-east1
```

