import argparse
from p_reporting.m_reporting import extracting_complete_df, visualization
from p_analysis.m_analysis import voting_counts

countries_list = ['Great Britain', 'France', 'Germany', 'Spain', 'Italy', 'Poland', 'Netherlands', 'Hungary', 'Romania',
                'Greece', 'Sweden', 'Belgium', 'Austria', 'Portugal', 'Czechia', 'Bulgaria', 'Ireland', 'Denmark',
                'Finland', 'Croatia', 'Slovakia', 'Lithuania', 'Slovenia', 'Latvia', 'Estonia', 'Luxembourg', 'Cyprus',
                'Malta']

def argument_parser():

    parser = argparse.ArgumentParser(description='create new dataframe from some data obtained with connection to a database, web scraping and connection to APIs')
    parser.add_argument('-c', '--country', help='specify country chosen by user to extract information from it', type=str)
    args = parser.parse_args()

    return args

def main(arguments):

    if arguments.country in countries_list:
        main_df = extracting_complete_df()
        main_df[main_df.Country == arguments.country].to_csv(f'data/results/{arguments.country}.csv')
        print(f'You can find {arguments.country} information in results folder')

    elif arguments.country == 'complete table':
        extracting_complete_df()
        print('You can find all EU countries information in complete table from results folder')
    else:
        raise ValueError('Please choose an available answer')

    question = input('Would you like to see a pie chart about employment in EU? ')

    if question.lower() == 'yes':
        visualization()
        print('You can find the visualization pdf file in your results folder')
    elif question.lower() == 'no':
        print('Okay, last question:')
    else:
        raise ValueError('Please answer yes or no')

    question2 = input("Would you like to extract a table rating about basic income people's opinion in 2016? ")

    if question2.lower() == 'yes':
        voting_counts()
        print('You can find the table in your results folder')
    elif question2.lower() == 'no':
        print('Fine, see you soon!')
    else:
        raise ValueError('Please answer yes or no')


if __name__ == '__main__':
    main(argument_parser())
