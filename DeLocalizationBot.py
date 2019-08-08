import praw

SUBREDDIT_NAME = 'ObnoxiousDev'
KEYWORDS = ['!delocalizeme']
RESPONSE = 'There is a keyword in your comment!'

USER_AGENT = 'script:Delocalization Bot:v0.0 (by /u/feelsobnoxiousman)'

print("Authenticating...")
reddit = praw.Reddit('bot1', user_agent=USER_AGENT)
print("Authenticated as {}".format(reddit.user.me()))

print("Starting comment stream...")
for comment in reddit.subreddit(SUBREDDIT_NAME).stream.comments():
    if comment.saved:
        continue
    has_keyword = any(k.lower() in comment.body.lower() for k in KEYWORDS)
    not_self = comment.author != reddit.user.me()
    if has_keyword and not_self:
        comment.save()
        reply = comment.reply(RESPONSE)
        print("http://reddit.com{}".format(reply.permalink()))

