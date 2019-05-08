from app import app
from newsapi import NewsApiClient
from .models import news,news_list

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

def get_sources_news(news_source):
    '''
    Function that takes in a news object and returns news from the news object
    '''
    newsapi = NewsApiClient(api_key=key)

    top_headlines = newsapi.get_top_headlines(
                            sources = news_source.news_.id,
                            language = news_source.language
                            )    
    news_source_object = None
    if top_headlines['articles']:
        top_headlines_lists = top_headlines['articles']

    for top_headlines_list in top_headlines_lists:
            author =  top_headlines_list.get('author')
            title = top_headlines_list.get('title')
            description = top_headlines_list.get('description')
            url = top_headlines_list.get('url')
            urlToImage = top_headlines_list.get('urlToImage')
            publishedAt = top_headlines_list.get('publishedAt')
            content = top_headlines_list.get('content')

    news_source_object = news_list.News_List(author,title,description,url,urlToImage,publishedAt,content)
    
    return news_source_object

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
        news_id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        news_object = news.News(news_id,name,description,url,category,language,country)
        news_results.append(news_object)

    return news_results