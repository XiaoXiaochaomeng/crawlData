import re
import requests
import multiprocessing

PROCESSES = 12

file_read = list(open("Pageid.txt", 'r'))

def get_page_content(pageid):
    URL = 'https://vi.wikipedia.org/w/api.php'
    PARAMS = {
        'action': 'query',
        'format': 'json',
        'utf8': 1,
        'prop': 'extracts',
        'explaintext': True,
        'pageids': pageid
    }

    response = requests.get(url=URL, params=PARAMS).json()
    page = response['query']['pages'][str(pageid)]
    content = page['extract']

    return content

def write_file(*file_list):
    file_list = list(file_list)
    for i in file_list:
        try:
            pageid = i.split(" ")[0]
            page_content = get_page_content(pageid).split(". ")
            with open("/home/manh/PycharmProjects/pythonProject/ACSLinkPaper/crawl/" + pageid + ".txt", 'a', encoding='utf-8') as file:
                for j in page_content:
                    j += "."
                    j = re.sub(r'\n+', '\n', j.strip())
                    if len(j) == 0:
                        continue

                    if ("xem thêm" in j.lower()) or ("chú thích" in j.lower()) or ("tham khảo" in j.lower()):
                        break

                    file.write(j + "\n")

            print(i.strip())
        except:
            continue

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=PROCESSES)
    pool_outputs = pool.starmap(write_file, [(file_read[0:783]),
                                               (file_read[783:1566]),
                                               (file_read[1566:2349]),
                                               (file_read[2349:3132]),
                                               (file_read[3132:3915]),
                                               (file_read[3915:4698]),
                                               (file_read[4698:5481]),
                                               (file_read[5481:6264]),
                                               (file_read[6264:7074]),
                                               (file_read[7074:7830]),
                                               (file_read[7830:8613]),
                                               (file_read[8613:])])

    pool.close()
    pool.join()