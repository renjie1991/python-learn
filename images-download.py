import requests
import time
import random
from multiprocessing import Pool


def download_image(num):
    file_path = 'images'
    base_url = 'http://cued.xunlei.com/demos/publ/img/P_'
    url = base_url + num + '.jpg'
    response = requests.get(url)
    file_name = str(int(time.time())) + \
        str(random.randint(000000, 999999)) + '.jpg'
    file = file_path + '/' + file_name
    with open(file, 'wb') as f:
        f.write(response.content)


def run():
    for i in range(0, 10):
        num = '{:0>3}'.format(i)
        download_image(num)
        print(num + ' OK')


if __name__ == '__main__':

    pool = Pool(2) 

    pool.apply_async(run,(1,))
