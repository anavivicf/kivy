from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        return AsyncImage (source='https://th.bing.com/th/id/OIP.RqfowQCH1KLpG0AHLgZ4WgHaEK?rs=1&pid=ImgDetMain')
    
if __name__ == "__main__":
        MinhaApp().run()