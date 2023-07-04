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

def backend_python(payload):

    # Get the environment variables
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" ######################START####################")
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" Get the environment variables...")

    a = json.loads(payload)
    OPERATION_NAME = a['operation'],
    SUBOPERATIONS = a['subOperation'],
    REGION_NAME = a['region'],
    ENVIRONMENT_NAME = a['environment'],
    DATABRICKS_TOKEN = a['token'],
    SCOPE_NAME = a['scope'],
    KEY = a['key'],
    PASSWORD = a['PASSWORD'],
    EMAIL_ID = a['email']




    v_novid = 'BHATTAD5'  #521ID
    v_jentoken = '113a34d995c633dc21b72f7a14cbf33c03' #API token
    jenkins_url = 'https://jenkins-f1devops-prdintranet-ie.aws.novartis.net'
    job_name = '/F1_ALL_ALL_UCE/AUTOMATION/FUCE/FUCE-3781-Scope-automation/'




 



    #Create a jenkins object
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" Create a jenkins object for ...")
    jenkins = Jenkins(jenkins_url,auth=(v_novid, v_jentoken),verify=False)
    print(jenkins)
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" generate the parameters for the job ...")
    #targetpolicyname=policy_prefix+v_projectid
    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+" Submit the job ...")

    try:
        item = jenkins.build_job(job_name,OPERATION_NAME = OPERATION_NAME,SUBOPERATIONS = SUBOPERATIONS,  REGION_NAME = REGION_NAME, ENVIRONMENT_NAME = ENVIRONMENT_NAME, DATABRICKS_TOKEN = DATABRICKS_TOKEN, SCOPE_NAME = SCOPE_NAME, KEY = KEY, PASSWORD = PASSWORD,EMAIL_ID = EMAIL_ID)
    #except e.AuthenticationError:
    #    print(e)
    #    raise SystemExit(f"Authentication Error. Exiting ...")
    except Exception as error:
      raise SystemExit(f"Received error : {error}")


    print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+"Below is the queueitem number of the jenkins job submitted ...")
    #print(item)
    time.sleep(20)
    build=item.get_build()
  # print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+"Below is the build URL of the job that has been submitted...")
  # print("ad1", build)
  # print("ad2", str(build).split(" ")[1][:-2])
    build_url=str(build).split(" ")[1][:-2]
    #print(build_url)
    url  = str(build_url)+"/api/json"
    #print(url)
    return build_url

    '''while True:

        data = requests.get(url,auth=(v_novid,v_jentoken),verify=False).json()
        print(dt.now().strftime('%Y-%m-%d %H:%M:%S')+"Below are the job details...")
        print(data)
        if data['building']:
            print("Job is in progress...")
            time.sleep(120)
        elif data['result'] == "SUCCESS":
            status = "Job is success"
            break
        elif (data['result'] == "FAILURE"):
            print(data['result'])
            status=data['result']
            raise SystemExit(f"Received error as the job status is --> "+status)'''
    




 