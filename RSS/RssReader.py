import requests
from bs4 import BeautifulSoup
from Episode import Episode

class RssReader():

    """Goal of object is to grab xml file, Grab Necessary podcast information (i.e. Title, Description)
     and create a Markdown file."""

    def __init__(self, feedUrl = "https://feed.podbean.com/thatscoolnews/feed.xml"):
        self.feedUrl = feedUrl
        self.rssFeed = self.grabRssFeedFromURL()
        self.episodes = self.grabAllEpisodes("item")


    def grabRssFeedFromURL(self):
        # Get XML Feed from That's Cool News XML Feed
        feedResponse = requests.get(self.feedUrl)
        return BeautifulSoup(feedResponse.content, features="xml")


    def grabAllEpisodes(self, episodeTag):
        # Find all the episodes for the specific episode tag.
        episodes = self.rssFeed.find_all(episodeTag)
        storedEpisodes = []
        for episode in episodes:
            title = self.grabEpisodeTitle(episode, "title")
            link = self.grabEpisodeLink(episode, "link")
            description = self.grabEpisodeDescription(episode, "description")
            storedEpisodes.append(Episode(title,link,description))

        return storedEpisodes

    def grabEpisodeTitle(self, episode, titleTag):
        return episode.find(titleTag).contents[0]

    def grabEpisodeLink(self, episode, linkTag):
        return episode.find(linkTag).contents[0]

    def grabEpisodeDescription(self, episode, descriptionTag):
        return episode.find(descriptionTag).contents[0]
