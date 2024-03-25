# Project Title

YouTube Data Harvesting and Warehousing using SQL and Streamlit

## Skills Takeaway From This Project

- Python scripting
- Data Collection
- Streamlit
- API integration
- Data Management using SQL

## Domain

Social Media


## Installation

To run this project, you'll need Python installed. Then, you can clone the repository and run the following command:


## Installation

This project requires the following libraries to be installed:
```
- `os`
- `google_auth_oauthlib.flow`
- `googleapiclient.discovery`
- `googleapiclient.errors`
- `pprint`
- `mysql.connector`
- `streamlit`
- `pandas`
```
You can install these libraries using pip:

```
pip install google-auth-oauthlib google-api-python-client mysql-connector-python
 details.
```
## Environment Setup

1. **Create a Virtual Environment:** (Optional but recommended)
   - It's a good practice to work in a virtual environment to isolate your project dependencies. You can create a virtual environment using `venv` or `conda`:
     - Using `venv` (for Python 3):
       ```sh
       python3 -m venv myenv
       ```
     - Using `conda`:
       ```sh
       conda create --name myenv
       ```

2. **Activate the Virtual Environment:**
   - Activate the virtual environment:
     - On Windows:
       ```sh
       myenv\Scripts\activate
       ```
     - On macOS/Linux:
       ```sh
       source myenv/bin/activate
       ```

3. **Install Streamlit and Dependencies:**
   - Once the virtual environment is activated, install Streamlit and other dependencies:
     ```sh
     pip install streamlit google-auth-oauthlib google-api-python-client mysql-connector-python
     ```

4. **Run the Streamlit Application:**
   - Start your Streamlit application:
     ```sh
     streamlit run your_app.py
     ```
   - Replace `your_app.py` with the name of your Streamlit application file.

5. **Deactivate the Virtual Environment:**
   - When you're done working on your project, deactivate the virtual environment:
     ```sh
     deactivate
     ```


## project workflow
```sh
                        create Youtube v3 API create(Google Developer Console)
                                        |
                                        |

  CHANNEL_ID ( UCiEmtpFVJjpvdhsQ2QAhxVA )
                                        |
                                        |

                                    PLAYLIST_ID (UUiEmtpFVJjpvdhsQ2QAhxVA)
                                        |
                                        |
                      ---------------------------------------------
                      |               |           |               |
                  VIDEO_ID(1)    VIDEO_ID(2)    VIDEO_ID(3)      VIDEO_ID(4)
                ("dQw4w9WgXcQ")("9bZkp7q19f0") ("j5-yKhDd64s")  ("QH2-TGUlwu4")
                      |
                comment data ID
                (hgfkh5wslajsq28) 
```

## Problem Statement

The problem statement is to create a Streamlit application that allows users to access and analyze data from multiple YouTube channels. The application should have the following features:

- Ability to input a YouTube channel ID and retrieve all the relevant data (Channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, comments of each video) using Google API.
- Ability to collect data for up to 10 different YouTube channels and store them in the data lake by clicking a button.
- Option to store the data in a MYSQL or PostgreSQL.
- Ability to search and retrieve data from the SQL database using different search options, including joining tables to get channel details.

## Approach

1. Set up a Streamlit app: Streamlit is a great choice for building data visualization and analysis tools quickly and easily. You can use Streamlit to create a simple UI where users can enter a YouTube channel ID, view the channel details, and select channels to migrate to the data warehouse.

2. Connect to the YouTube API: You'll need to use the YouTube API to retrieve channel and video data. You can use the Google API client library for Python to make requests to the API.

3. Store and Clean data: Once you retrieve the data from the YouTube API, store it in a suitable format for temporary storage before migrating to the data warehouse. You can use pandas DataFrames or other in-memory data structures.

4. Migrate data to a SQL data warehouse: After you've collected data for multiple channels, you can migrate it to a SQL data warehouse. You can use a SQL database such as MySQL or PostgreSQL for this.

5. Query the SQL data warehouse: You can use SQL queries to join the tables in the SQL data warehouse and retrieve data for specific channels based on user input. You can use a Python SQL library such as SQLAlchemy to interact with the SQL database.

6. Display data in the Streamlit app: Finally, you can display the retrieved data in the Streamlit app. You can use Streamlit's data visualization features to create charts and graphs to help users analyze the data.

## Example Data Extraction from Youtube API

```json
{
    "Channel_Name": {
        "Channel_Name": "Example Channel",
        "Channel_Id": "UC1234567890",
        "Subscription_Count": 10000,
        ...
    },
    "Video_Id_1": {
        "Video_Id": "V1234567890",
        "Video_Name": "Example Video 1",
        ...
    },
    ...


}

```


Project Logo](YDHW.png)



