class News:
    def __init__(self,link,picture,description):
        self.link = link
        self.picture = picture
        self.description =description
    
    def get_text(self):
        return self.link + self.description
