"""从Gravatar获取头像和公开信息
doc :https://en.gravatar.com/site/implement/
"""

import urllib.parse
import hashlib


class Gravatar():
    def __init__(self, email, default="mm", size=60):
        self.email = email
        #default image, doc: https://en.gravatar.com/site/implement/images/
        self.default = default
        self.size = size

    def hash_email(self):
        """email hash
        """
        return hashlib.md5(self.email.lower().encode()).hexdigest()

    def get_image(self):
        image_url = "http://www.gravatar.com/avatar/" + self.hash_email() + "?"
        image_url += urllib.parse.urlencode(({'d': self.default, 's': str(self.size)}))
        return image_url

    def get_page(self):
        return "http://www.gravatar.com/" + self.hash_email()

    def get_profile_data(self):
        """return json format
        """
        return self.get_page() + '.json'


if __name__ == '__main__':
    person = Gravatar('imaguowei@gmail.com')
    print(person.get_image())
    print(person.get_page())
    print(person.get_profile_data())

