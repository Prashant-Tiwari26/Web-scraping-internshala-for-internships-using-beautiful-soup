# Web-scraping-internshala-for-internships-using-beautiful-soup
The project scrapes the internshala website to look for data science and machine learning internships
every 45 minutes.

## Utility
Although the project looks for only data science and machine learning internships, you can simply 
change the link in the following part of code in `main.py`
```
html = requests.get("https://internshala.com/internships/data-science,machine-learning-internship/stipend-10000/").text
```
in the above part of code to
- Different skill requirement other than Data science and Machine learning
- Different minimum stipend
it will work similarly. You can also change the time interval of scraping and job location depending
on your  requirements.

## How to get started
You will need two libraries if you dont already have them.
- requests
- Beautifulsoup
If not then you can install them by running the follwing code in terminal :
```
pip install requests beautifulsoup4
```
After the installation you can simply run the >main.py
The program will scrape and save internship with given requirements details in a `.txt file`
