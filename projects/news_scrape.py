# This program scrapes and summarizes news articles from the New York Times

from newspaper import Article
import nltk



# Summarizes the article and provides valuable information regarding the article metadata, including images and
# attributions.
def summarize_article(url):
    article = Article(url)

    #SETUP
    article.download()
    article.parse()

    #for text & wording detection
    nltk.download("punkt")
    #calling the Natural Language aparocessor
    article.nlp()

    # Gets the author or authors of the article
    author_string = "Author(s): "
    for author in article.authors:
        author_string += author  # adds all authors (if more than 1) to the author string.
    print(author_string)

    #Formating the date
    date = article.publish_date
    print("Publish Date: " + str(date.strftime("%m/%d/%Y")))

    # Geting the top image of the article
    print("Top Image: " + str(article.top_image))

    #iterating through images
    image_string = "All Images: "
    for image in article.images:
        image_string += "\n\t" + image  # adds a newline and a tab before each image is printed
    print(image_string)
    print()

    # Getting the article summary
    print("A Quick Article Summary")
    print("-----------------------------------")
    print(article.summary)

    return article.summary



