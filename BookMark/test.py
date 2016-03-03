import BookMark.AbstractTask as Ab
import BookMark.Book as Book
import datetime


def test_for_Book():
    bk = Book.Book(_name="c")
    a = datetime.datetime.today()
    a = bk.getSpecificTime(bk.timeFormatting, a)
    print a
    pass

if __name__ == '__main__':
    test_for_Book()