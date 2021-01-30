# ih_datamadpt1120_project_m1
Module 1 Project for Data Analytics Ironhack Bootcamp

<p align="center">
  <img width="300" height="300" src="https://d92mrp7hetgfk.cloudfront.net/images/sites/misc/ironhack/original.jpg?1568082165">
</p>

## **ABOUT**

This project has the purpose to be a tool to extract some information about employment in each EU country. 

The results you are able to extract from this tool are:

---

### 1. Country, jobs and age group information
The tool let you extract a table with EU countries, jobs titles, age groups, and the quantity and percentage of people who is working or unemployed. You can choose to extract the whole table or an especific EU country instead. 

**HOW TO**: As you choose the main script to run it with python, you need to add an argument --country where you can choose the EU country (for example: --country='Hungary') or choose the whole table writting 'complete table'.

---

### 2. Employment vs unemployment chart
You can also choose to extract a pie chart to see the percentage of people employed and unemployed in the EU. 

---

### 3. Pro and Con Arguments about BBI project
The last result you can extract is a table where you can see the quantity of people who was in favor, against or absteined to vote about the European Bio-Based Industries project in  2016. 

---

## :bug: **STATUS**
This is the first project made during Ironhack Bootcamp. My goal is to get this project improved step by step, applying all the knowledge we will keep learning these next months, so we can have an efficient and interesting tool to applicate with other kind of information we would want to process.

## :computer: **TECHNOLOGY STACK**
- Python :snake:
- Pandas :panda_face: 
- SQL Alchemy :electric_plug:
- Requests :link:
- BeautifulSoup :ramen:
- Matplotlib :bar_chart:
- Argparse :book:
- PyCharm :beetle:

## :open_file_folder: **FOLDER STRUCTURE**
```
└── project
    ├── .idea
    ├── __trash__
    ├── data
    │   ├── raw
    │   ├── processed
    │   └── results
    ├── p_acquisition
    │   ├── __init__.py
    │   └── m_acquisition.py
    ├── p_analysis
    │   ├── __init__.py
    │   └── m_analysis.py
    ├── p_reporting
    │   ├── __init__.py
    │   └── m_reporting.py
    ├── p_wrangling
    │   ├── __init__.py
    │   └── m_wrangling.py
    ├── .gitignore
    ├── README.md
    └── main_script.py
```

### :information_source: **RESOURCES**

- **Tables (.db).** [Here](http://www.potacho.com/files/ironhack/raw_data_project_m1.db) you can find the `.db` file with the main dataset.

- **API.** We will use the API from the [Open Skills Project](http://dataatwork.org/data/). 

- **Web Scraping.** Finally, we will need to retrieve information about country codes from [Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes) website.
    
    
### :mailbox_with_mail: CONTACT INFO

If you have any comments or questions please contact me! emilypaz3012@gmail.com

