import json
import subprocess
import boto3
import urllib2
import os
import urllib

def lambda_handler(event, context):

    response3 = urllib2.urlopen('http://google.com/')

    print "The URL is: ", response3.geturl()

 
    print response3.code
    

    if response3.code == 200:
        pingstatus = "success"
    else:
        pingstatus = "error"
        
    #return response
    return {
        'pingstatus': pingstatus,
        'statusCode': 200

       
    }
