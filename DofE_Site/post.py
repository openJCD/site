class Post():
    def __init__(self, dict: dict = {'title':'', 'image_url':'', 'description':''}):
        self.data = dict
    
    def get_title(self) -> str :
        return self.data['title']
    
    def get_image_url(self) -> str :
        return self.data['image_url']

    def get_description(self) -> str :
        return self.data['description']     
    
    def set_full_post_data(self, dict):
        self.data = dict;

    def set_title(self,title:str):
        self.data['title'] = title

    def set_image_url(self,image_url:str):
        self.data['image_url'] = image_url

    def set_description(self,description:str):
        self.data['description'] = description
