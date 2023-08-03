import requests

ls = list()

def get_pageids_by_category_pageid(cat_id):
    URL = 'https://vi.wikipedia.org/w/api.php'

    PARAMS = {
        'action': 'query',
        'format': 'json',
        'list': 'categorymembers',
        'utf8': 1,
        'formatversion': 'latest',
        'cmprop': 'ids|title|type',
        'cmtype': 'subcat|page',
        'cmlimit': 'max'
    }

    PARAMS['cmpageid'] = cat_id
    response = requests.get(url=URL, params=PARAMS).json()
    category_members = list(response['query']['categorymembers'])
    for i in category_members:
        ls.append(str(i['pageid']) + " " + i['title'])

    return ls

file_write = open("SubCat Lists.txt", 'w')
file_read = list(open("SubCatPageID.txt", 'r'))
check_page = set()
check_cat = set()

def getPageID(file_read):
    for i in file_read:
        if ("phim" in i.lower()) or ("truyện" in i.lower()) or ("khiêu dâm" in i.lower()) or ("tự tử" in i.lower()) or ("lạm dụng tình dục" in i.lower()) or ("mại dâm" in i.lower()):
            continue
        list_page = []
        cat_id = i.strip().split(" ")[0]
        ls = get_pageids_by_category_pageid(cat_id)
        for j in ls:
            if "Thể loại" in j:
                check_cat.add(j)
            if (j not in check_page) and ("Thể loại" not in j):
                check_page.add(j)
                list_page.append(j)
        if len(list_page) > 0:
            file_write.write("PageID của cat " + i)
            print("PageID của cat " + i.strip())
            file_write.write(str(list_page) + "\n")
            print(list_page)

getPageID(file_read)
ls_check_cat = list(check_cat)
for i in ls_check_cat:
    if i not in file_read:
        getPageID([i])
        file_read.append(i)

