from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp

    def set_user(self, user):
        self.user = user
        
    def _date_to_string(self):
        return self.timestamp.strftime("%A, %b %d, %Y")


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
         super(TextPost, self).__init__(text, timestamp)
         self.user = None

    def __str__(self):
         return "@{name}: \"{text}\"\n\t{time}".format(name=self.user.full_name, 
                text=self.text, time=self._date_to_string())


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
         super(PicturePost, self).__init__(text, timestamp)
         self.user = None
         self.image_url = image_url

    def __str__(self):
         return "@{name}: \"{text}\"\n\t{url}\n\t{time}".format(name=self.user.full_name, 
         text=self.text, url = self.image_url, time=self._date_to_string())


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
         super(CheckInPost, self).__init__(text, timestamp)
         self.user = None
         self.latitude = latitude
         self.longitude = longitude

    def __str__(self):
         return "@{fname} Checked In: \"{text}\"\n\t{latitude}, {longitude}\n\t{time}".format(fname=self.user.first_name, 
         text=self.text, latitude=self.latitude, longitude=self.longitude, time=self._date_to_string())
