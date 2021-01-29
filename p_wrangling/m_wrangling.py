import pandas as pd


def cleaning_ages_step1():
    """
    changing some values in column age_group to make it more readable
    """
    raw_db_path = 'data/raw/data_from_db.csv'
    db_data = pd.read_csv(raw_db_path)
    age_group = db_data['age_group'].tolist()
    clean_age_group = [i.replace('_', '-') for i in age_group]
    properly_age_group = [i.replace('juvenile', '14-25') for i in clean_age_group]

    db_data['age_group'] = properly_age_group

    return db_data

def cleaning_ages_step2(clean_age_df):
    """
    adding new age groups with 4 more years because last results of the dataset were given in 2016
    """

    age_group = clean_age_df['age_group'].tolist()

    new_age_group = []

    for i in age_group:
        if i == '14-25':
            new_age_group.append(i.replace('14-25', '18-29'))
        elif i == '26-39':
            new_age_group.append(i.replace('26-39', '30-49'))
        else:
            new_age_group.append(i.replace('40-65', '50-69'))

    clean_age_df['age_group'] = new_age_group

    return clean_age_df

def completing_country_names():
    """
    changing columns names to understandable ones and changing Greece country code to the one that appears in the
    database we worked with first
    """
    country_df_path = 'data/raw/country_names.csv'
    country_df = pd.read_csv(country_df_path)

    country_names_df = country_df.rename(columns={'Unnamed: 0': 'country', '0': 'country_codes'})

    country_names_df['country_codes'][1] = 'GR'

    return country_names_df

def merging_jobs_ages(ages_df):
    """
    merging dataframe were we have our clean age_group column and our job titles
    """
    jobs_df_path = 'data/raw/job_titles_df.csv'
    job_titles_df = pd.read_csv(jobs_df_path)
    merged_df = ages_df.merge(job_titles_df, left_on='normalized_job_code', right_on='uuid')
    cleaning_df = merged_df.drop(columns=['normalized_job_code', 'error', 'uuid_y', 'normalized_job_title', 'parent_uuid'])
    first_almost_proper_df = cleaning_df.fillna('Unemployed')

    return first_almost_proper_df

def merging_countries(countries, job_and_ages):
    """
    last merge to also add the country names corresponding to theirs codes
    """
    merging_countries = countries.merge(job_and_ages, left_on='country_codes', right_on='country_code')
    cleaning_df = merging_countries.drop(columns=['country_codes', 'country_code', 'uuid_x'])
    processed_df = cleaning_df.rename(columns={'country': 'Country', 'age_group': 'Age Group', 'title': 'Job Title'})

    processed_df.to_csv('data/processed/processed_df.csv')

    return processed_df

def cleaning_voting_df():
    """
    changing column names of poll_data dataframe to make it readable
    """
    vote_data = pd.read_csv('data/raw/poll_data.csv')
    poll_data = vote_data.rename(columns={'question_bbi_2016wave4_basicincome_vote': 'vote',
                                           'question_bbi_2016wave4_basicincome_argumentsfor': 'pro_args',
                                           'question_bbi_2016wave4_basicincome_argumentsagainst': 'con_args'})

    poll_data = poll_data.to_csv('data/processed/poll_data_processed.csv')

    return poll_data


def wrangling():

    cleaning_step1 = cleaning_ages_step1()
    clean_age_group_column = cleaning_ages_step2(cleaning_step1)
    complete_countries = completing_country_names()
    jobs_and_ages = merging_jobs_ages(clean_age_group_column)
    merging_countries(complete_countries, jobs_and_ages)
    cleaning_voting_df()



