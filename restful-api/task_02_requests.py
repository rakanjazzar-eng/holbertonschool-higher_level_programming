#!/usr/bin/python3
"""Fetches posts from JSONPlaceholder, prints titles and saves to CSV."""
import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetches all posts, prints the status code and each post title."""
    response = requests.get(URL)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """Fetches all posts and saves id, title and body to posts.csv."""
    response = requests.get(URL)
    if response.status_code == 200:
        posts = [{"id": p["id"], "title": p["title"], "body": p["body"]}
                 for p in response.json()]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
