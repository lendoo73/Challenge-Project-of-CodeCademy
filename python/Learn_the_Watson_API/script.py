import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV3
import os                 # to use environment variable

def analyze(handle):
    #The Twitter API credentials
    twitter_consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    twitter_consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    twitter_access_secret = os.getenv('TWITTER_ACCESS_SECRET')

    twitter_api = twitter.Api(
        consumer_key = twitter_consumer_key, 
        consumer_secret = twitter_consumer_secret, 
        access_token_key = twitter_access_token, 
        access_token_secret = twitter_access_secret
    )

    statuses = twitter_api.GetUserTimeline(
        screen_name = handle, 
        count = 200, 
        include_rts = False
    )

    text = ""

    for status in statuses:
        if status.lang == "en":
            #English tweets
            text += status.text

    text = text.encode("utf-8")
    #print(text)

    # This url is available from the manage page of the service
    url = os.getenv('PERSONALITY_INSIGHTS_URL')
    # this is your API key:
    apikey = os.getenv('PERSONALITY_INSIGHTS_APIKEY')

    # Create conection to service:
    service = PersonalityInsightsV3(
        url = url, 
        version = '2017-10-13', 
        iam_apikey = apikey
    )

    # Send file to service and get result:
    profile = service.profile(
        text, 
        content_type = "text/plain",
        accept = 'application/json'
    ).get_result()

    # Check for any warnings
    #print(f"Warnings ({handle}): ", profile["warnings"])
    #print(f"Result ({handle}): ",json.dumps(profile, indent = 2))

    return profile

def flatten(orig):
    #print(json.dumps(orig, indent = 2))
    data = {}
    for personality in orig['personality']:
        for c in personality['children']:
            #print("Child found\n", json.dumps(c, indent = 2))
            if (c['category'] == 'personality'):
                #print("Child found\n", json.dumps(c, indent = 2))
                data[c['name']] = c['percentile']
    return data

def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
                compared_data[keys]=abs(dict1[keys] - dict2[keys])
    return compared_data

user_handle = "@Codecademy"
celebrity_handle = "@IBM"

user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)


#First, flatten the results from the Watson PI API
user = flatten(user_result)
celebrity = flatten(celebrity_result)

#Then, compare the results of the Watson PI API by calculating the distance between traits
compared_results = compare(user,celebrity)

sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

def form(num):
    return "{:.4f}".format(num)

print(f" Personality         | {user_handle}        | {celebrity_handle}               | compared ")
print("______________________________________________________________________________________")
for keys, value in sorted_result[:5]:
    print(f"{keys + ' ' * (20 - len(keys)) } | {form(user[keys])}             | {form(celebrity[keys])}             | {form(compared_results[keys])}\n")
