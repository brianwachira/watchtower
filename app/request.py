from app import app
from newsapi import NewsApiClient
from .models import News

 # Getting api key
key = app.config['NEWS_API_KEY']



def get_sources(Category):
    '''
    Function that gets the json response to our url request
    '''
    newsapi = NewsApiClient(api_key=key)

    news_sources_response = newsapi.get_sources(
                            category= Category,
                            language='en'
                            )
    if news_sources_response['sources']:
        news_results_list = news_sources_response['sources']

        news_results = process_results(news_results_list)

    return news_results


def process_results(news_sources_list):
    '''
    Function that processes the news result and transforms them to a list of objects
    Args:
        news_sources_list: A list of dictionaries that contain news details
    Returns:
            news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_sources_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        news_object = News(id,name,description,url)
        news_results.append(news_object)

    return news_results