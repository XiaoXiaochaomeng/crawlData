import requests
import multiprocessing

PROCESSES = 12

URL = 'https://vi.wikipedia.org/w/api.php'

PARAMS={
    'action': 'query',
    'format': 'json',
    'list': 'categorymembers',
    'utf8': 1,
    'formatversion': 'latest',
    'cmprop': 'ids|title|type',
    'cmtype': 'subcat',
    'cmlimit': 'max',
}

cat_list = list(set(open("SubCatPageID.txt", 'r')))
session = requests.Session()
subcategory_page_ids = set()

def get_subcategory_page_ids(*categories):
    thread_name = multiprocessing.current_process().name
    testTitle = open("/home/manh/PycharmProjects/pythonProject/ACSLinkPaper/test/" + thread_name, 'a')
    # subcat_list = open("SubCat Lists.txt", 'a')
    if isinstance(categories[0], str):
        categories = [categories[0]]
    else:
        categories = list(categories)[0]
    for category in categories:
        try:
            PARAMS['cmtitle'] = category.strip()
            response = session.get(url=URL, params=PARAMS).json()
            category_members = response['query']['categorymembers']

            for member in category_members:
                if member['type'] == 'subcat':
                    if member['pageid'] not in check_catID:
                        check_catID.add(member['pageid'])
                        subcategory_page_ids.add(member['pageid'])
                        get_subcategory_page_ids(member['title'])
                        infor = str(member['pageid']) + " " + member['title']
                        testTitle.write(infor + "\n")
                        print(infor + " " + thread_name)

        except:
            continue

check_catID = set()

# get_subcategory_page_ids(cat_list[6])


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=PROCESSES)
    pool_outputs = pool.starmap(get_subcategory_page_ids, [(cat_list[156],),
                                                           (cat_list[157],),
                                                           (cat_list[158],),
                                                           (cat_list[159],),
                                                           (cat_list[160],),
                                                           (cat_list[161],),
                                                           (cat_list[162],),
                                                           (cat_list[163],),
                                                           (cat_list[164],),
                                                           (cat_list[165],),
                                                           (cat_list[165],),
                                                           (cat_list[165],), ])

    pool.close()
    pool.join()

    page_list = open("SubCat.txt", 'a')
    for i in subcategory_page_ids:
        page_list.write(str(i) + '\n')

