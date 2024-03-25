# youtube-data-harvesting-Warehousing-using-API-SQL-and-Streamlit

Short description of the project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Instructions on how to install the project and its dependencies.

## Usage

Instructions on how to use the project and examples if applicable.


# Project work Flow

This project uesed tools and technology - python, Pandas, Data Collection, Streamlit, API integration, Data Management, Mysql using SQL.


```sh
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

## Approach:

      Set up a Streamlit app: Streamlit is a great choice for building data visualization and analysis tools quickly and easily. You can use Streamlit to create a simple UI where users can enter a YouTube channel ID, view the channel details, and select channels to migrate to the data warehouse.
      
      - `Connect to the YouTube API: You'll need to use the YouTube API to retrieve channel and video data. You can use the Google API client library for Python to make requests to the API.`
      
      - Store and Clean data : Once you retrieve the data from the YouTube API, store it in a suitable format for temporary storage before migrating to the data warehouse. You can use pandas DataFrames or other in-memory data structures.
      
      Migrate data to a SQL data warehouse: After you've collected data for multiple channels, you can migrate it to a SQL data warehouse. You can use a SQL database such as MySQL or PostgreSQL for this.
      
      Query the SQL data warehouse: You can use SQL queries to join the tables in the SQL data warehouse and retrieve data for specific channels based on user input. You can use a Python SQL library such as SQLAlchemy to interact with the SQL database.
      
      Display data in the Streamlit app: Finally, you can display the retrieved data in the Streamlit app. You can use Streamlit's data visualization features to create charts and graphs to help users analyze the data.


## Installation

To run this project, you'll need Python installed. Then, you can clone the repository and run the following command:

```sh
## Installation

This project requires the following libraries to be installed:

- `os`
- `google_auth_oauthlib.flow`
- `googleapiclient.discovery`
- `googleapiclient.errors`
- `pprint`
- `mysql.connector`

You can install these libraries using pip:

```sh
pip install google-auth-oauthlib google-api-python-client mysql-connector-python
 details.
