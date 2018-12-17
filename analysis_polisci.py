import csv
import pandas
import numpy
import matplotlib.pyplot as plt


my_file = 'snopes.csv'
updated_file = 'us_arrests_updated.csv'
verasities = ['', 'correct-attribution', 'false', 'legend', 'misattributed', 'miscaptioned', 'mixture', 'mostly-false', 'mostly-true', 'no-rating', 'outdated', 'research-in-progress', 'scam', 'true', 'unproven']
categories = ['animals', 'automobiles', 'ballot-box', 'business', 'business-politics', 'charity', 'cokelore', 'college', 'computers', 'conspiracy-theories', 'controversy', 'crime', 'crime-politics', 'disney', 'embarrassments', 'entertainment', 'environment', 'food', 'fraud', 'glurge-gallery', 'history', 'holidays', 'horrors', 'humor', 'hurricane-katrina', 'immigration', 'inboxer-rebellion', 'junk-news', 'language', 'legal', 'legal-affairs', 'love', 'luck', 'media-matters', 'medical', 'medical-politics', 'military', 'military-politics', 'nsfw', 'oldwivestales', 'photos', 'political-quotes', 'politicians', 'politics', 'politics-guns', 'politics-race', 'quotes', 'racial-rumors', 'religion', 'religion-politics', 'science', 'september-11', 'sexuality', 'soapbox', 'sports', 'superstition', 'technology', 'terrorism', 'travel', 'uncategorized', 'viral-phenomena', 'war', 'weddings']

def import_data(delimited_file):
    """
    imports the a delimited file and casts the data to a list
    """
    with open(delimited_file, 'r') as csvfile:
        all_data = list(csv.reader(csvfile, delimiter=','))
    return all_data


def seperate_headings_from_data(data):
    """
    seperates the headings from the data
    """
    headings = data[0]
    data.pop(0)
    print(headings)
    print(pandas.DataFrame(data, columns=headings))
    return headings

    

def get_category_types(data):

    category = []
    for article in data:
        temp = article[5].split()
        for cat in temp:
            category.append(cat)
        #print(article[5])
    category = list(set(category))
    category.sort()
    print(category)
    return category

def get_verasity_types(data):

    verasity = []
    for article in data:
        verasity.append(article[4])
        #print(article[5])
    verasity = list(set(verasity))
    verasity.sort()
    print(verasity)
    return verasity

def get_articles_of_2016(data):
    articles = []
    d16 = "2016"
    d70 = "1970"
    for article in data:
        if (d16 in article[1] or d70 in article[1]):
            articles.append(article)
    return articles

def get_articles_of_2017(data):
    articles = []
    d17 = "2017"

    for article in data:
        if (d17 in article[1]):
            articles.append(article)
    return articles

def get_articles_of_2018(data):
    articles = []
    d18 = "2018"

    for article in data:
        if (d18 in article[1]):
            articles.append(article)
    return articles

def get_articles_of_category(category, data):
    articles = []
    check_category = category

    for article in data:
        if(check_category in article[5]):
            articles.append(article)
    return articles

def get_articles_of_verasity(verasity, data):
    articles = []
    check_verasity = verasity

    for article in data:
        if(check_verasity in article[4]):
            articles.append(article)
    return articles

def get_articles_of_keyword(keyword, data):
    articles = []

    for article in data:
        content = ""
        content = content + article[2] + article[3] + article[7]
        if(keyword in content):
            articles.append(article)
    return articles


def show_contents(articles):
    for article in articles:
        date = article[1]
        title = article[2]
        claim = article[3]
        verasity = article[4]
        print("Title: " + title)
        print("Date: " + date)
        print("Claim: " + claim)
        print("Fact Check: " + verasity)
        print("-------------------------")

