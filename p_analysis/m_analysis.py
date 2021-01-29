import pandas as pd

def quantity_col():
    """
    creating a column with the quantity of people in each country that works in each job or people that is unemployed
    """

    processed_df_path = 'data/processed/processed_df.csv'
    processed_df = pd.read_csv(processed_df_path)
    adding_qt_col = pd.DataFrame(processed_df.groupby(['Country', 'Job Title'])['Age Group'].value_counts().reset_index(name='Quantity'))
    sorted_qt = adding_qt_col.sort_values(by='Quantity', ascending=False)

    return sorted_qt

def percentage_col(complete_df):
    """
    calculating and creating a column with the percentage from quantity results
    """
    complete_df['Percentage'] = round((complete_df['Quantity'] / complete_df['Quantity'].sum()) * 100, 2)
    complete_df['Percentage'] = complete_df['Percentage'].astype(str) + '%'
    complete_df.to_csv('data/results/main_df.csv', index=False)

    return complete_df

def voting_counts():
    """
    creating lists to count the arguments in favour and against of people about BBI in 2016
    """
    poll_data = pd.read_csv('data/processed/poll_data_processed.csv')

    for_list = ['I would vote for it', 'I would probably vote for it']
    for i in for_list:
        for_voting = poll_data[poll_data['vote'] == i]
    against_list = ['I would vote against it', 'I would probably vote against it']
    for i in against_list:
        against_voting = poll_data[poll_data['vote'] == i]
    abstain_list = ['I would not vote']
    for i in abstain_list:
        abstain_voting = poll_data[poll_data['vote'] == i]

    for_pro_args = len(for_voting['pro_args'].unique().tolist())
    for_con_args = len(for_voting['con_args'].unique().tolist())
    against_pro_args = len(against_voting['pro_args'].unique().tolist())
    against_con_args = len(against_voting['con_args'].unique().tolist())
    abstain_pro_args = len(abstain_voting['pro_args'].unique().tolist())
    abstain_con_args = len(abstain_voting['con_args'].unique().tolist())

    votes_dict = {'Number of Pro Arguments': [for_pro_args, against_pro_args, abstain_pro_args],
                  'Number of Con Arguments': [for_con_args, against_con_args, abstain_con_args]}

    votes_df = pd.DataFrame(votes_dict, index=['In Favour', 'Against', 'Abstained'])

    arguments_count = votes_df.to_csv('data/results/arguments_count.csv')

    return arguments_count

def analysis():

    qt_col = quantity_col()
    percentage_col(qt_col)
