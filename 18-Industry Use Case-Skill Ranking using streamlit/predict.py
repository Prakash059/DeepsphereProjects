import sys
from flask import Flask, flash, request, redirect, url_for, render_template ,session
from skillset import data_scientist,data_engineer,Cloud_engineer,AI 
import subprocess
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/dsailabusr1/sangeeth/skillmatrix/vast-verve-292018-6f41b128c4b1.json'
import pandas as pd
from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1
from google.cloud.automl_v1.proto import service_pb2
from werkzeug.utils import secure_filename
import numpy as np
import json

UPLOAD_FOLDER='upload'


jobtitle=""

app = Flask(__name__)

app.secret_key = 'xyz'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'pdf'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_data():
        # check if the post request has the file part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')
        print(files)

        for file in files:
            if file and allowed_file(file.filename):

                #filename = secure_filename(file.filename)
                #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
                file.save("/home/dsailabusr1/sangeeth/skillmatrix/"+os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))


@app.route('/', methods=['GET', 'POST'])

def firstpage():
    if request.method == "POST":
        print("title")
        global jobtitle
        vAR_Job_Title1 = []
        job=int(request.form["title_name"])
        vAR_Job_Title1.append(job)
        print(vAR_Job_Title1[0])
        print(type(vAR_Job_Title1[0]))
        if vAR_Job_Title1[0]==1:
           jobtitle='data scientist'
        elif vAR_Job_Title1[0]==2:
            jobtitle='data engineer'
        elif vAR_Job_Title1[0]==3:
            jobtitle='Cloud engineer'
        elif vAR_Job_Title1[0]==4:
            jobtitle="AI Architect"

        temp=0
        temp+=1
        print(jobtitle)
    if request.method == "POST" and temp>=1:
        print("file")
        upload_data()

		
    return render_template("index.html")

@app.route('/redirect2', methods=['GET'])
def next2():
    
	return redirect(url_for("index2"))

@app.route('/index2', methods=['GET','POST'])
def index2():
    global jobtitle
    subprocess.call("rm -r /home/dsailabusr1/sangeeth/skillmatrix/static/upload", shell=True)
    subprocess.call("cp -r /home/dsailabusr1/sangeeth/skillmatrix/upload /home/dsailabusr1/sangeeth/skillmatrix/static/", shell=True)
    localfilepath=subprocess.check_output("ls /home/dsailabusr1/sangeeth/skillmatrix/static/upload/", shell=True)
    localfilepath=localfilepath.split("\n")[:-1]
    print(localfilepath)
    session['localfilepath']={'filenames':localfilepath,'jobtitle':jobtitle}
    print(session['localfilepath'])

    return render_template("index2.html", content=session['localfilepath'])

@app.route('/redirect3', methods=['GET'])
def next3():
    
	return redirect(url_for("index3"))

@app.route('/index3', methods=['GET','POST'])
def index3():
   subprocess.call("rm /home/dsailabusr1/sangeeth/skillmatrix/static/result.csv", shell=True) 
   model_name = "projects/vast-verve-292018/locations/us-central1/models/TEN8905826481683300352"
   move_filetobucket()
   files=getfilepath()
   allresume_skill=[]
   global jobtitle
   for i in files:
     response=get_prediction(i, model_name)
     skill=[]
     for annotation_payload in response.payload:
         text_segment = annotation_payload.text_extraction.text_segment
         skill.append(str(text_segment.content)) 
     cal_score=resume_ranking(jobtitle,skill)
     print(i)
     allresume_skill.append({'name':i.split('/')[-1],'skill':skill,'title':cal_score['Title'],'score':cal_score['Score']})

   df=pd.DataFrame(allresume_skill)
   df=df.sort_values('score',ascending=False)
   df['Rank'] = np.arange(1, len(df)+1)
   print(df)  
   final=df.to_dict('records')
   df.to_csv(r'/home/dsailabusr1/sangeeth/skillmatrix/static/result.csv')
   print(allresume_skill)
   print(type(allresume_skill))
   session['result']=final  

   return render_template("index3.html",content=session['result'])


def inline_text_payload(file_path):
  with open(file_path, 'rb') as ff:
    content = ff.read()
  return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def pdf_payload(file_path):
  return {'document': {'input_config': {'gcs_source': {'input_uris': [file_path] } } } }

