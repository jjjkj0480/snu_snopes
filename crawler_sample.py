import bs4, os, requests
import pandas as pd
import random
import time
import article



class SnopesParser(object):

    def __init__(self, start_url=None, start_page=1, page_count=2, **kwargs):
        self.start_url = start_url
        self.seed = 'http://www.snopes.com/fact-check/page/'
        self.start_page = start_page
        self.end_page = start_page + page_count - 1
        self.articles_dict = dict()

    def get_soup(self, url):
        '''
        Function to extract beautiful soup object from the html page.
        '''
        url_text = requests.get(url)
        url_text.raise_for_status()
        soup = bs4.BeautifulSoup(url_text.text, 'html.parser')
        self.soup = soup
        return soup

    def article_parse(self, url):
        '''
        Function to loop over the soup and extract the articles as a dictionary of objects.
        '''
        soup = self.get_soup(url)
        articles_dict = dict()
        raw = soup.find_all('article')
        for i in raw:
            #append article object to dictionary
            article = self.extract_article_info(i)
            articles_dict[article.post_num] = article
        return articles_dict


    def extract_article_info(self, article_content):

        art_object = article.snopes_article()
        art_object.url = article_content.find('a')['href']

        art_object.post_num = [i for i in article_content.find('a')['class'] if 'post-' in i][0]
        art_object.date = article_content.find('p').find('span').text
        art_object.title = article_content.find('h2').text
        art_object.claim = self.get_soup(art_object.url).find('article').find('p').text
        
        art_object.verasity = [i[18:] for i in article_content.find('a')['class'] if 'fact_check_rating-' in i]
        if(art_object.verasity != []): art_object.verasity = art_object.verasity[0]
        else: art_object.verasity = None
        
        art_object.category = [i[20:] for i in article_content.find('a')['class'] if 'fact_check_category-' in i]
        temp = ""
        if(art_object.category != []):
            for i in art_object.category:
                temp += i + " "
        art_object.category = temp

        # art_object.share = ??
        
        art_object.tags = [i[4:] for i in article_content.find('a')['class'] if 'tag-' in i]
        temp = ""
        if(art_object.tags != []):
            for i in art_object.tags:
                temp += i + " "
        art_object.tags = temp
        
        return art_object

    def get_all_articles(self): #once finished running, this will end us with a dictionary of article classes as a class attribute.
        all_articles = dict()
        for i in range(self.start_page, self.end_page + 1):
            url = self.seed + str(i)
            print(" Getting articles from {}".format(url))
            articles_dict = self.article_parse(url)
            all_articles.update(articles_dict)
        self.all_articles = all_articles

    def format_articles(self):
        final_dict = dict()
        for i in self.all_articles:
            final_dict.update({i: self.all_articles[i].__dict__})
        self.data = pd.DataFrame.from_dict(final_dict, orient='index').reset_index(drop=True)

    def run(self):
        self.get_all_articles()
        self.format_articles()
        print("Data Created")

if __name__ == '__main__':
    # x = SnopesParser()
    x = SnopesParser(start_page=1, page_count=10)
    x.run()
    print("Final page covering: {} ~ {}".format(x.start_page, x.end_page))
    x.data.to_csv('samples.csv', index=False, encoding='utf-8')

