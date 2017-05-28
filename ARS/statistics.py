# -*- coding: utf8 -*-
from collections import Counter
import uniout


def switch(argument):
    # ------------Hobbies-------------
    return {
        'Local business': '本地商家',
        'Community': '社群',
        'Government organization': '政府機關',
        'Product/service': '產品／服務',
        'Doctor': '博士',
        'Movie theater': '電影院',
        'Internet/software': '網路／軟體',
        'Food/grocery': '食品／雜貨',
        'Shopping/retail': '購物／零售',
        'Restaurant/cafe': '餐廳／咖啡店',
        'Website': '網站',
        'Games/toys': '遊戲/玩具',
        'Food/beverages': '食品／飲料',
        'Tv network': '電視節目',
        'App page': '應用程式專頁',
        'Hotel': '旅遊／休閒',
        'Insurance company': '保險公司',
        'Computers/internet website': '電腦／互聯網網站',
        'Electronics': '電子產品',
        'Computers/technology': '電腦／科技',
        'Health/beauty': '健康／美容',
        'Clothing': '服飾',
        'Tours/sightseeing': '旅遊／觀光',
        'News/media website': '新聞／媒體網站',
        'Music video': '音樂影片',
        'Video game': '電玩遊戲',
        'Non-profit organization': '非營利組織',
        'Athlete': '運動員',
        'Public figure': '公眾人物',
        'Fictional character': '虛構人物',
        'Travel/leisure': '旅遊／休閒',
        'Automobiles and parts': '汽車',
        'Cars': '汽車',
        'Automotive': '汽車',
        'Artist': '藝術家',
        'Personal blog': '部落客',
        'Book': '書籍',
        'Publisher': '出版社',
        'Media/news/publishing': '出版社',
        'Jewelry/watches': '珠寶/手錶',
        'Software': '軟體',
        'Professional services': '書籍',
        'Hospital/clinic': '醫院／診所',
        'Pet supplies': '寵物',
        'Movie': '電影',
        'Computers': '電腦／科技',
        'University': '學院與大學',
        'Musician/band': '音樂家／樂團',
        'Farming/agriculture': '養殖／農業',
        'Baby goods/kids goods': '嬰兒用品／兒童用品',
        'Retail and consumer merchandise': '購物／零售',
        'Landmark': '地標',
        'Photographer': '攝影師',
        'Magazine': '雜誌',
        'Actor/Director': '演員/導演',
        'Furniture': '傢俱',
        'Outdoor gear/sporting goods': '戶外用品/體育用品',
        'Home decor': '傢俱',
        'Designer': '設計師',
    }.get(argument, argument)


def statistic(a):
    list_counts = Counter(a)
    top = list_counts.most_common(1)
    s = switch(top[0][0])
    return s


def run(likes):
    H = [[], []]
    list_ = []
    n = likes[0][0]
    for i in range(len(likes)):
        list_.append(likes[i][3])
        if i < len(likes)-1:
            if likes[i+1][0] != n:
                H[0].append(n)
                H[1].append(statistic(list_))
                n = likes[i+1][0]
                list_[:] = []
    # H is an 2 * n array, n is the amount of id
    return H

