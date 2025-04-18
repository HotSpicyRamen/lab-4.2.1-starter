from io import BytesIO
import os


class Backend:
    def __init__(self):
        self.pages = {f.split('.')[0]: f for f in os.listdir("flaskr/static/data/")}
        self.images = {f.split('.')[0]: f for f in os.listdir("flaskr/static/img/")}
        print("Images loaded:", self.images)  # Debug helper

    def get_wiki_page(self, name):
        if name not in self.pages:
            return "No page exists with this name"
        filepath = "flaskr/static/data/" + self.pages[name]
        with open(filepath, 'r') as file:
            return file.read()

    def get_all_page_names(self):
        return self.pages.keys()

    def get_image(self, name):
        if name not in self.images:
            return BytesIO()
        filepath = "flaskr/static/img/" + self.images[name]
        with open(filepath, 'rb') as f:
            return BytesIO(f.read())