def get_prediction(file_path, model_name):
  options = ClientOptions(api_endpoint='automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)

  #payload = inline_text_payload(file_path)
  # Uncomment the following line (and comment the above line) if want to predict on PDFs.
  payload = pdf_payload(file_path)

  params = {}
  request = prediction_client.predict(model_name, payload, params)
  return request  # waits until request is returned



def getfilepath():
    file_list1=subprocess.check_output("gsutil ls gs://skill_extraction/upload", shell=True)
    file_list=file_list1.split("\n")[:-1]
    return(file_list)


def resume_ranking(title,skills):
    if (title == 'data scientist'):
        #data_scientist = ['Python','R','SQL','Spark','Hadoop','Tableau','scala','Tableau','SAS','Java','AWS','Tensorflow','Hive','NumPy','MatLab','NoSQL','Azure','C++','Kafka','Scikit-learn','Keras','Torch','C','SPSS','Pyspark','Linux','Pig','Pandas','Qlik','Weka','Octave','MongoDB','Mahout','Caffe','D3.js','Grafana','Spotfire','Impala','UNIX','Apache lucene','Cognos','PowerBI','EC2','Lambda','Sagemaker','DynamoDB','Microsoft azure','Mxnet','AWS Neptune','Neo4j','Gensim','Go','Elasticsearch','Cassandra']
        skills_set = set(skills)
        data_scientist_set = set(data_scientist)
        common_set = skills_set & data_scientist_set
        common = list(common_set)
        global score
        score = 0
        global scores_dict
        scores_dict = {}
        for i in common:
            if (i == 'python' or i == 'Python'):
                score += 12
            elif (i == 'R' or i == 'r'):
                score += 11
            elif (i == 'SQL' or i == 'sql'):
                score += 10
            elif (i == 'Spark' or i == 'spark'):
                score += 9
            elif (i == 'Hadoop' or i == 'hadoop'):
                score += 8
            elif (i == 'Tableau' or i == 'tableau'):
                score += 8
            elif (i == 'scala' or i == 'Scala'):
                score += 7
            elif (i == 'SAS' or i == 'sas' ):
                score += 6
            elif (i == 'Java' or i == 'java' ):
                score += 6
            elif (i == 'AWS' or i == 'aws' ):
                score += 5
            elif (i == 'Tenserflow' or i == 'tenserflow' ):
                score += 5
                
        scores_dict = {"Title": title,
                       "Score": score}

        return scores_dict
    
    if (title == 'data engineer'):
        #data_scientist = ['SQL','Python','Spark','Java','scala','Hadoop','Kafka','Hive','AWS','NoSQL','Azure','Cassandra','Airflow','Redshift','MongoDB','UNIX','Tableau','Kubernetes','Agile','Linux','Hbase','Docker','AWS Athena','PigGo','Snowflake','Shell','MapReduce','RDBMS','Apache Flink','R','C++','Lambda','Elasticsearch','scrum','C','Pyspark','Impala','EC2','Googlecloud platform','Apache beam','Perl','SAS','Pandas','Qlik','Mahout','D3.js','PowerBI','Neo4j','AWS KMS','Apache ranger','Apache atlas','ArangoDB','Arrow','Luiji','AWS Firehose','Jupyter']
        skills_set = set(skills)
        data_engineer_set = set(data_engineer)
        common_set = skills_set & data_engineer_set
        common = list(common_set)
        #global score
        score = len(common)
        scores_dict = {}
        for i in common:
            if (i == 'SQL' or i == 'sql'):
                score += 12
            elif (i == 'python' or i == 'Python'):
                score += 11
            elif (i == 'Spark' or i == 'spark'):
                score += 10
            elif (i == 'Java' or i == 'java' ):
                score += 9
            elif (i == 'scala' or i == 'Scala'):
                score += 8
            elif (i == 'Hadoop' or i == 'hadoop'):
                score += 8
            elif (i == 'kafka' or i == 'Kafka'):
                score += 7
            elif (i == 'Hive' or i == 'hive' ):
                score += 6
            elif (i == 'Cassandra' or i == 'cassandra' ):
                score += 6
            elif (i == 'Airflow' or i == 'airflow' ):
                score += 5
        scores_dict = {"Title": title,
                       "Score": score}
        
        return scores_dict
    
    if (title == 'Cloud engineer'):
        #data_scientist = ['Go','Python','Azure','Linux','Java','SQL','Kubernetes','Docker','AWS RDS','scala','Googlecloud platform','Shell','AWS CLI','Terraform','CI/CD','AWS EC2','Chef','Paas','AWS VPC','UNIX','AWS Lambda','AWS S3','Vmware','.Net','NoSQL','Cassandra','Redshift','Perl','Spring','Spark','Hadoop','Tableau','Kafka','mysql','AWS Cloudwatch','AWS ELB','AWS IAM','Spring boot','Maven','Orchestration tools','Ruby','Saas','Cloud foundry','Hive','C#','C++','DynamoDB','Ruby','Amazon SNS','AWS SQS','Shell scripts','NodeJS','Gradle,Redhat' ,'SAS','PowerBI','Neo4j','Cosmos','Nifi','PHP','AWS Glacier','AWS WAF','AWS EFS','Spring MVC','Hudson','IBM blue mix','Superset','Jira','looker','Specflow','Octopusdeploy','Spring security','Tensorflow','SPSS','Pyspark','Pig','D3.js','Grafana','Spotfire','Impala','Elasticsearch','MapReduce','Snowflake','Unix shell','Cloudera','RabbitMQ','Alteryx','AWS Route53','AWS CloudFront','AWS Codebuild']
        skills_set = set(skills)
        Cloud_engineer_set = set(Cloud_engineer)
        common_set = skills_set & Cloud_engineer_set
        common = list(common_set)
        #global score
        score = len(common)
        #global scores_dict
        scores_dict = {}
        for i in common:
            if (i == 'Go' or i == 'go'):
                score += 12
            elif (i == 'python' or i == 'Python'):
                score += 11
            elif (i == 'Linux' or i == 'linux'):
                score += 10
            elif (i == 'Java' or i == 'java' ):
                score += 9
            elif (i == 'sql' or i == 'SQL'):
                score += 8
            elif (i == 'Kubernetes' or i == 'kubernetes'):
                score += 8
            elif (i == 'Docker' or i == 'docker'):
                score += 7
            elif (i == 'AWS RDS' or i == 'aws rds' ):
                score += 6
            elif (i == 'scala' or i == 'Scala' ):
                score += 6
            elif (i == 'Googlecloud platform' or i == 'googlecloud platform' ):
                score += 5
            elif (i == 'Shell' or i == 'shell' ):
                score += 4
            elif (i == 'AWS CLI' or i == 'aws cli' ):
                score += 4
        scores_dict = {"Title": title,
                       "Score": score}
        return scores_dict
    
    if (title == 'AI Architect'):
        #data_scientist = ['Python','Tensorflow','Java','Spark','Pytorch','Keras','Torch','SQL','Scikit-learn','Hadoop','R','scala','C++','Pandas','Azure','Docker','Googlecloud platform','Kafka','Kubernetes','NumPy','NoSQL','C#','Hive','Linux','Caffe','AWS Sagemaker','Go','Agile','Cassandra','Tableau','Airflow','Shell','CI/CD','MatLab','AWS EC2','Neo4j','Jupyter','RabbitMQ','Salesforce','Ruby','mysql,','SAS','Pyspark','Qlik','Mahout','D3.js','Grafana','Spotfire','Impala','UNIX','AWS Lambda','DynamoDB','Mxnet','MapReduce','Hbase','scrum','Redshift','Perl','kaldi','Sphinx','Word2Vec','Sentence2Vec','Wav2Vec','PHP','Perforce','Dataiku','PowerBI']
        skills_set = set(skills)
        AI_set = set(AI)
        common_set = skills_set & AI_set
        common = list(common_set)
         #global score
        score = len(common)
        #global scores_dict
        scores_dict = {}
        for i in common:
            if (i == 'python' or i == 'Python'):
                score += 12
            elif (i == 'Tensorflow' or i == 'tensorflow'):
                score += 11
            elif (i == 'Java' or i == 'java'):
                score += 10
            elif (i == 'Spark' or i == 'spark'):
                score += 9
            elif (i == 'Pytorch' or i == 'pytorch'):
                score += 8
            elif (i == 'Keras' or i == 'keras'):
                score += 8
            elif (i == 'Torch' or i == 'torch'):
                score += 7
            elif (i == 'SQL' or i == 'sql' ):
                score += 6
            elif (i == 'Scikit-learn' or i == 'scikit-learn' ):
                score += 6
            elif (i == 'Hadoop' or i == 'Hadoop' ):
                score += 5
            elif (i == 'R' or i == 'r' ):
                score += 5
            elif (i == 'scala' or i == 'Scala'):
                score += 4
            elif (i == 'C++' or i == 'c++'):
                score += 4
        
        scores_dict = {"Title": title,
                       "Score": score}
        return scores_dict 

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080,debug=True)
#    file_path = "/home/dsailabusr1/sangeeth/skillmatrix/sample.txt"
#    model_name = "projects/vast-verve-292018/locations/us-central1/models/TEN8905826481683300352"
#    move_filetobucket()
#    files=getfilepath()
#    allresume_skill=[]
#    for i in files:
#      response=get_prediction(i, model_name)
#      skill=[]
#      for annotation_payload in response.payload:
#          text_segment = annotation_payload.text_extraction.text_segment
#          skill.append(str(text_segment.content)) 
#      cal_score=resume_ranking('data scientist',skill)
#      allresume_skill.append({'name':i.split('/')[-1],'skill':skill,'title':cal_score['Title'],'score':cal_score['Score']})
#    df=pd.DataFrame(allresume_skill)
#    df=df.sort_values('score',ascending=False)
#    print(df)  





