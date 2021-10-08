

class MakeEpisodeFile():

    def __init__(self, episodes):
        self.episodes = episodes

    def run(self):
        for episode in self.episodes:
            self.createFile(episode)
        return 0

    @staticmethod
    def createFileContents(episode):
        MDcontent = f"""#{episode.title}
        ---
        [Listen Here!]({episode.link}) \\
        ## Description of The Podcast
        {episode.description}"""
        return MDcontent


    def createFile(self, episode):
        with open(f"../Episodes/{episode.title}.md", "w") as markdownFile:
            markdownFile.write(self.createFileContents(episode))
