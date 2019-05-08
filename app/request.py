from app import app
from newsapi import NewsApiClient
from .models import news

 # Getting api key
key = app.config['NEWS_API_KEY']



def get_sources(Category):
    '''
    Function that gets the json response to our url request
    '''
    newsapi = NewsApiClient(api_key=key)

    news_sources = newsapi.get_sources(
                            category= Category,
                            language='en'
                            )
    
    news_results = process_results(news_sources)

    return news_results