import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np
from backend import youtube_channel
from sql_backend_fetch import *
from backend import *



logo_image = 'youtube.png'
st.image(logo_image, width=400)

# Add a title to your app
st.title(':red[Youtube] data :green[harvestest] and :blue[warehouse]')
# st.markdown("<h1 style='color: red;'>YouTube Channel Data Viewer</h1>", unsafe_allow_html=True)


temp_ch_count= [0]
print(temp_ch_count)
col1, col2, col3,col4,col5 = st.columns(5)

ch_count = channel_count()      # output in str formate
pc = playlist_count()
vc = vedio_count()
cc = comment_count()



ch,play,ved,com = inc()
col1.metric("Working","45 hrs", "8+")
col2.metric("Channel Count", str(ch_count), str(ch))
col3.metric("Total playlist data", pc, str(play))
col4.metric("Total vedio data", vc, str(ved))
col5.metric("Total comment data", cc, str(com))
st.header("",divider='rainbow')



    # Add an input field for the user to enter the channel ID
channel_id = st.text_input('Enter YouTube Channel ID')

    # Add a button to fetch data for the entered channel ID
if st.button('Get Channel Data'):
    with st.spinner('Wait for it...'):
        time.sleep(3)
        if channel_id:
            try:
                channel_data = core_engine(channel_id)
                for key, value in channel_data.items():
                    st.write(f'<span style="color:red">{key}</span>: <span style="color:black">{value}</span>', unsafe_allow_html=True)
            except KeyError:
                st.success('Data Fetched successfully', icon="✅")
            except Exception as e:
                st.warning(f"An error occurred: {str(e)}", icon="🚨")
        else:
            st.warning('Please enter a YouTube Channel ID', icon="🚨")


selected_option = st.radio(
    "Select Table to View",
    ("Clear","Channel Data", "Playlist Data","Vedio Data", "Comment Data")
)

if selected_option == "Channel Data":
    a = channel_table()
    a = pd.DataFrame(a)
    st.write(a)

elif selected_option == "Playlist Data":
    b = playlist_table()
    b = pd.DataFrame(b)
    st.write(b)

elif selected_option == "Vedio Data":
    c = pd.DataFrame(vedio_table())
    st.write(c)
    
elif selected_option == "Comment Data":
    d = pd.DataFrame(comment_table())
    st.write(d)
elif selected_option == 'clear':
    pass


#    query show design  

option = st.selectbox(
    'FAQ - Question for future decision',
    ('---Defaut---Not Selected---Any---FAQ',
     'What are the names of all the videos and their corresponding channels',
     'Which channels have the most number of videos, and how many videos do they have?',
    'How many comments were made on each video, and what are their corresponding video names?',
    "Which videos have the highest number of comments, and what are their corresponding channel names?",
    "What are the names of all the channels that have published videos in the year 2022?",
    "Which videos have the highest number of likes, and what are their corresponding channel names",
    "What is the total number of likes and dislikes for each video, and what are their corresponding video names?"
    
))

if option == "What are the names of all the videos and their corresponding channels":
    a = query1()
    a = pd.DataFrame(a,columns=['Channel Name','vedio Name'])
    st.write(a)

elif option == "Which channels have the most number of videos, and how many videos do they have?":
    b = pd.DataFrame(query2(),columns=['channel_id','channel_name','vedio_count'])
    st.write(b)

elif option == "How many comments were made on each video, and what are their corresponding video names?":
    c = pd.DataFrame(query4(),columns=['comment_count','vedio_id','vedio_name'])
    st.write(c)
    
elif option == "Which videos have the highest number of likes, and what are their corresponding channel names":
    c = pd.DataFrame(query5(),columns=['Hightest Likes','Vedio Tittle','channel_name'])
    st.write(c)
elif option == "What is the total number of likes and dislikes for each video, and what are their corresponding video names?":
    c = pd.DataFrame(query6(),columns=['Likes','Vedio_name'])
    st.write(c)
elif option == "What are the names of all the channels that have published videos in the year 2022?":
    c = pd.DataFrame(query8(),columns=['published', 'video_name', 'channel_name'])
    st.write(c)
elif option == "Which videos have the highest number of comments, and what are their corresponding channel names?":
    c = pd.DataFrame(query10(),columns=["vedio_id", "comment count", "channel_name"])
    st.write(c)
    
agree = st.checkbox('what are the top 10 most viewed videos and their respective channels')
if agree:
    data = pd.DataFrame(query3(), columns=['View Count', 'Video Name', 'Channel Name'])
    st.scatter_chart(data.set_index('Video Name')['View Count'], color=["#FF0000"])
    
    
agree = st.checkbox('What is the total number of views for each channel, and what are their corresponding channel names?')
if agree:
    data = pd.DataFrame(query7(), columns=['Channel Name','View Count'])
    st.line_chart(data.set_index('Channel Name')['View Count'], color='#355E3B')



#==========================================================================================================
def sidebar():
    # Sidebar with input fields
    with st.sidebar:
        st.header("Welcome back :red[Siranjeevi V]", divider='rainbow')
        
        
        today = datetime.datetime.now()
        next_year = today.year
        jan_1 = datetime.date(next_year, 3, 2)
        dec_31 = datetime.date(next_year, 12, 31)
        st.date_input(
            "Working duration for this project",
            (jan_1, datetime.date(next_year, 3, 24)),
            jan_1,
            dec_31,
            format="DD.MM.YYYY")
        
        skill = st.button('show leaning skills and using tools')
        if skill:
            st.toast('Python :white_check_mark:')
            time.sleep(0.8)
            st.toast('SQL 📚')
            time.sleep(0.8)
            st.toast('MySQL 🛠️')
            time.sleep(0.8)
            st.toast('API Integration ⏳')
            time.sleep(0.8)
            st.toast('Data Collection & cleaning 🛠️')
            time.sleep(0.8)
            st.toast('Streamlit', icon='🎉')
            
        agree = st.checkbox('channel list DB')
        if agree:
            a = channel_list()
            st.write(a)
sidebar()