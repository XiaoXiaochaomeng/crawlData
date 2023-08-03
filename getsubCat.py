import requests

def get_subcategory_pageids(cat_title):
    URL = 'https://en.wikipedia.org/w/api.php'
    PARAMS = {
        'action': 'query',
        'format': 'json',
        'prop': 'categories',
        'titles': cat_title
    }

    response = requests.get(url=URL, params=PARAMS).json()
    pageid = list(response['query']['pages'].keys())[0]
    subcategories = response['query']['pages'][pageid]['categories']

    subcategory_pageids = []
    for subcategory in subcategories:
        if subcategory['title'].startswith('Category:'):
            subcat_title = subcategory['title'][9:]
            subcat_pageid = get_pageid_by_title(subcat_title)
            subcategory_pageids.append(subcat_pageid)

    return subcategory_pageids

def get_pageid_by_title(page_title):
    URL = 'https://en.wikipedia.org/w/api.php'
    PARAMS = {
        'action': 'query',
        'format': 'json',
        'prop': 'info',
        'titles': page_title
    }

    response = requests.get(url=URL, params=PARAMS).json()
    pageid = list(response['query']['pages'].keys())[0]

    return pageid

health_subcat_pageids = get_subcategory_pageids('Sức khỏe')

for pageid in health_subcat_pageids:
    print(pageid)
