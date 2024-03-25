# Update the import statement in backend.py
import google_auth_oauthlib.flow
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from pprint import*
import mysql.connector
from googleapiclient.discovery import build


def core_engine(id):
    
    #channel data
    channel_data,cid=youtube_channel(id)
    channel_data_sql(channel_data)
    #playlist data
    play_data,playlist_id = playlist_data(cid)
    playlist_id_insert(play_data)
    
    # vedio id collecter
    vedio_id =  vedio_id_collector(cid)
    
    #vedio data
    # vedio_id = vedio(vedio_id)
    vedio_data,v_id = vedio_main(vedio_id)
    # vedio_data = vedio_main(vedio_id)   # => collect video data
    video_data_insert(vedio_data)
    
    #comment data
    comment_data = comment_main(v_id)
    comment_data_insert(comment_data)



# Open the file in read mode
def read_key():
    with open('youtube api key.txt', 'r') as file:
        api_key = file.read()
        return api_key

def vedio_id_collector(ch_id):
    # Replace 'YOUR_API_KEY' with your actual API key
    API_KEY = read_key()

    # Create a service object for interacting with the API
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Retrieve the list of videos from the channel
    request = youtube.search().list(
        part='id',
        channelId=ch_id,
        maxResults=50  # Maximum number of results per page
    )

    vedio_id = []
    # Iterate over the results and print video IDs
    while request:
        response = request.execute()

        for item in response['items']:
            if item['id']['kind'] == 'youtube#video':
                result = item['id']['videoId']
                vedio_id.append(result)

        request = youtube.search().list_next(request, response)
    return vedio_id




def youtube_channel(id):
    api_service_name = "youtube"
    api_version = "v3"
    api_key = read_key()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics,status",
        id=id)

    response = request.execute()
    channel_data = {
        "Channel_Name": response['items'][0]['snippet']['title'],
        "Channel_Id": response['items'][0]['id'],
        "Subscription_Count": response['items'][0]['statistics']['subscriberCount'],
        "Channel_Views": response['items'][0]['statistics']['viewCount'],
        "vedio_count": response['items'][0]['statistics']['videoCount'],
        "Status":response['items'][0]['status']['privacyStatus'],
        "Channel_Description": response['items'][0]['snippet']['description']
        # "Channel_thumbnails": response['items'][0]['snippet']['thumbnails'],      #extra
      
    }
    return channel_data,id
    

def channel_data_sql(channel_data):
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1022',
        database="youtube"
    )

    mycursor = mydb.cursor()
    data = channel_data
    # Check if data already exists
    check_sql = "SELECT * FROM channel_data WHERE Channel_Id = %s"
    check_val = (data['Channel_Id'],)
    mycursor.execute(check_sql, check_val)
    existing_data = mycursor.fetchone()

    if existing_data:
        return "Data already exists. No need to insert."
    else:
        insert_sql = "INSERT INTO channel_data (Channel_Name, Channel_Id, Subscription_Count, Channel_Views, Channel_Description, vedio_count, Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        insert_val = (data['Channel_Name'], data['Channel_Id'], data['Subscription_Count'], data['Channel_Views'], data['Channel_Description'], data['vedio_count'], data['Status'])
        mycursor.execute(insert_sql, insert_val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    mycursor.close()
    mydb.close()
    
# --------------------------------------------------------------------------------------------------------

def playlist_data(ch_id):
    api_service_name = "youtube"
    api_version = "v3"
    api_key = read_key()
    youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=api_key)
    
    playlist_data = []
    page_token=None
    while True:
        playlist_request = youtube.playlists().list(
                part="snippet,contentDetails,id,status",
                channelId=ch_id,
                maxResults=50,
                pageToken=page_token
            )
        playlist_response = playlist_request.execute()
        Playlist_count = len(playlist_response['items'])
        for i in range(0, Playlist_count):
            playlist = {
                'channel_id': playlist_response['items'][i]['snippet']['channelId'],
                'playlists': {
                    # 'vedio_title': playlist_response['items'][i]['snippet']['title'],
                    'playlist_name': playlist_response['items'][i]['snippet']['title'],
                    'playlist_id': playlist_response['items'][i]['id']
                    # 'playlist_video_count': playlist_response['items'][i]['contentDetails']['itemCount']
                }
            }
            playlist_data.append(playlist)
        
        # Check if there are more pages
        page_token = playlist_response.get('nextPageToken')
        if not page_token:
            break
        
    
    playlist_id = [playlist_data[i]['playlists']["playlist_id"] for i in range(len(playlist_data))]
    # playlist_id_collect(playlist_data)
    return playlist_data,playlist_id



def playlist_id_insert(data):
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1022',
        database="youtube"
    )

    mycursor = mydb.cursor()

    # Your playlist_data dictionary
    playlist_data = data
    # Insert data into the table
    # Insert data into the table
    for entry in playlist_data:
        playlists = entry['playlists']
        sql = "INSERT IGNORE INTO playlist_data (playlist_id, channel_id, playlist_name) VALUES (%s, %s, %s)"
        val = (playlists['playlist_id'], entry['channel_id'], playlists['playlist_name'])
        mycursor.execute(sql, val)

    # Commit changes to the database
    mydb.commit()

    print(mycursor.rowcount, "records inserted.")

    # Close cursor and connection
    mycursor.close()
    mydb.close()
#-------------------------------------------------------------------------------------------------

