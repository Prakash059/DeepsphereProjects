import streamlit as st
from PIL import Image
import os
import base64
#from google.api_core.client_options import ClientOptions
#from google.cloud import automl_v1
import subprocess
#from google.cloud.automl_v1.proto import service_pb2

def local_css(file_name):
    
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            

def getfilepath():
    file_list1=subprocess.check_output("gsutil ls gs://skill_extraction/upload", shell=True)
    file_list=file_list1.split("\n")[:-1]
    return(file_list)
    
    
def get_prediction(file_path, model_name):
  options = ClientOptions(api_endpoint='automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)

  #payload = inline_text_payload(file_path)
  # Uncomment the following line (and comment the above line) if want to predict on PDFs.
  payload = pdf_payload(file_path)

  params = {}
  request = prediction_client.predict(model_name, payload, params)
  return request  # waits until request is returned


def inline_text_payload(file_path):
  with open(file_path, 'rb') as ff:
    content = ff.read()
  return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }


def pdf_payload(file_path):
  return {'document': {'input_config': {'gcs_source': {'input_uris': [file_path] } } } }
  

def result_prediction():
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

   
     
def move_filetobucket(): 
    subprocess.call("gsutil rm -r gs://skill_extraction/upload", shell=True)  
    subprocess.call("gsutil mv ./skillmatrix/upload gs://skill_extraction/", shell=True)
    subprocess.call('pwd')     
    
def JobTitle(Jobtitle):  

    if  Jobtitle == "Data Scientist":
        st.sidebar.header('Upload All Resume')
        
        datafile = st.sidebar.file_uploader("",type=['pdf'],accept_multiple_files=True)
        
        if st.button("Preview"):
            for file in datafile:
                if file is not None:
                    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
                    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">' 
                    st.markdown(pdf_display, unsafe_allow_html=True)
        
        if datafile is not None:
            for i in datafile:              
                with open(os.path.join("tempDir",i.name),"wb") as f:
                    f.write(i.getbuffer())         
          
        
    elif Jobtitle == "Data Engineer":
        st.sidebar.header('Upload All Resume')
        file=st.sidebar.file_uploader("Upload Resume", type="pdf",accept_multiple_files=True)
       
        
        
    elif Jobtitle == "Cloud Engineer":
        st.sidebar.header('Upload All Resume')
        file=st.sidebar.file_uploader("Upload Resume", type="pdf",accept_multiple_files=True)
      
        
    elif Jobtitle == "AI Architect":
        st.sidebar.header('Upload All Resume')
        file=st.sidebar.file_uploader("Upload Resume", type="pdf",accept_multiple_files=True)
      
        
    else:
        print("Select a JobTitle")
        
        
   
    
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

def main():
    main_bg = "design.png"
    main_bg_ext = "png"
    
    st.markdown(
    f"""<style>.reportview-container {{background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})}}</style>""",unsafe_allow_html=True)
    
    local_css("style.css")
    image1 = Image.open('logo.jfif')
  
    st.image(image1)
   
    html_temp = """
    <h2><font style="color:blue;text-align:center;"> Artificial Intelligence</font> Reinvents Recruitment and Significantly Reduces Candidates Qualifying Time by 90%<h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.sidebar.header('Select Job Title')
    Jobtitle=st.sidebar.selectbox("",["Select Job Title","Data Scientist","Data Engineer","Cloud Engineer","AI Architect"])
    JobTitle(Jobtitle)
        
    st.sidebar.write("you selected ",Jobtitle)
    
    if st.button("Run Model"):
        result=resume_ranking

if __name__ == '__main__':
    main()