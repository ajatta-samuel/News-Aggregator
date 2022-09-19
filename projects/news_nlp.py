# This program performs sentiment analysis on news articles using TextBlob.

from textblob import TextBlob

news_summary = """A woman died from treatment delays after a hospital in Germany hit by a cyberattack was forced to turn away emergency patients.
This is a small sample of the toll from ransomware attacks, in which hackers break into computer networks and freeze the digital information until the targeted organization or city pays for its release.
Victims have two bad choices: Give in to extortion and hope the criminals didn’t do too much damage, or refuse and risk the hackers releasing or deleting essential information.
I spoke to Charles Carmakal, an executive with the cybersecurity response company FireEye Mandiant, about the root causes and fixes for ransomware attacks.
What are the root causes of ransomware?"""


# Given a news summary, extracts polarity and subjectivity metrics, returning both in a readable format.
def find_sentiment (news_story):
    news = TextBlob(news_story)
     # Iterates over each sentence in the news, extracts the sentiment, and stores each inside of a list.
    sentiments = []
    for sentence in news.sentences:
        sentiment = sentence.sentiment
        for metric in sentiment:
            sentiments.append(metric)
    

    polarity_data = []
    subjectivity_data = []
    for i in range(len(sentiments)):
        if i % 2 == 0:
            polarity_data.append(sentiments[i])
        else:
            subjectivity_data.append(sentiments[i])

    # Averages of both sentiment lists are calculated.
    polarity_average = calculate_average(polarity_data)
    subjectivity_average = calculate_average(subjectivity_data)


    # Displays the sentiment that relates to the averages on the console. 
    print()
    print("FINAL ANALYSIS!")
    print("----------------------------------")
    print("Polarity: " + calculate_sentiment(polarity_average , "polarity"))
    print("Subjectivity: " + calculate_sentiment(subjectivity_average , "subjectivity"))

# Helper for find_sentiment method
#---------------------------------------------------------------

# Calculates and returns the average of all.
def calculate_average (list):
    return sum(list) / len(list)

def calculate_sentiment(sentiment , type):
    sentiment_category = ""
    if type == "polarity":
        if sentiment > 0.75:
            sentiment_category = "Extremely positive."
        elif sentiment > 0.5:
            sentiment_category = "Significantly positive."
        elif sentiment > 0.3:
            sentiment_category = "Fairly positive."
        elif sentiment > 0.1:
            sentiment_category = "Slightly positive."
        elif sentiment < -0.1:
            sentiment_category = "Slightly negative." 
        elif sentiment < -0.3:
            sentiment_category = "Fairly negative."
        elif sentiment < -0.5:
            sentiment_category = "Significantly negative."
        elif sentiment < -0.75:
            sentiment_category = "Extremely negative"
        else:
            sentiment_category = "Neutral."
        return sentiment_category
    elif type == "subjectivity":
        if sentiment > 0.75:
            sentiment_category = "Etremely subjective."
        elif sentiment > 0.5:
            sentiment_category = "Fairly subjective."
        elif sentiment > 0.3:
            sentiment_category = "Fairly objective."
        elif sentiment > 0.1:
            sentiment_category = "Extremely objective."
        return sentiment_category
    else:
        print("Invalid input.")






