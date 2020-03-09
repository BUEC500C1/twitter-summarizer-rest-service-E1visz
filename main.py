from twittwer_api import Get_twitter
from textToImage import setAllImg
from imgToVideo import imgToVideo
import sys


def main():
  hashtag = sys.argv[1]
  setAllImg(hashtag)
  imgToVideo(hashtag)


if __name__=="__main__":
    main()
