from Downloader import Downloader
import os


def get_urls():
    url_list = []
    file_path = 'urls.txt'
    with open(file_path) as fp:
        line = fp.readline()
        while line:
            url_list.append(line.strip())
            line = fp.readline()
    return url_list


directory = os.getcwd() + "/IMAGES"

lis = get_urls()

instance_list = [Downloader(lis[i], directory) for i in range(len(get_urls()))]
