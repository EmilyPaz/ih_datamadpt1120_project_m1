from p_acquisition.m_acquisition import acquire
from p_wrangling.m_wrangling import wrangling
from p_analysis.m_analysis import analysis
import pandas as pd
import matplotlib.pyplot as plt

def extracting_complete_df():
    acquire()
    wrangling()
    analysis()
    complete_df = pd.read_csv('data/results/main_df.csv')

    return complete_df

def quantities_for_ratios():
    """
    calculating total quantity of employed and unemployed people in EU
    """

    main_df_path = 'data/results/main_df.csv'
    main_df = pd.read_csv(main_df_path)
    rates_qt = main_df[['Job Title', 'Quantity']]
    rates_qt = rates_qt.rename(columns={'Job Title': 'job_title'})
    unemployment = rates_qt[rates_qt.job_title == 'Unemployed']
    unemployment_qt = sum(unemployment['Quantity'].to_list())
    employment = rates_qt[rates_qt.job_title != 'Unemployed']
    employment_qt = sum(employment['Quantity'].to_list())
    whole_qt = unemployment_qt + employment_qt

    return unemployment_qt, employment_qt, whole_qt

def percentage_function(part, whole):
    """
    function to calculate percentages
    """
    return 100 * float(part) / float(whole)

def percentages_for_ratios(qts_function):
    """
    calculating percentages of employed and unemployed people from theirs quantities
    """
    unemployment_ptcg = round(percentage_function(qts_function[0], qts_function[2]), 2)
    employment_ptcg = round(percentage_function(qts_function[1], qts_function[2]), 2)

    return unemployment_ptcg, employment_ptcg

def visualization_ratios(pctgs_function):
    """
    creating a pie chart for visualization
    """
    labels = 'Unemployment', 'Employment'
    sizes = [round(pctgs_function[0], 2), round(pctgs_function[1], 2)]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')
    ax.title.set_text('Unemployment vs Employment ratios in EU')

    visual_pie = fig.savefig('data/results/ratios.pdf', transparent=False, dpi=80, bbox_inches='tight')

    return visual_pie


def visualization():

    qts = quantities_for_ratios()
    pctgs = percentages_for_ratios(qts)
    return visualization_ratios(pctgs)
