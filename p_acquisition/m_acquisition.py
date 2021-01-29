import requests
import pandas as pd
from sqlalchemy import create_engine
from bs4 import BeautifulSoup


def database_connection():
    """
    creating connection to sqlite database and creating two dataframes with the information we will need from its tables
    """
    path = 'data/raw/raw_data_project_m1.db'
    conn_str = f'sqlite:///{path}'

    engine = create_engine(conn_str)

    data = pd.read_sql_query("""
    SELECT career_info.uuid,
    career_info.normalized_job_code,
    country_info.country_code,
    personal_info.age_group,
    personal_info.age
    FROM career_info
    JOIN country_info
    ON country_info.uuid = career_info.uuid
    JOIN personal_info
    ON personal_info.uuid = career_info.uuid;
    """, engine)

    votes_data = pd.read_sql_query("""
    SELECT poll_info.question_bbi_2016wave4_basicincome_vote,
    poll_info.question_bbi_2016wave4_basicincome_argumentsfor,
    poll_info.question_bbi_2016wave4_basicincome_argumentsagainst
    FROM poll_info;
    """, engine)

    raw_db_data = data.to_csv('data/raw/data_from_db.csv', index=False)
    poll_data = votes_data.to_csv('data/raw/poll_data.csv', index=False)

    return raw_db_data, poll_data

def creating_url_list():
    """
    creating a list of urls with each job code
    """
    raw_db_path = 'data/raw/data_from_db.csv'
    raw_db_data = pd.read_csv(raw_db_path)

    job_code_list = raw_db_data['normalized_job_code'].unique().tolist()
    url_list = []
    for code in job_code_list:
        url_list.append(f'http://api.dataatwork.org/v1/jobs/{code}')

    return url_list

def connecting_api(url_list):
    """
    creating the connection to the api where we can find the job titles and creating a dataframe with them
    """

    json_data_list = []

    for url in url_list:
        response = requests.get(url)
        json_data = response.json()
        json_data_list.append(json_data)

    job_titles_df = (pd.DataFrame(json_data_list)).to_csv('data/raw/job_titles_df.csv', index=False)

    return job_titles_df

def web_scraping():
    """
    web scraping to Eurostat page to extract a table with the country names and country codes, then creating a
    dataframe with this info. Adding Great Britain as its code GB because in Eurostat table this country does not appear
    """
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    items = [x.text for x in table.find_all('td')]
    clean_items = [i.strip('\n') for i in items]

    countrys = []
    country_codes = []

    for i in clean_items:
        if i.startswith('('):
            country_codes.append(i[1:-1])
        else:
            countrys.append(i)

    country_dict = dict(zip(countrys, country_codes))
    country_dict['Great Britain'] = 'GB'
    country_df = pd.DataFrame.from_dict(country_dict, orient='index')

    country_names_csv = country_df.to_csv('data/raw/country_names.csv')

    return country_names_csv


def acquire():

    database_connection()
    creating_url_list()
    url_list = creating_url_list()
    connecting_api(url_list)
    web_scraping()





