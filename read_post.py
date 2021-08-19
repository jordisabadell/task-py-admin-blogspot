#This code is based on Joe Gregorio's example and Google API Python client.
from __future__ import print_function
import re
__author__ = 'jcgregorio@google.com (Joe Gregorio)'

from oauth2client import client
from googleapiclient import sample_tools

import sys

def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/blogger')

    try:
        numPost = 0
        posts = service.posts()

        contents = posts.list(blogId='*** your blog id ***', maxResults='500', startDate='2016-09-11T00:00:00+00:00', fetchImages=True).execute()
        for item in contents['items']:
            date = item['published']
            title = item['title']
            content = item['content']
            if "images" in item:
                images =  item['images']
            else:
                images = []

            replies =  item['replies']
            
            numPost = numPost + 1

        print("Done!", numPost)

    except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run'
        'the application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
