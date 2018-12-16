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

def show_verasity_distritubtion(data):
    v_distribution = []
    for v in verasities:
        v_distribution.append([v,0])

    for article in data:
        for v in v_distribution:
            if(article[4] == v[0]):
                v[1] = v[1]+1

    print(v_distribution)


def show_category_distribution(articles):
    c_distribution = []
    for c in categories:
        c_distribution.append([c,0])

    for article in data:
        for c in c_distribution:
            if(c[0] in article[5]):
                c[1] = c[1]+1

    print(c_distribution)

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

def calculate_statistics(crime):
    """
    calculates mean, media, and standard Deviation
    """
    return numpy.mean(crime), numpy.median(crime), numpy.std(crime)


def calculate_min_and_max(crime):
    """
    calculates min and max values
    """
    return numpy.min(crime), numpy.max(crime)


def get_state(crime, min_max, data):
    """
    associates the state with the min and max values
    """
    state = []
    min_index = crime.index(min_max[0])
    max_index = crime.index(min_max[1])
    for crime in data:
        state.append(crime[0])
    return state[min_index], state[max_index]


def urban_percent(data):
    """
    calculates median using helper function, then returns
    list of values ("low" or "high") based on whether the
    UrbanPop is above or below the median
    """
    urban_pop = []
    urban_level = []
    for column in data:
        urban_pop.append(int(column[3]))
        if int(column[3]) > calculate_median(urban_pop):
            urban_level.append("high")
        else:
            urban_level.append("low")
    return urban_level


def add_data(data, new_list):
    """
    append a new list into a list of a list
    """
    for count in range(len(data)):
        data[count].append(new_list[count])
    return data


def add_headings_to_data(data, headings):
    """
    add the headings back to the data
    """
    headings.append("UrbanLevel")
    data.insert(0, headings)
    return data


def export_data(delimited_file, data):
    """
    export the new data list to a new delimited file
    """
    with open(delimited_file, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in data:
            writer.writerow(row)


def create_frequency_distribution(crime):
    """
    creates a frequency distribution chart
    """
    hist, bin_edges = numpy.histogram(crime, bins=10)
    return hist, bin_edges


def create_histogram(crime):
    """
    creates a histogram in matplotlib
    """
    plt.hist(crime, facecolor='green', label='murders')
    plt.title("Murder Rate Histogram")
    plt.xlabel("murder rates")
    plt.ylabel("# of murders")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = import_data(my_file)
    headings = seperate_headings_from_data(data)
    data2016 = get_articles_of_2016(data)
    data2017 = get_articles_of_2017(data)
    data2018 = get_articles_of_2018(data)
    show_category_distribution(data2018)
    show_verasity_distritubtion(data2018)
    trump = get_articles_of_keyword("Trump", data2016)
    trump_politics = get_articles_of_category("politics", trump)
    show_contents(trump_politics)