from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
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
    message = 'Hello World'
    return render_template('index.html',message = message, title = title,general = general_news,business=business_news,entertainment=entertainment_news,health=health_news,science=science_news,sports=sports_news,technology=technology_news)
