"""


https://www.youtube.com/watch?v=txPNMDDWsB8

Uses fontawesome version 5.x
https://github.com/minimaxir/stylecloud

https://fontawesome.com/icons

"""
import stylecloud
from IPython.display import Image
from wordcloud import WordCloud, STOPWORDS


def gen_cloud() -> None:

    stylecloud.gen_stylecloud(
        file_path="keywordcloud\logo.txt",
        icon_name="fab fa-twitter",
        #icon_name="fas fa-yin-yang",
        palette="colorbrewer.qualitative.Paired_3",
        background_color="white",
        gradient="horizontal",
        stopwords=True,
        custom_stopwords=STOPWORDS,
    )

    Image("stylecloud.png")


def main():
    gen_cloud()


if __name__ == "__main__":
    main()
