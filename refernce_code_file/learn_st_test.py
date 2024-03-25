import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["a", "b"])

st.bar_chart(chart_data)




st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.title(':blue[Youtube data harvestest and warehouse using API Automation]:red[ project - 1]')
st.header(':green[Guvi project - 1]', divider='rainbow')

st.subheader('Enter :blue[Channel ID] :sunglasses:')

st.caption('This is a string that explains something above.')

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
st.text('This is some text.')

st.write("This is some text using 'write'.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")



import pandas as pd
import streamlit as st

data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)

import streamlit as st

col1, col2, col3 = st.columns(3)
a = '70 °F'
col1.metric("Temperature", a, "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")


import streamlit as st

with open("youtube.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="youtube.png",
            mime="youtube.png"
          )
    



st.link_button("Go to gallery", "https://streamlit.io/gallery")

st.text("""your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py""")


st.text("""st.page_link("your_app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")""")


import streamlit as st

agree = st.checkbox('I agree')

if agree:
    st.write(agree)
    st.write('Great!')
    
    
    
    
option = st.selectbox(
   "How would you like to be contacted?",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method...",
)

st.write('You selected:', option)



import streamlit as st

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)



# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)

import streamlit as st

txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    )

st.write(f'You wrote {len(txt)} characters.')




#  PROJECT START TO END

import datetime
import streamlit as st

today = datetime.datetime.now()
next_year = today.year
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)


import datetime
import streamlit as st

d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d)



import streamlit as st
st.image('youtube.png', caption='Sunrise by the mountains')


import streamlit as st
import time

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')
    
import streamlit as st
import time

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()
    
    
    
import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'
    
    
    
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')                                                                                



import streamlit as st
import pandas as pd

def channel_data_sql(data):
    # Assume this function saves the data to a MySQL database
    pass

def main():
    st.title("YouTube Channel Data Viewer")

    # Input for getting user channel data
    channel_name = st.text_input("Enter YouTube channel name:")
    get_data_button = st.button("Get channel data")

    if get_data_button:
        # Assume this function collects data from the channel
        data = {"Channel Name": channel_name, "Data": "Some data"}
        df = pd.DataFrame(data, index=[0])
        st.write("Channel Data:")
        st.write(df)

        # Button to move data to database
        move_to_db_button = st.button("Move data to DB")

        if move_to_db_button:
            st.write(data)
            channel_data_sql(data)
            st.success("Data moved to database successfully.")

if __name__ == "__main__":
    main()
