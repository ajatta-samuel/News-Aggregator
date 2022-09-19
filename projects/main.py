# Imports all the methods and variables from each script.
from news_extract import*
from news_nlp import*
from news_scrape import*
import time

# Welcome message
print("Welcome to Newspaper Scrape Project. \n In seconds, you will have"
      " access to the latest articles in the technology section of the New"
      " York Times. \n In addition, you will also be able to know whether the"
      " article is positve or negative as well as the extent of the writer's bias.")

print()

# Getting user input
name = input("Enter your Names: ")

# Console display
print("Welcome, "+name+" !, \nYou will now see the latest articles in"
      " the New York Times...")
print("Extracting article hyperlinks...")
time.sleep(3)
print("Retrieving summaries...")
print()
time.sleep(2)


# Gets all the latest URL's from the NY Times Technology Section. (see news_extract.py for more detail)
content_string = get_content_string("https://www.nytimes.com/section/technology")
start_indices, end_indices = find_occurrences(content_string)
url_list = get_all_urls(start_indices, end_indices, content_string)

# Getting the article summary and performing sentiment analysis on the chosen URL.(see new.scrape.py for more info)
for url in url_list:
      print("Article URL: " + str(url))
      article_summary = summarize_article(url)
      find_sentiment(article_summary)
      print("-------------------------------------")
      time.sleep(7) #allowing user to get through all the text.

# Closing Messages
print()
print("The article have been successfully extracted!")
print("In total, we were able to extract " + str(len(url_list)) + " different article," )
print("Thanks for participating  " + name + "!")