f_in = open("courses_selenium.txt", "rt", encoding='utf-8')
FL = ["日文上", "日文下", "印尼文一", "韓文一", "韓文二", "泰文一", "泰文二", "泰文三", "越南文一", "越南文二", "法文一", "法文二",
      "德文一", "德文二", "西班牙文一", "西班牙文二", "俄文一", "俄文二", "義大利文一", "義大利文二", "葡萄牙文一", "土耳其文一",
      "土耳其文二", "日文一", "日文二"]
DEPARTMENTS = ['健統所', '心理系', '腫瘤醫學所', '植科產博學程', '積體電路碩士', '臨醫所醫研組', '海洋所物理組',
               '茶與茶業學程', '臺灣研究學程', '物理所', '學士後護', '事業經營碩士', '生物機電所', '工管系',
               '歐洲暨歐盟學', '農化系', '化學所化生組', '積體電路博士', '工管系企管組', '東亞學分學程', '農藝所',
               '圖資系', '經濟所', '分子科技學程', '數學所', '藝史所', '病理所', '臺文所', '工管系科管組',
               '植醫碩士學程', '農經所', '藝術設計學程', '應用物理所', '國企系', '生化科學所', '土木系',
               '動物福祉學分', '中草藥學程', '生科系', '園藝所作物組', '法醫所', '醫材影像所', '生理所',
               '分子細生所', '生多學程', '公事所', '商資分析學程', '生化分生所', '高分子所', '公衛系', '森林環資系',
               '建城所', '流預所', '工業工程所', '基因學位學程', '人類系', '生態演化所', '法律系司法組', '政治系',
               '智慧醫療學程', '毒理所', '建築設計學程', '牙醫所', '藥學系產研組', '創新學位學程', '領導學程', '植物科學所',
               '大氣所', '社工系', '社工所', '生科院院學士', '海洋所漁業組', '量子計算學程', '歷史系', '生技食營學程', '中文所',
               '生物科技管理', '口腔生物所', '華教碩士學程', '機械所', '工科海洋系', '經濟系', '醫學院', '物理系', '工學院',
               '翻譯碩士學程', '奈米工科博士', '資料科學學程', '自動化學程', '綠色精密學程', '圖資所', '醫技所', '事業法務碩士',
               '政治所', '海洋所地物理', '機械系', '保健營養學程', '政治系國關組', '解剖所', '資工所', '傳播學程', '海洋科學學程',
               '天文物理所', '戲劇所', '微生所', '法律系法學組', '生傳發展所', '全英工學士', '校學士', '園藝所產品組', '智醫健康資訊',
               '醫工系', '中文系國際生', '文學院', '地理系', '物治系', '元件材料博士', '統計碩士學位', '臨醫所試驗組', '法律院',
               '分子醫學學程', '醫學系', '植微系', '電資院', '國際企業所', '幹細胞學程', '精準健康博士', '免疫所', '土木所',
               '人口學程', '臨床藥學所', '漁業科學所', '醫衛共同課程', '化學系', '生工系', '動科系', '健康政策學程', '大氣系',
               '國發所', '能源科技學程', '創新設計學院', '政治系公行組', '傳染病學程', '食科所', '資訊管理所', '職治系', '分子醫學所',
               '土木所交通組', '醫技系', '森林環資所', '生科院', '植微所', '農化所', '農藝系', '歷史所', '牙醫系', '微生所微免組',
               '管理院', '統計所', '藥理所', '電子所', '日文系', '園藝系', '古典文學學程', '電機所', '大數據學程', '中英翻譯學程',
               '台大遠距教學', '土木所測量組', '心理所', '國家理論中心', '社科院', '地科學程', '分子比病所', '地科國際學程',
               '寫作教學中心', '法律系', '獸醫系', '數學系', '獸醫所', '社會系', '永續資源學程', '食安所', '\xa0', '食品科技學程',
               '生命教育學程', '材料所', '土木所結構組', '藥學系', '商研所', '環職所', '全衛碩士學程', '分子醫藥學程', '土木所大地組',
               '創業創新MB', '生技所', '人類所', '生物多樣性', '哲學所', '理學院', '工科海洋所', '會計系', '法律系財法組',
               '元件材料碩士', '化工系', '國際神經學程', '品牌顧客學程', '應力所', '會計所', '生技學程', '工學院院學士',
               '流預所生統組', '昆蟲所', '風電學程', '神經認知學程', '共教組', '財金所', '農經系', '地質系', '政治系政論組',
               '海洋所', '教育學程', '法律所', '地質所', '全衛博士學程', '語言所', '土木所CAE組', '化學所化學組', '轉譯博士學程',
               '婦女性別學程', '大陸研究學程', '課外活動組', '創意創業學程', '護理所', '腦與心智所', '戲劇系', '環工所', '護理系',
               '日本學程', '中文系', '智網國際學程', '微生所熱醫組', '化工所', '生資國際學程', '流預所預醫組', '園藝所', '土木所營管組',
               '材料系', '永續化學科技', '電機系', '農科基因體', '運動健康管理', '防災減害韌性', '醫工所', '物治所', '哲學系',
               '地理所', '臨醫所', '生工所', '外文系', '農藝所作物組', '生技系', '海洋所化學組', '資工系', '全電運輸學程',
               '國際運動事務', '藥物科技組', '社會所', '分子醫藥組', '氣候永續學位', '動科所', '生傳發展系', '音樂學所', '精準健康碩士',
               '昆蟲系', '生物統計學程', '企管碩士專班', '農藝所生統組', '科法所', '奈米科技學程', '應數所', '臨床動醫所',
               '知識管理學程', '光電所', '基蛋所', '醫教生倫所', '生科所', '生物科技所', '奈米工科碩士', '行社所', '老人長照學程',
               '公衛碩士學程', '生農院', '職治所', '流預所流病組', '經典人文學程', '亞洲藝術學程', '網媒所', '日文所', '電信所',
               '國際學程', '資管系', '健管所', '園藝所景觀組', '新聞所', '財金系', '生物機電系', '土木所水利組', '公衛院',
               '生醫電資所', '外文所', '藥學所']
