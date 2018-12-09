from urllib.parse import urlparse
from urllib.parse import urlsplit
from urllib.request import urlopen
from urllib.request import urlretrieve
from os.path import basename
import os
import re


class Downloader:
    def __init__(self, p_url, p_directory=None):
        self.img_url = p_url
        self.img_directory = p_directory

        self.set_standards()

        self.create_structure(self.img_url)

    def set_standards(self):
        if self.img_directory is None:
            self.img_directory = os.getcwd() + "/img"

    def format_url(self, url):
        if ' ' not in url[-1]:
            url = url.replace(' ', '%20')
            return url
        elif ' ' in url[-1]:
            url = url[:-1]
            url = url.replace(' ', '%20')
            return url

    def create_structure(self, p_url):
        parse_object = urlparse(p_url)
        dir_name = basename(parse_object.path)
        root = basename(parse_object.netloc)
        if not os.path.exists(self.img_directory):
            os.mkdir(self.img_directory)
        if not os.path.exists(self.img_directory + "/" + dir_name):
            os.mkdir(self.img_directory + "/" + dir_name)
        os.chdir(self.img_directory + "/" + dir_name)

        url_content = urlopen(p_url).read().decode('utf-8')
        img_urls = re.findall('img .*?src="(.*?)"', url_content)

        print(str(len(img_urls)) + " Images found in " + dir_name + "!")

        for img_url in img_urls:
            try:
                img_url = self.format_url(img_url)
                file_name = basename(urlsplit(img_url)[2])
                urlretrieve("http://" + root + img_url, file_name)

            except Exception as e:
                print(e)
