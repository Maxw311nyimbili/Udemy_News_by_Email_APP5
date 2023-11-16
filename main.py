# API stands for Application Programming Interfaces
# APIs are meant to be read by computers. Given that you are creating an app that
# gives the latest news the app is most likely, going to need an API to fetch the required information.
# given that you have a lot of data, you can use the debugger to explore the content of that data
import requests

# the API key and the url is obtained from a website called News API. Therefore, the API being created will
# collect news feed from that site and send it to a preferred email address.
api_key = "c153d4982f6f4018ab1db020215bf7c7"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-10-16&sortBy=publishedAt&apiKey=c153d4982f6f4018ab1db020215bf7c7"

# make a request
request_1 = requests.get(url)

# collect data inform of a dictionary
content = request_1.json()
articles = content["articles"] # get a specific part of the data, in this case, "articles"

# loop through the specific data only collecting the title and description of the data
for article in articles:
    print(article["title"])
    print(article["description"] + "\n")
