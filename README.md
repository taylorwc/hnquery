# hnquery - function that scrapes ShowHN's and pushes them to Slack

[Serverless](https://serverless.com) framework-based python lambda function that will post trending ShowHN's to Slack via webhook. Runs on an arbitrary schedule (currently once every 12 hours) and uses an arbitrary karma threshold to determine which ShowHN's are passed (currently 50 votes)

### Adusting parameters
To change the schedule, adjust the `schedule` parameter in `serverless.yml`.

To adjust the karma threshold for which stories get pushed to slack change the `threshold` variable in `handler.py`.

### Webhook URL
Since this was deployed on AWS, I just used [SSM](https://aws.amazon.com/secrets-manager/) for the unique webhook URL and pulled it into an environment variable. If you were deploying to a private repo, you could put the url as a variable in the handler.
