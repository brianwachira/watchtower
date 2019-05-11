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
        

class News_List:
    '''
    News_List class to define News Objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content