import os
import json
import requests

def showhn(event, context):

    # get the current ShowHN's
    current_shows = requests.get("https://hacker-news.firebaseio.com/v0/showstories.json")
    current_shows = current_shows.json()

    # pull out those above the arbitrary vote threshold
    threshold = 50
    above_threshold = []

    # parse relevant story details
    for show in current_shows:
        req_string = "https://hacker-news.firebaseio.com/v0/item/" + str(show)+ ".json"
        show_details = requests.get(req_string)
        show_details = show_details.json()
        if show_details.get("score") > threshold:
            relevant = {"title": show_details.get("title"), "url": show_details.get("url"), "score": show_details.get("score")}
            above_threshold.append(relevant)
    
    # format them for message attachment in slack
    attachment_formatted = []
    for item in above_threshold:
        holder = {}
        holder['fallback'] = item['title']
        holder['color'] = '#69a97f'
        holder['title'] = item['title']
        if item['url']:
            holder['title_link'] = item['url']
        else:
            holder['title_link'] = 'https://news.ycombinator.com'
        holder['text'] = 'Score: ' + str(item['score']) + ' ... URL: ' + holder['title_link']
        attachment_formatted.append(holder)

    # make POST request via webhook
    headers = {'Content-type': 'application/json'}
    url = os.environ['SLACK_URL']
    req = requests.post(url,json={'text': 'digest from today', 'attachments': attachment_formatted},headers=headers)

    return {
        "message": "ShowHN Scrape Completed Successfully...",
        "event": event
    }
