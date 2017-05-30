# -*- coding: utf8 -*-


def is_hobby(arg):
    return {

        # merge the hobbies
        '電影院': '電影',
        '電影': '電影',
        '演員/導演': '電影',
        '喜劇演員': '電影',
        '電影工作室': '電影',
        '演員': '電影',

        '食品／雜貨': '食品',
        '食品／飲料': '食品',
        '餐廳／咖啡店': '食品',
        '廚房/烹飪': '食品',
        '食品及飲料公司': '食品',
        '餐廳': '食品',
        '糖果店': '食品',
        '葡萄酒／烈酒': '食品',

        '購物／零售': '購物',
        '產品／服務': '購物',
        '珠寶/手錶': '購物',
        '零售和消費商品': '購物',
        '零售公司': '購物',
        '購物與零售': '購物',
        '雜貨店': '購物',

        '電視節目': '娛樂',
        '電視頻道': '娛樂',
        '體育／娛樂／活動': '娛樂',
        '娛樂網站': '娛樂',
        '藝人': '娛樂',

        '遊戲/玩具': '電玩',
        '應用程式專頁': '電玩',
        '電玩遊戲': '電玩',

        '媒體／新聞機構': '媒體／新聞',
        '媒體／新聞／出版': '媒體／新聞',
        '新聞／媒體網站': '媒體／新聞',
        '媒體/新聞/出版': '媒體／新聞',
        '廣播與媒體製作公司': '媒體／新聞',

        '部落客': '社群',
        '個人部落格': '社群',
        '社交／文化網站': '社群',
        '社區': '社群',
        '個人網站': '社群',

        '旅遊／休閒': '旅遊／休閒',
        '旅遊／觀光': '旅遊／休閒',
        '戶外用品/體育用品': '旅遊／休閒',
        '運動員': '旅遊／休閒',
        '活動策劃／活動服務': '旅遊／休閒',
        '體育賽事': '旅遊／休閒',
        '運動隊伍': '旅遊／休閒',
        '旅行社': '旅遊／休閒',
        '休閒和健身': '旅遊／休閒',
        '地標和名勝古蹟': '旅遊／休閒',
        '地標': '旅遊／休閒',
        '城市': '旅遊／休閒',
        '本地／旅遊網站': '旅遊／休閒',
        '運動／健身中心': '旅遊／休閒',
        '航空': '旅遊／休閒',
        '戶外及運動用品公司': '旅遊／休閒',
        '體育場館與體育場': '旅遊／休閒',
        '國家公園': '旅遊／休閒',

        '電腦／互聯網網站': '電腦電子產品',
        '電子產品': '電腦／電子產品',
        '電腦／科技': '電腦／電子產品',
        '網路／軟體': '電腦／電子產品',
        '電信': '電腦／電子產品',
        '軟體': '電腦／電子產品',
        '網站': '電腦／電子產品',
        '手機／平板電腦': '電腦／電子產品',

        '音樂影片': '音樂',
        '音樂家／樂團': '音樂',
        '巡迴演唱會': '音樂',

        '舞者': '設計／藝術',
        '藝術家': '設計／藝術',
        '設計師': '設計／藝術',
        '藝術 / 娛樂 / 夜生活': '設計／藝術',
        '藝術／人文網站': '設計／藝術',
        '時尚': '設計／藝術',
        '藝術與娛樂': '設計／藝術',

        '書籍': '書籍',
        '作家': '書籍',
        '出版社': '書籍',
        '雜誌': '書籍',
        '作者': '書籍',
        '書籍系列': '書籍',

        '傢俱': '傢俱',
        '居家裝飾': '傢俱',
        '家居／庭園網站': '傢俱',
        '家庭用品': '傢俱',

        '服飾': '服飾',
        '手提袋／行李箱': '服飾',
        '服裝（品牌）': '服飾',
        '服飾公司': '服飾',
        '品牌': '服飾',
        '女性服飾店': '服飾',

        '水療 / 美容 / 個人護理': '健康／美容',
        '健康／美容': '健康／美容',
        '美容': '健康／美容',
        '美容、美妝與個人護理': '健康／美容',
        '健康/醫療/製藥': '健康／美容',
        '製藥': '健康／美容',
        '藥物': '健康／美容',

        '汽車': '汽車',
        '汽車及零件': '汽車',

        '金融公司': '金融',
        '銀行／金融機構': '金融',

        '保險公司': '保險公司',
        '寵物': '寵物',
        '養殖／農業': '養殖／農業',
        '嬰兒用品／兒童用品': '嬰兒用品／兒童用品',
        '攝影師': '攝影師',

        # not supposed to be a hobby, named 'not_a_hobby'
        '醫院／診所': 'not_a_hobby',
        '專業服務': 'not_a_hobby',
        '公眾人物': 'not_a_hobby',
        '政治人物': 'not_a_hobby',
        '非營利組織': 'not_a_hobby',
        '學院與大學': 'not_a_hobby',
        '本地商家': 'not_a_hobby',
        '公司': 'not_a_hobby',
        '政府機關': 'not_a_hobby',
        '政府機構': 'not_a_hobby',
        '虛構人物': 'not_a_hobby',
        '教堂/宗教組織': 'not_a_hobby',
        'OTHER': 'not_a_hobby',
        '純屬好玩': 'not_a_hobby',
        '組織': 'not_a_hobby',
        '宗教組織': 'not_a_hobby',
        '教育': 'not_a_hobby',
        '社區組織': 'not_a_hobby',
        '非政府組織（NGO）': 'not_a_hobby',
        '法治／法律': 'not_a_hobby',
        '感興趣': 'not_a_hobby',
        'Interest': 'not_a_hobby',

    }.get(arg, arg)
