import webbrowser

class snopes_article(object):
    def __init__(self, post_num=None, date=None, title=None, claim=None, verasity=None, category=None, share=None, tags=None, url=None, **kwargs):
        self.post_num = post_num
        self.date = date
        self.title = title
        self.claim = claim
        self.verasity = verasity
        self.category = category
        self.share = share
        self.tags = tags
        self.url = url

    @property
    def goto(self):
        try:
            webbrowser.open(self.url)
        except:
            print("Error in getting {}".format(self.url))