#This code is based on Joe Gregorio's example and Google API Python client.
from __future__ import print_function
import re
__author__ = 'jcgregorio@google.com (Joe Gregorio)'

from oauth2client import client
from googleapiclient import sample_tools

import sys
import datetime
import rfc3339

posts = []

def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/blogger')

    try:
        numPost = 0
        g_posts = service.posts()
        g_comments = service.comments()

        contents = g_posts.list(blogId='6393501472497239119', maxResults='500', startDate='2016-09-11T00:00:00+00:00', fetchImages=True).execute()
        for item in contents['items']:
            date = item['published']
            title = item['title']
            content = item['content']
            if "images" in item:
                images =  item['images']
            else:
                images = []
           
            '''
            #get comments
            comments_content = g_comments.list(blogId='*** your id blog ***', maxResults='500', postId=item['id'], fetchBodies=True).execute()
            if 'items' in comments_content:

                print(title)

                for comment_item in comments_content['items']:
                    
                    comment_date = comment_item['published']
                    comment_content = comment_item['content']
                    comment_autor = comment_item['author']['displayName']
                    
                    print(comment_autor, comment_date, comment_content)
            '''

            convert_day_table = {
                0: "Dilluns, ",
                1: "Dimarts, ",
                2: "Dimecres, ",
                3: "Dijous, ",
                4: "Divendres, ",
                5: "Dissabte, ",
                6: "Diumenge, ",
            }

            convert_month_table = {
                1:"de gener de ",
                2:"de febrer de ",
                3:"de març de ",
                4:"d’abril de ",
                5:"de maig de ",
                6:"de juny de ",
                7:"de juliol de ",
                8:"d’agost de ",
                9:"de setembre de ",
                10:"d’octubre de ",
                11:"de novembre de ",
                12:"de desembre de "
            }

            d = datetime.date(int(date[:4]), int(date[5:7]), int(date[8:10]))

            date = convert_day_table[d.weekday()] + str(int(date[8:10])) + " " + convert_month_table[int(date[5:7])] + date[:4] #+ " a les " + date[11:16]
            
            posts.append(content.replace("	", " ") + "<br>")
            posts.append(date + ".<br>")
            posts.append('__#__' + title + "<br>")

            numPost = numPost + 1

        # reverse array
        posts.reverse() 

        # write json file
        f = open("posts.html", "w", encoding='utf8')
        for i, post in enumerate(posts):
            f.write(post)
        f.close()

        print("Done!", numPost)

    except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run'
        'the application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
