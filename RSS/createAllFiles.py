from MakeEpisode import MakeEpisodeFile
from RssReader import RssReader

if __name__ == "__main__":
    thatsCoolNews = RssReader()
    makeEpisodeFiles = MakeEpisodeFile(thatsCoolNews.episodes)

    makeEpisodeFiles.run()


