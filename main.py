import requests
from bs4 import BeautifulSoup

# Retrieving HTML data by calling GET request
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# Using Beautiful Soup library to parsing structured data
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# looping through the data to get all the information collected from HTML page
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

    # Printing output here
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()




