import pandas as pd  # Library for data analysis
import requests  # Library to handle requests
from bs4 import BeautifulSoup  # Library to parse HTML documents
import re  # Library to handle split with regex

# Get the response in the form of HTML
url = "https://en.wikipedia.org/wiki/List_of_animal_names"
table_class = "wikitable sortable jquery-tablesorter"
response = requests.get(url)

# Parse data from the HTML into a Beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable = soup.findAll('table', {'class': "wikitable"})

# Set the table size
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 7)

df = pd.read_html(str(indiatable[1]))
# Convert list to dataframe
df = pd.DataFrame(df[0])


# Function for split and clear collective
def clear_link(text):
    # Clearing []
    result = re.split("\[(.*?)\]", str(text))
    # Clearing NULL values
    result = list(filter(None, result))
    # Clearing numbers
    result = [x for x in result if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
    return result


# Data arrangement, conditions and prints
for index, row in df.iterrows():
    # Data arrangement
    name = row['Animal'][0]
    collective = row["Collective noun"][0]
    collateral = row["Collateral adjective"][0]

    # Conditions and prints
    if collective == "—" or collective == "?":
        print(f"{name} - {collateral}")
    else:
        collective_objects = clear_link(collective)
        indexval = 0
        for i in range(len(collective_objects)):
            print(f"{name} - " + collective_objects[indexval])
            indexval += 1
