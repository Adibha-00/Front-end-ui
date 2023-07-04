import json
import os
import boto3
import sys
import requests
import api4jenkins
import argparse
from datetime import datetime as dt ,timedelta
from api4jenkins import Jenkins,exceptions as e
import time
requests.packages.urllib3.disable_warnings()

 

 

 

 

  
if __name__ == "__main__":
    # Get the environment variables
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" ######################START####################")
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" Get the environment variables...")

 


    Cluster_ID = "0116-114242-tok3zd3a"
    deploy_branch = "feature/alpha-orbitic"
    deploy_folder = "feature-raw-fdo-inet-sz"
    tag_name = "default"
    onboard_url = "https://vpce-089989da2b91e2907-eh86vkc4.execute-api.eu-west-1.vpce.amazonaws.com/dev/"
    print("log2",os.environ)
    print("log1",os.environ['JENKINS_URL'])

 

 

    v_novid = 'BHATTAD5'  #521ID
    v_jentoken = '113a34d995c633dc21b72f7a14cbf33c03' #API token
    jenkins_url = 'https://jenkins-f1devops-prdintranet-ie.aws.novartis.net'
    job_name = '/F1_ALL_ALL_DE_SHARED/subgroup-pipelines/Feature_UCE_pipelines_E2/feature-raw-inet-sz/'

 

 

    #Create a jenkins object 
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" Create a jenkins object for ...")
    jenkins = Jenkins(jenkins_url,auth=(v_novid, v_jentoken),verify=False)
    print(jenkins)
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" generate the parameters for the job ...")
    #targetpolicyname=policy_prefix+v_projectid
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" Submit the job ...")
    try:
        item = jenkins.build_job(job_name,Cluster_ID=Cluster_ID,deploy_branch=deploy_branch,deploy_folder=deploy_folder,tag_name=tag_name,onboard_url=onboard_url) 
    #except e.AuthenticationError:
    #    print(e)
    #    raise SystemExit(f"Authentication Error. Exiting ...") 
    except Exception as error:
      raise SystemExit(f"Received error : {error}")

 

 

    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+"Below is the queueitem number of the jenkins job submitted ...")
    #print(item)
    time.sleep(20)
    build=item.get_build()
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+"Below is the build URL of the job that has been submitted...")
  # print("ad1", build)
  # print("ad2", str(build).split(" ")[1][:-2])

    build_url=str(build).split(" ")[1][:-2]
    print(build_url)
    url  = str(build_url)+"/api/json" 
    print(url)

 

 

 

    while True:
        data = requests.get(url,auth=(v_novid,v_jentoken),verify=False).json()
        print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+"Below are the job details...")
        print(data)
        if data['building']:
            print("Job is in progress...")
            time.sleep(120)
        elif data['result'] == "SUCCESS":
            print("Job is success")
            break
        elif (data['result'] == "FAILURE"):
            print(data['result'])
            status=data['result']
            raise SystemExit(f"Received error as the job status is --> "+status)