class Book:

    def __init__(self, name, author, comment, state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)


class BookManager:

    books = []

    def __init__(self):
        book1 = Book('惶然录', '费尔南多·佩索阿',
                     '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book(
            '以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯',
                     '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
        book4 = Book('撒哈拉的故事', '三毛', '我每想你一次，天上便落下一粒沙，从此便有了撒哈拉。')
        book5 = Book('梦里花落知多少', '三毛', '人人都曾拥有荷西，虽然他终会离去。')
        book6 = Book('月亮与六便士', '毛姆', '满地都是六便士，他却抬头看见了月亮。')
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)
        self.books.append(book4)
        self.books.append(book5)
        self.books.append(book6)

    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.根据作者查询\n6.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                self.show_author_book()
            elif choice == 6:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海中相遇。')
                break

    def show_all_book(self):
        for book in self.books:
            print(book)
            print('')

    def add_book(self):
        new_name = input('请输入书籍名称：')
        new_author = input('请输入作者名称：')
        new_comment = input('请输入书籍推荐语：')
        new_book = Book(new_name, new_author, new_comment)
        self.books.append(new_book)
        print('书籍录入成功！\n')

    def check_book(self, name):
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None

    def lend_book(self):
        name = input('请输入借阅书籍的名称：')
        res = self.check_book(name)

        if res != None:
            if res.state == 1:
                print('你来晚了一步，这本书已经被借走了噢')
            else:
                print('借阅成功，借了不看会变胖噢～')
                res.state = 1
        else:
            print('这本书暂时没有收录在系统里呢')

    def return_book(self):
        name = input('请输入归还书籍的名称：')
        res = self.check_book(name)

        if res != None:
            if res.state == 1:
                print('归还成功！你是个好嗨哦！')
                res.state = 0
            else:
                print('图书没有借出，请核对 ？')
        else:
            print('书名有误，请核对后再选择！')

    def show_author_book(self):
        author = input('你想找谁的书呢？')
        i = 0
        for book in self.books:
            if author == book.author:
                i += 1
                print(author + '收录书目如下：')
                print('第'+str(i)+'本书')
                print('*'*10)
                print(book.name)
                print(book.comment)
        if i == 0:
            print('很可惜，我们暂时没有收录这位作者的作品')


manager = BookManager()
manager.menu()
