import requests
import re
import os

from bs4 import BeautifulSoup
from fpdf import FPDF
from PIL import Image
from io import BytesIO

XCROP_VALUE = 36 #36
YCROP_VALUE = 40 #40

def get_picture(trg_url, out_dir='./output'):
    """Extract the picture for a given target URL from scryfall"""
    html_str = requests.get(trg_url).text
    img_url = extract_picture_url(html_str)

    proxi_pics = sorted(
        [f for f in os.listdir(out_dir) if re.match('proxi_[0-9]*.jpeg', f)])
    print(proxi_pics)
    if len(proxi_pics) > 0:
        nbrs = [int(re.search('_(\d+)\.', x).group(1)) for x in proxi_pics]
        last_prox_nr = max(nbrs)
    else:
        last_prox_nr = 0
    print("Adding proxi nr: {}".format(last_prox_nr))

    # get new image and store as next proxi -> safe as backup
    print("Working with url: {}".format(img_url))
    resp = requests.get(img_url)
    print("Response is: {}".format(resp))
    fname = './output/proxi_' + str(last_prox_nr + 1) + '.jpeg'
    img = Image.open(BytesIO(resp.content))
    w, h = img.size

    # crop image by defining a new rectangle (left, upper, right, bottom) pixel
    lc, rc = XCROP_VALUE, w - XCROP_VALUE
    uc, bc = YCROP_VALUE, h - YCROP_VALUE
    print("Croping image and saving")
    img.crop((lc, uc, rc, bc)).save(fname)

    # return file name for further processing
    return fname


def extract_picture_url(html_str):
    """Given a html string of the page parse for the pictures URL"""

    soup = BeautifulSoup(html_str)
    div = soup.find('div', {'class': 'card-image-front'})

    return div.findAll('img')[0]['src']


def compose_proxi_pdf():

    with open('cards.txt', 'r') as url_file:
        urls = url_file.readlines()
        urls = [u.replace('\n', '') for u in urls]

    cards = dict(zip(range(1, len(urls)+1), urls))

    i = 0
    xmarg, ymarg = 0, 20
    xsize = 672 - 2 * XCROP_VALUE
    ysize = 936 - 2 * YCROP_VALUE
    pdf = FPDF(unit='pt', format=(xsize*3 + 300, ysize*3 + 100))
    pdf.add_page()

    for k in cards.keys():
        img = get_picture(cards[k])

        pdf.image(img, xsize * (i%3) + xmarg, ysize * (i//3) + ymarg)
        i += 1

    pdf.output('./proxi_set.pdf')

    return 0


if __name__ == '__main__':
    compose_proxi_pdf()

