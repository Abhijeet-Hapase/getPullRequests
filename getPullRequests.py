import requests
import yaml
from datetime import datetime,timedelta 
from prettytable import PrettyTable
import sys

def getPullRequests(owner,repo_name,request_status):

    #Define parameters
    receiver_email_list="jon.smith@test.com;alex.hewitt@test.com;scarlett.wilde@test.com;carl.ward@test.com"
    message_key='message'
    pull_request_counter=0
    # url to request for valdating repo name and getting pull request data
    try:
        check_repository_name=f"https://api.github.com/search/repositories?q="+repo_name
        get_pull_request_data = f"https://api.github.com/repos/"+owner+"/"+repo_name+"/pulls?state="+request_status+"&per_page=100"
    except TypeError:
        print("Invalid values passed as command line arguments.Please provide correct values")
        sys.exit(1)     

    # make the request and return the json or handle the exception
    try:
        validate_repo_Name=requests.get(check_repository_name).json()
        pull_request_data = requests.get(get_pull_request_data).json()
    except:
        print("Unable to fetch pull request data.Please validate below Values\n1.API Url\n3.Repository Owner Name\n4.Pull Request Status")
        sys.exit(1)

    #Check if response received contains valid data or not
    if (validate_repo_Name['total_count']==0):
        print("Invalid Repository Name.Please provide name of repository with valid name and is public as command line argument")
        sys.exit(1)
    if (message_key in pull_request_data and pull_request_data['message']=='Not Found'):
        print("Invalid Repository Owner Name.Please valid name provide as command line argument")
        sys.exit(1)    
        
    #Print the pull request data in email format
    print("From: getpullrequestdata@noreply.com\n")
    print("To:"+receiver_email_list+"\n")
    print("Subject: Pull Request Status : "+request_status)
    if (len(pull_request_data)==0):
        print("\nHello, \n\n No pull requests were raised for repository: "+repo_name+"\n")
        sys.exit(1)
    print("\nHello, \n\nPlease see below status of pull requests from last week for repository: "+repo_name+"\n")

    t=PrettyTable(["ID","Pull Request Title","State"])

    for i in  pull_request_data:

        if datetime.strptime(i['created_at'][:-1], '%Y-%m-%dT%H:%M:%S')>datetime.now()- timedelta(days=7):
            
            pull_request_counter+=1
            t.add_row([i['number'],i['title'],i['state']])

    t.align="l"
    print("Number of Pull Requests : "+str(pull_request_counter)+"\n\nPull Request Details:\n\n")
    print(t)
    print("\nThanks and Regards,\n\nAbhijeet Hapase\n")

if (len(sys.argv)<4):
    print("Please enter all parameters:\n1.Owner\t2.Repository Name\t3.Pull Request Status(open/closed/all)")
    sys.exit(1)
else:    
    getPullRequests(sys.argv[1],sys.argv[2],sys.argv[3])
