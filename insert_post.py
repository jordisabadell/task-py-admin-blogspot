#This code is based on Joe Gregorio's example and Google API Python client.
from __future__ import print_function
__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import sys
import json

from oauth2client import client
from googleapiclient import sample_tools

def readJsonFile():
    # read file
    with open('posts.json', 'r') as myfile:
        data=myfile.read()

    # parse file
    return json.loads(data)

def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/blogger')

    try:
        posts = service.posts()
        
        contents = readJsonFile()
        for content in contents:        
            #respost = posts.insert(blogId='*** your blog id ***', isDraft=False, body=content).execute() #add
            #print("Done. Response post_id:", respost['id'])

            print(content)

    except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run'
        'the application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
