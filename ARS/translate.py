#!/usr/bin/python
# -*- coding: utf-8 -*-
import load_csv


# from Shuan66
def cat_trans(s):
    # ------------Hobbies-------------
    # Only list the meaningful hobbies, the remainder is regarded as unimportant and ignorable
    return {
        'Local business': '本地商家',
        'Local Business': '本地商家',
        'Community': '社群',
        'Government organization': '政府機關',
        'Government Organization': '政府機關',
        'Product/service': '產品／服務',
        'Product/Service': '產品／服務',
        'Author': '作家',
        'Movie theater': '電影院',
        'Movie Theater': '電影院',
        'Internet/software': '網路／軟體',
        'Internet/Software': '網路／軟體',
        'Food/grocery': '食品／雜貨',
        'Food/Grocery': '食品／雜貨',
        'Shopping/retail': '購物／零售',
        'Shopping/Retail': '購物／零售',
        'Restaurant/cafe': '餐廳／咖啡店',
        'Restaurant/Cafe': '餐廳／咖啡店',
        'Games/toys': '遊戲/玩具',
        'Games/Toys': '遊戲/玩具',
        'Food/beverages': '食品／飲料',
        'Food/Beverages': '食品／飲料',
        'Tv network': '電視節目',
        'App page': '應用程式專頁',
        'App Page': '應用程式專頁',
        'Hotel': '旅遊／休閒',
        'Insurance company': '保險公司',
        'Computers/internet website': '電腦／互聯網網站',
        'Computers/Internet website': '電腦／互聯網網站',
        'Electronics': '電子產品',
        'Computers/technology': '電腦／科技',
        'Computers/Technology': '電腦／科技',
        'Health/beauty': '健康／美容',
        'Health/Beauty': '健康／美容',
        'Clothing': '服飾',
        'Tours/sightseeing': '旅遊／觀光',
        'Tours/Sightseeing': '旅遊／觀光',
        'News/media website': '新聞／媒體網站',
        'News/Media website': '新聞／媒體網站',
        'Music video': '音樂影片',
        'Music Video': '音樂影片',
        'Video game': '電玩遊戲',
        'Video Game': '電玩遊戲',
        'Non-profit organization': '非營利組織',
        'Non-Profit Organization': '非營利組織',
        'Telecommunication': '電信',
        'Athlete': '運動員',
        'Public figure': '公眾人物',
        'Public Figure': '公眾人物',
        'Travel/leisure': '旅遊／休閒',
        'Local/travel website': '旅遊／休閒',
        'Local/Travel website': '旅遊／休閒',
        'Automobiles and parts': '汽車',
        'Cars': '汽車',
        'Automotive': '汽車',
        'Artist': '藝術家',
        'Personal blog': '部落客',
        'Personal Blog': '部落客',
        'Book': '書籍',
        'Publisher': '出版社',
        'Media/news/publishing': '媒體/新聞/出版',
        'Media/News/Publishing': '媒體/新聞/出版',
        'Jewelry/watches': '珠寶/手錶',
        'Jewelry/Watches': '珠寶/手錶',
        'Software': '軟體',
        'Professional services': '專業服務',
        'Entertainment website': '娛樂網站',
        'Entertainment Website': '娛樂網站',
        'Hospital/clinic': '醫院／診所',
        'Hospital/Clinic': '醫院／診所',
        'Pet supplies': '寵物',
        'Pet Supplies': '寵物',
        'Movie': '電影',
        'Computers': '電腦／科技',
        'University': '學院與大學',
        'Musician/band': '音樂家／樂團',
        'Musician/Band': '音樂家／樂團',
        'Farming/agriculture': '養殖／農業',
        'Farming/Agriculture': '養殖／農業',
        'Baby goods/kids goods': '嬰兒用品／兒童用品',
        'Baby Goods/Kids Goods': '嬰兒用品／兒童用品',
        'Retail and consumer merchandise': '購物／零售',
        'Landmark': '地標',
        'Actor/director': '演員/導演',
        'Actor/Director': '演員/導演',
        'Tv show': '電視節目',
        'Tv Show': '電視節目',
        'Photographer': '攝影師',
        'Magazine': '雜誌',
        'Furniture': '傢俱',
        'Outdoor gear/sporting goods': '戶外用品/體育用品',
        'Outdoor gear/Sporting goods': '戶外用品/體育用品',
        'Home decor': '傢俱',
        'Designer': '設計師'
    }.get(s, s)


# encode location
def loc_trans(s):
    return {
        "基隆市": 0,
        "台北市": 1,
        "新北市": 2,
        "新竹市": 3,
        "苗栗市": 4,
        "台中市": 5,
        "彰化市": 6,
        "雲林市": 7,
        "南投市": 8,
        "嘉義市": 9,
        "台南市": 10,
        "高雄市": 11,
        "屏東市": 12,
        "宜蘭市": 13,
        "花蓮市": 14,
        "台東市": 15
    }.get(s, 1)


def gender_trans(s):
    value = 0.5
    if s == "男性":
        value = 1
    elif s == "女性":
        value = 0

    return value


def age_trans(s):
    if not load_csv.pandas.isnull(s):
        int_arr = s.split("/")
        return 2017 - int(int_arr[0])
    else:
        return 30