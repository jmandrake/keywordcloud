import numpy as np
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import PIL.Image


def gen_cloud(txtfile, bgfile, bgcolor="white"):
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
    python_mask = np.array(PIL.Image.open(bgfile))
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
    plt.savefig("test.png")
    plt.show()


def main():
    pngfile = "logo.png"
    txtfile = "logo.txt"
    gen_cloud(txtfile, pngfile, "white")


if __name__ == "__main__":
    main()
