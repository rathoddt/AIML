# BigTbale

### Resources

git clone https://github.com/ACloudGuru-Resources/Course_Google_Certified_Professional_Data_Engineer.git cloud-bigtable-examples

```
echo project = playground-s-11-63a33447 > ~/.cbtrc
echo instance = demo-bt >> ~/.cbtrc
```

Introduction to Cloud Bigtable  
https://cloud.google.com/bigtable/docs/overview  

https://codelabs.developers.google.com/codelabs/cloud-bigtable-intro-java/index.html#0

## Schema design best practices  
https://cloud.google.com/bigtable/docs/schema-design

Designing a Bigtable schema is different than designing a schema for a relational database. In Bigtable, a schema is a blueprint or model of a table, including the structure of the following table components:

- Row keys
- Column families, including their garbage collection policies
- Columns

In Bigtable, schema design is driven primarily by the queries, or read requests, that you plan to send to the table.

Scans are the most common way to read Bigtable data. You can read a range of contiguous rows or multiple ranges of rows from Bigtable, by specifying a row key prefix or specifying beginning and ending row keys. 

- Reading a range of rows
- Reading multiple ranges of rows
- Reading multiple rows using a key prefix


A secondary consideration is the avoidance of hotspots – to prevent hotspots, you need to consider write patterns and how you can avoid accessing a small key space in a short amount of time.


How twitter  they optimized their schema?  
Visualizing Cloud Bigtable Access Patterns at Twitter for Optimizing Analytics  

https://www.youtube.com/watch?v=3QHGhnHx5HQ&t=1574s




### Client libraries  
https://cloud.google.com/bigtable/docs/samples-python-hello