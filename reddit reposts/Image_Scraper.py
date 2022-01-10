import praw
import requests
import cv2
import numpy as np

def scraper(quantity, domain):
    counter = 1
    r = praw.Reddit(client_id='ERcR3P8Vs-gjHYHaH7tmsQ',
                    client_secret='DkXu1wsd_gTq8GCgrIrRCtchbAr_6A',
                    user_agent='imageloader')


    page = r.subreddit(domain)
    new_posts = page.new(limit = quantity)

    for post in new_posts:

        if "jpg" in post.url.lower() or "png" in post.url.lower():
            resp = requests.get(post.url.lower(), stream=True).raw
            file = np.asarray(bytearray(resp.read()), dtype="uint8")
            file = cv2.imdecode(file, cv2.IMREAD_COLOR)
            cv2.imwrite("E:/Documents/GitHub/ethan-data-stuffs/reddit reposts/scraped images/""reddit image"+str(counter)+".jpg", file)
            counter+=1













