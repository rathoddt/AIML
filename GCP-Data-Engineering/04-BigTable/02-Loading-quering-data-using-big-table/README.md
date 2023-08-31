
# Demo: Loading and Querying Data with Cloud Bigtable
```
https://learn.acloud.guru/course/gcp-certified-professional-data-engineer/learn/3f7671dd-d630-11a2-588d-b91d4847f245/3026a961-b49a-b203-d93a-0b298f3820cf/watch
```
# Cloud Shell commands:
```
sudo apt remove java* -y

sudo bash -c 'cat << EOF >> /etc/apt/sources.list
deb http://archive.debian.org/debian/ stretch main contrib non-free
deb http://archive.debian.org/debian/ stretch-proposed-updates main contrib non-free
deb http://archive.debian.org/debian-security stretch/updates main contrib non-free
EOF'

sudo apt-get update

sudo apt-get install openjdk-8-jdk-headless -y

java -version

echo project = YOUR_PROJECT_NAME > ~/.cbtrc
echo instance = labinstance >> ~/.cbtrc

cat ~/.cbtrc

cbt listinstances

cbt createtable fires
cbt createfamily fires fwi
cbt createfamily fires metric

cbt ls fires

# Upload dataloader.py & forestfires.csv files to Google Cloud Shell

curl https://raw.githubusercontent.com/ACloudGuru-Resources/Course_Google_Certified_Professional_Data_Engineer/master/Demos/dataloader.py -O

curl https://raw.githubusercontent.com/ACloudGuru-Resources/Course_Google_Certified_Professional_Data_Engineer/master/Demos/forestfires.csv -O

vim dataloader.py

# Update your project name:
# project_name = 'YOUR_PROJECT_NAME'

sudo pip3 install google-cloud-bigtable

python3 dataloader.py

git clone https://github.com/ACloudGuru-Resources/Course_Google_Certified_Professional_Data_Engineer.git cloud-bigtable-examples

cd cloud-bigtable-examples/quickstart/

./quickstart.sh

scan 'fires'

scan 'fires', {ROWPREFIXFILTER => '2#2#', COLUMNS => 'metric:area'}

scan 'fires', {ROWPREFIXFILTER => '2#2#aug#', COLUMNS => 'metric:area'}

scan 'fires', {ROWPREFIXFILTER => '2#2#aug#', COLUMNS => 'metric'}
```



```
cd cloud-bigtable-examples/quickstart/
cat quickstart.sh 
./quickstart.sh 
sudo apt-get install google-cloud-sdk google-cloud-sdk-bigtable-emulator
./quickstart.sh 
mvn clean package exec:java -Dbigtable.projectID=playground-s-11-63a33447 -Dbigtable.instanceID=demo-bt
gcloud init
mvn clean package exec:java -Dbigtable.projectID=playground-s-11-63a33447 -Dbigtable.instanceID=demo-bt
echo project = playground-s-11-63a33447 > ~/.cbt
echo instance = demo-bt > ~/.cbt
echo project = playground-s-11-63a33447 > ~/.cbtrc
echo instance = demo-bt > ~/.cbtrc
cat ~/.cbtrc
echo project = playground-s-11-63a33447 >> ~/.cbtrc
cat ~/.cbtrc
cbt listinstances
cbt listclusters
cbt ls
gcloud config set project       playground-s-11-63a33447
cbt listinstances
cbt createtable fires
cbt createfamily fires fwi
cbt ls fires
cbt createfamily fires metric
cbt ls fires
ls
vim dataloader.py 
sudo pip install google-cloud-bigtable
payhton3 dataloader.py 
pyhton3 dataloader.py 
python3 dataloader.py 
git clone https://github.com/GoogleCloudPlatform/cloud-bigtable-examples.git
```


https://www.scribd.com/document/501036817/IOT-Analytics-for-the-Internet-of-Things-IoT-Packt


https://www.scribd.com/document/513453064/Internet-of-Things-a-Hands-On-Approach-by-Arshdeep-Bahga-Vijay-Madisetti