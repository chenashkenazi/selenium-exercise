
# Web Scraping with Selenium project

This project is a system that collects information from BBC website and Natbag flights board website, saves it in a database using web scraping methods written in python with selenium and beautiful soup

## How to run it?

1. Clone the GitHub repository to your local machine

2. Install MongoDB server

3. Install Kafka server in order to send actions to the system

4. Install standalone chrome browser with the command: `docker run -d -p 4444:4444 selenium/standalone-chrome`

5. Create an image: `docker build -t selenium-exercise .`

6. Run the system: `docker run --rm  --network host -it selenium-exercise:latest`

7. The following should appear:

   ```
      System is starting
      Consuming
   ```

## Actions instructions

Each crawler has two actions:

1. Download the content that currently apeears in the website and save to database

2. Search in database by text

In order to activate each action the user needs to produce a Kafka event that contains JSON.
The JSON must include the following fields:

* **crl**: name of crawler. `"bbc"` for bbc website, `"flights"` for natbag website

* **action**: `download_save` for downloading and saving content, `search` for searching

* **search**: add this field only in case of searching.
  * search for bbc: **text**: words to search
  * search for flights: **text**: words to search, **field**: flight / airline / city / terminal / scheduled_time / updated_time / status
              
Examples:

Download and save content from bbc.com: `{"crl": "flights", "action": "download_save"}`

Search in BBC database: `{"crl": "bbc", "action": "search","search": {"text": "China"}}`

Search in flights database: `{"crl": "flights", "action": "search","search": {"text": "1", "field": "terminal"}}`

## Requirements

- Python3
- Pip3
- Selenium
- BeautifulSoup
- Pymongo
- requests
- Kafka
- Docker

