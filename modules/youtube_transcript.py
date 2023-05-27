import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeTranscript:
    def __init__(self, text):
        self.url = re.search("(?P<url>https?://[^\s]+)", text).group("url")
        self.id = self.get_video_id(self.url)


    def get_video_id(self, url):
        # eğer https yoksa, ekle
        if url.startswith(("youtu", "www")):
            url = "https://" + url

        query = urlparse(url)

        if "youtube" in query.hostname:
            if query.path == "/watch":
                return parse_qs(query.query)["v"][0]
            elif query.path.startswith(("/embed/", '/v/')):
                return query.path.split("/")[2]
        elif "youtu.be" in query.hostname:
            return query.path[1:]  # https://youtu.be/Tz9W9-u_6dw
        else:
            raise ValueError