def write_contents(articles, file):
    for article in articles:
        date = article[1]
        title = article[2]
        claim = article[3]
        verasity = article[4]
        file.write("Title: " + title + "\n")
        file.write("Date: " + date + "\n")
        file.write("Claim: " + claim + "\n")
        file.write("Fact Check: " + verasity + "\n")
        file.write("-------------------------" + "\n")

def show_by_verasity(data):
    print("-- For all articles in 2016")
    for i in verasities:
        temp = 0
        for article in data:
            if(i == article[4]):
                temp = temp + 1
        if(i == ""):
            print("No Value (\" \"): "+ str(temp))
        else:
            print(i + ": " + str(temp))

def show_by_category(data):
    print("-- For all articles from 2016 ~ 2018 --")
    for i in categories:
        temp = 0
        for article in data:
            if(i in article[5]):
                temp = temp + 1
        if(i == ""):
            print("No Value (\" \"): "+ str(temp))
        else:
            print(i + ": " + str(temp))


if __name__ == '__main__':
    
    # Trim data for usage
    data = import_data(my_file)
    headings = seperate_headings_from_data(data)

    # Display For PoliSci Paper

    print(len(data)) # 총 기사 개수
    print(len(verasities)) # veracity 개수
    print(len(categories)) # category 개수
 
    show_by_category(data) # 그림1
    show_by_verasity(data) # 그림2
    data_politics = get_articles_of_category("politic", data)
    print(len(data_politics))
    show_by_verasity(data_politics) # 그림3

    # 연도별 데이터
    data2016 = get_articles_of_2016(data) # Data 오염 상 1970으로 지정된 2017년 이전의 데이터 고려 (snopes.csv 참고)
    data2017 = get_articles_of_2017(data)
    data2018 = get_articles_of_2018(data)

    data_science = get_articles_of_category("science", data)
    data_medicine = get_articles_of_category("medic", data)
    data_sci = data_science + data_medicine # 중복 제거
    show_by_verasity(data_sci)

    mixture_poli = get_articles_of_verasity("mixture", data_politics)
    #file1 = open("text1.txt", "w")
    #write_contents(mixture_poli, file1) # text1 creation

    data_politicians = get_articles_of_category("politicians", data)
    print(len(data_politicians))
    show_by_verasity(data_politicians)
    #file2 = open("text2.txt", "w")
    #write_contents(data_politicians, file2) # text2 creation

    
    #
    f_attribute = get_articles_of_verasity("misattributed", data)
    t_attribute = get_articles_of_verasity("correct-attribution", data)
    f_captioned = get_articles_of_verasity("miscaptioned", data_politics)
    print("Attribution articles:")
    print("  False: " + str(len(f_attribute)))
    print("  True: " + str(len(t_attribute))) # <그림6>
    print("Photo News: ")
    print("  False: " + str(len(f_captioned)))
    
    trump = get_articles_of_keyword("Trump", data2016)
    trump_politics = get_articles_of_category("politics", trump)
    clinton = get_articles_of_keyword("Clinton", data2016)
    clinton_politics = get_articles_of_category("politics", clinton)
    republic = get_articles_of_keyword("republic", data2016)
    republic_politics = get_articles_of_category("politics", republic)
    democrat = get_articles_of_keyword("democrat", data2016)
    democrat_politics = get_articles_of_category("politics", democrat)
    show_contents(trump_politics)
    print("Number of Articles in 2016: ")
    print("Total: " + str(len(data2016)))
    print("Trump: " + str(len(trump)))
    print("Clinton: " + str(len(clinton)))
    print("Republican Party: " + str(len(republic)))
    print("Democratic Party: " + str(len(democrat))) # <그림7>

    print("Donald Trump")
    show_by_verasity(trump)
    print("Hillary Clinton")
    show_by_verasity(clinton)
    
    file_t = open("text_t.txt", "w")
    write_contents(trump, file_t) # trump text creation
    file_c = open("text_c.txt", "w")
    write_contents(clinton, file_c) # clinton text creation
    