import os
import googleapiclient.discovery


def fetch_all_playlist_items(id):           # collect all vedio id in a channel
    all_playlist_items = []
    next_page_token = None
    api_key = read_key()
    api_service_name = "youtube"
    api_version = "v3"
    
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
    while True:
        playlist_request = youtube.playlistItems().list(
            part="snippet,contentDetails,id,status",
            playlistId=id,
            maxResults=50,
            pageToken=next_page_token
        )
        playlist_response = playlist_request.execute()
        
        all_playlist_items.extend(playlist_response.get('items', []))
        
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break
    
    return all_playlist_items


def vedio_id_collect(id):
    temp = []                       # Initialize list to store video data     
    temp_playlist_ids = id
    for playlist_id in temp_playlist_ids:
        all_playlist_items = fetch_all_playlist_items(playlist_id)   
        for item in all_playlist_items:
            id = item['contentDetails']['videoId']
            temp.append(id)
    return temp                             ## vedio id only






#----------------------vedio table ------------------------------------------------------------------------------------
import os
import pprint
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from pprint import *


def vedio_collection(vedid):                            # collecting data by given id
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    api_key = read_key()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
    
    request = youtube.videos().list(
            part="snippet,contentDetails,statistics,status",
            id=vedid
        )
    return request.execute()

def vedio_main(temp_data):
    vediodata =[]
    ved_id = []
    for id in temp_data:
        data = vedio_collection(id).get('items')
        # pprint(data)
        for response in data:
            data = {
                "channal_id":response['snippet']['channelId'],
                "video_id": response['id'],
                "like_count":response['statistics']['likeCount'],
                "view_count":response['statistics']['viewCount'],
                "comment_count":response['statistics']['commentCount'],
                "favorite_count":response['statistics']['favoriteCount'],
                "Vedio_name":response['snippet']['title'],
                "Duration":response['contentDetails']['duration'],
                "published":response['snippet']['publishedAt'],
                "status":response["status"]["privacyStatus"],
                "thumbnail":response['snippet']['thumbnails']['default']['url'],
                "description":response["snippet"]["description"][:250]    # i will take only 255 charter
                
            }
            
            ved_id.append(response['id'])
            vediodata.append(data)
            # pprint(response)
    return vediodata,ved_id
       


import mysql.connector

def video_data_insert(data_list):


    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1022',
        database="youtube"
    )

    mycursor = mydb.cursor()

    # Create video_data table if it does not exist
    # mycursor.execute("CREATE TABLE IF NOT EXISTS V_data ("
                    #  "channel_id VARCHAR(255), "
                    #  "video_id VARCHAR(255) PRIMARY KEY, "
                    #  "like_count INT, "
                    #  "view_count INT, "
                    #  "comment_count INT, "
                    #  "favorite_count INT, "
                    #  "video_name VARCHAR(255), "
                    #  "duration VARCHAR(255), "
                    #  "published VARCHAR(255), "
                    #  "status VARCHAR(255), "
                    #  "thumbnail VARCHAR(255), "
                    #  "description TEXT"
                    #  ")")

    # Insert data into the table
    sql = "INSERT INTO V_data (channel_id, video_id, like_count, view_count, comment_count, favorite_count, video_name, duration, published, status, thumbnail, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE video_id=video_id"

    for data in data_list:
        val = (
            data["channal_id"],data["video_id"], data["like_count"], data["view_count"],data["comment_count"],
            data["favorite_count"],data["Vedio_name"],data["Duration"],data["published"],
            data["status"],data["thumbnail"],data["description"]
        )
        mycursor.execute(sql, val)

    # Commit changes to the database
    mydb.commit()

    print(mycursor.rowcount, "records inserted.")

    # Close cursor and connection
    mycursor.close()
    mydb.close()


#===================================================================================================================

import os
import googleapiclient.discovery
import pandas as pd
from pprint import *

def comment(vid_id):
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = read_key()
        youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

        request = youtube.commentThreads().list(
                part="snippet",
                videoId =vid_id,
                maxResults=25
        )
        response = request.execute()
        items = response.get('items')
        # print(len(items))
        temp = []
        for item in items:      
                comment = item['snippet']['topLevelComment']['snippet']
                comment_data = {
                        'comment_id':comment['authorChannelId']['value'],
                        'vedio_id': comment['videoId'],
                        'text_comment':comment['textOriginal'],
                        'comment_time':comment['updatedAt'],
                        'comment_author':comment['authorDisplayName']
                        }
                temp.append(comment_data)    
        # pprint(temp)
        return temp

def comment_main(vedio_id):                     # main function
    cm_data = []
    for i in vedio_id:
        data = comment(i)
        cm_data.extend(data)
    return cm_data


import mysql.connector

def comment_data_insert(data):
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1022',
        database="youtube"
    )

    mycursor = mydb.cursor()
    
    # Insert data into the table
    for i in range(len(data)):
        item = data[i]
        sql = "INSERT INTO comment_data (comment_id, comment_author, comment_time, text_comment, vedio_id) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE comment_id=comment_id"
        val = (item['comment_id'], item['comment_author'], item['comment_time'], item['text_comment'], item['vedio_id'])
        mycursor.execute(sql, val)
        
    # Commit changes to the database
    mydb.commit()

    print(mycursor.rowcount, "records inserted.")

    # Close cursor and connection
    mycursor.close()
    mydb.close()

