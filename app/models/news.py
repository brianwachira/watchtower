class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,news_id,name,description,url,category,language,country):
        self.news_id = news_id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        