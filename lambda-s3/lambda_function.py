import boto3
from urllib.parse import unquote_plus
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import PIL.Image

            
s3_client = boto3.client('s3')
            
def resize_image(image_path, resized_path):
  with Image.open(image_path) as image:
    image.thumbnail(tuple(x / 2 for x in image.size))
    image.save(resized_path)
            
def gen_cloud(txtfile, pngfile, outputfile, bgcolor="white"):
    """_summary_

    Args:
        txtfile (str): text filename with keywords.
        bgfile (str, optional): background imag filename.
        bgcolor (str, optional): background color. Defaults to "white".
    """
    with open(txtfile, "r", encoding="utf-8") as rfile:
        txt = rfile.read()
    clean_str = re.sub(r"[^\x00-\x7f]", r"", txt)
    stopwords = [
        "and",
        "or",
        "the",
        "wikipedia",
        "wikimedia",
        "commons",
        "this",
        "to",
        "â",
        "Â",
        "a",
        "o",
        "you",
        "is",
        "it",
        "of",
        "your",
    ] + list(STOPWORDS)
    python_mask = np.array(PIL.Image.open(pngfile))
    colormap = ImageColorGenerator(python_mask)
    wc = WordCloud(
        stopwords=stopwords,
        mask=python_mask,
        background_color=bgcolor,  # None (use None with mode='RGBA')
        #    mode="RGBA",
        #    contour_color="grey",
        #    contour_width=1,
        max_words=500,
    ).generate(clean_str)
    wc.recolor(color_func=colormap)
    plt.figure(figsize=(15, 10), facecolor="none")
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(outputfile)
    #plt.show()       
            
            
def lambda_handler(event, context):
  for record in event['Records']:
    bucket = record['s3']['bucket']['name']
    key = unquote_plus(record['s3']['object']['key'])
    tmpkey = key.replace('/', '').replace('.png', '')
    
    key_png = key    
    download_path_png = '/tmp/{}.png'.format(tmpkey)
    s3_client.download_file(bucket, key_png, download_path_png)
    
    key_txt = key.replace('.png', '.txt')
    download_path_txt = '/tmp/{}.txt'.format(tmpkey)
    s3_client.download_file(bucket, key_txt, download_path_txt)
    
    upload_path_output = '/tmp/{}-output.png'.format(tmpkey)
    
    gen_cloud(download_path_txt, download_path_png, upload_path_output, bgcolor="white")
    
    output_bucket = bucket.replace('input', 'output')
    output_filename = '{}-output.png'.format(tmpkey)
    s3_client.upload_file(upload_path_output, output_bucket, output_filename)