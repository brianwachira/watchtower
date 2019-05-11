from flask import render_template,request,redirect
from . import main
from ..request import get_sources,get_sources_news

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    
    general_news= get_sources('general')
    business_news = get_sources('business')
    entertainment_news =get_sources('entertainment')
    health_news= get_sources('health')
    science_news=get_sources('science')
    sports_news=get_sources('sports')
    technology_news=get_sources('technology')
    
    title = 'Home - Welcome to Watch Tower'
    brandname = 'Welcome to Watch Tower'
    mantra = 'Get your news from anywhere in the world'
    message = 'Hello World'
    return render_template('index.html',message = message, title = title,brandname = brandname, mantra = mantra,general = general_news,business=business_news,entertainment=entertainment_news,health=health_news,science=science_news,sports=sports_news,technology=technology_news)

@main.route('/news/<news_id>')
def news(news_id):
    '''
    View news page function that returns news from news source
    '''
    news = get_sources_news(news_id)
    title = f'{news_id}'

    return render_template('source_news.html',title=title,news=news)