WEEKDAY = "一二三四五六"
DAYS_DICT = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6}


FL_SET = set(FL)


class AvailableTime:
    def __init__(self):
        self.time = []
        self.date = ['一', '二', '三', '四', '五', '六']
        for i in range(6):
            self.time.append(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D'])

    def remove_time(self, date, time):  # ex. if it takes date= [一,三], time=[[1,2,3][1]], it will remove周一123 and 周三1
        for c, d in enumerate(date):
            for t in time[c]:
                self.time[DAYS_DICT[d]-1].remove(t)

    def __repr__(self):
        txt = ""
        for c, day in enumerate(self.date):
            txt += day
            txt += str(self.time[c])
        return txt


class CourseTime:
    def __init__(self, text):
        if text == " ":
            raise ValueError
        else:
            new_text = ''
            self.date = []
            self.time = []
            in_paren = False
            try:
                for char in text:
                    if not in_paren:
                        new_text += char
                    if char == '(':
                        in_paren = True
                        new_text = new_text[:-1]
                    elif char == ')':
                        in_paren = False
                new_text = new_text.replace(' ', '')
                new_text = new_text.replace(',', '')
                for char in new_text:
                    if char in WEEKDAY:
                        self.time.append([])
                        self.date.append(char)
                    else:
                        if char == "0":
                            self.time[-1].remove('1')
                            self.time[-1].append('10')
                        else:
                            self.time[-1].append(char)
            except Exception as e:
                raise ValueError
            
    def __repr__(self):
        txt = ""
        for c, day in enumerate(self.date):
            txt += day
            txt += str(self.time[c])
        return txt


class Course:
    def __init__(self, name, time, department, category, list_id, id, credit, site, professor, note):
        self.name = name
        try:
            self.time = CourseTime(time)
        except ValueError:
            self.time = None
        self.department = department
        self.category = category
        self.list_id = list_id
        self.id = id
        self.credit = credit
        self.site = site
        self.professor = professor
        self.note = note

    def __repr__(self):
        txt = f"{self.list_id} : {self.name}"
        return txt


class CourseList:
    def __init__(self, course_list):
        self.full = course_list
        self.temp_list = []

    def search(self, departments=None, categories=None, times=None):  # get a list of departments
        self.temp_list = []
        for c in self.full:
            temp_bool = True
            if departments is not None:
                if c.department not in departments:
                    temp_bool = False
            if times is not None:
                if type(c.time) is not CourseTime:
                    continue
                if not check_time(times, c.time):
                    temp_bool = False

            if categories is not None:
                for category in categories:
                    if category not in c.category:
                        temp_bool = False
                if "外文" in categories and "外文" in c.category:
                    temp_bool = True
                if "通識" in categories and "通識" in c.category:
                    temp_bool = True
                if "國文" in categories and "國文" in c.category:
                    temp_bool = True

            if temp_bool:
                self.temp_list.append(c)
        if not self.temp_list:
            return "無結果"
        return self.temp_list

    def __repr__(self):
        txt = f"Course List: currently {len(self.full)} courses"
        return txt

    def __getitem__(self, list_id):
        for c in self.full:
            if int(c.list_id) == list_id:
                return c
        return None


def check_time(ava_time, course_time):
    for c, d in enumerate(course_time.date):
        for t in course_time.time[c]:
            if t not in ava_time.time[DAYS_DICT[d]-1]:
                return False
    return True


all_courses = f_in.readlines()
course_list = []
all_category = {}
all_department = set()
for course in all_courses:
    course_slice = course.split('/')
    try:
        course_list.append(Course(name=course_slice[5][1:], time=course_slice[14], department=course_slice[2], category=[course_slice[11]], list_id=course_slice[0], id=course_slice[3],
                                  credit=course_slice[8], site=course_slice[6], professor=course_slice[12], note=course_slice[16] + '\n' + course_slice[17]))
        if "通識" in course_list[-1].note or course_list[-1].category == '\xa0':
            course_list[-1].category.append("通識")
        if "校際" in course_list[-1].note:
            course_list[-1].category.append("校際")
        if "大學國文" in course_list[-1].name:
            course_list[-1].category.append("國文")
        for fl in FL_SET:
            if fl in course_list[-1].name:
                course_list[-1].category.append("外文")
        if course_list[-1].department == " ":
            course_list[-1].category.append("共同")
        for c in course_list[-1].category:
            if c in all_category:
                all_category[c] += 1
            else:
                all_category[c] = 1
        all_department.add(course_slice[2])
    except IndexError:
        print(course_slice[0], "IndexError")
        continue

course_list = CourseList(course_list)
times = AvailableTime()
times.remove_time(["一", "三"], [["1", "2"], ["3", "4"]])
course_time = CourseTime("一3二34")
print(course_list.search(departments="外文系", times=times))
print(course_time)
print(check_time(times, course_time))
print(times.time)
print(times.date)
print(course_list[455].name, course_list[455].time, course_list[455].department, course_list[455].category,
      course_list[455].list_id, course_list[455].id, course_list[455].credit, course_list[455].site,
      course_list[455].professor, course_list[455].note)
print(all_category)
print(all_department)
