"""
YouTube link örnekleri:
http://youtu.be/Tz9W9-u_6dw,
www.youtube.com/watch?v=Tz9W9-u_6dw&feature=feedu,
http://www.youtube.com/embed/Tz9W9-u_6dw,
http://www.youtube.com/v/Tz9W9-u_6dw?version=3&amp;hl=en_US,
https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6,
youtube.com/watch?v=Tz9W9-u_6dw,
https://www.youtube.com/watch?v=Tz9W9-u_6dw

YouTube link regex: https:\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)(?:[\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?
Link regex: (?P<url>https?://[^\s]+)
"""
