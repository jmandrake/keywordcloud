import numpy as np
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import PIL.Image

"""Resources

Word Cloud in python | Word cloud tutorial
https://www.youtube.com/watch?v=4N_exdTyGHk



"""

# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# stop_words = set(stopwords.words("english"))


# def data_processing(data):
#     # Lowercase text
#     data_lc = data.lower()
#     # Tokenize the text
#     data_tokens = word_tokenize(data_lc)
#     # Remove stop words
#     processed_words = [w for w in data_tokens if not w in stop_words]
#     return " ".join(processed_words)


def gen_cloud(txt, bgfile=None, bgcolor="white"):
    """_summary_

    Args:
        txt (str): _description_
        bgfile (str, optional): _description_. Defaults to None.
        bgcolor (str, optional): _description_. Defaults to "white".
    """
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


# def get_word_cloud(txt, bgcolor="white", mask=None):
#     clean_str = re.sub(r'[^\x00-\x7f]',r'', txt)
#     stopwords = ['and', 'or', 'the', 'wikipedia', 'wikimedia', 'commons', 'this', 'to', 'â', 'Â', 'a', 'o', 'you', 'is', 'it', 'of','your'] + list(STOPWORDS)
#     if not mask is None:
#         wc = WordCloud(stopwords=stopwords, mask=mask, background_color=bgcolor).generate(clean_str)
#     else:
#         wc = WordCloud(stopwords=stopwords, background_color=bgcolor).generate(clean_str)
#     #plt.rcParams["figure.figsize"] = 8,8
#     plt.imshow(wc)
#     plt.axis("off")
#     plt.savefig("test.png")
#     plt.show()


def main():
    # txt = "Hello World"
    # with open("sample3.txt", "r", encoding="utf-8") as rfile:
    #     txt = rfile.read()
    # get_word_cloud(txt)

    # with PIL.Image.open("heart_logo.png") as png:
    #     mask = np.array(png)
    # get_word_cloud(txt, mask)

    with open("sample.txt", "r", encoding="utf-8") as rfile:
        txt = rfile.read()
    bgfile = "logo.png"
    gen_cloud(txt, bgfile, "white")


if __name__ == "__main__":
    main()
