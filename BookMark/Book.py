# -*- coding:utf-8 -*-
import BookMark.AbstractTask as Ab
import datetime

class Book(Ab.AbstractTask):
    """
    :type name:              -*- "str"      -*-         Book name
    :type author:            -*- [str,]     -*-         Author's name
    :type startDate:         -*- datetime   -*-         The time start to read
    :type publishingCompany: -*- "str"      -*-         Publishing company
    :type page:              -*- int        -*-         Total pages of the book
    :type readRecord:        -*- {str:int}  -*-         str come from timeFormatting(datetime)
    """

# ====================== __init__ Start ========================
    def __init__(self,
                 _name,
                 _author=None,
                 _start_date=datetime.datetime.today(),
                 _publishing_company=None,
                 _page=0
                 ):
        Ab.AbstractTask.__init__(self, _name)
        self.name = '《'+_name+'》'
        self.author = _author
        self.startDate = _start_date
        self.publishingCompany = _publishing_company
        self.page = _page
        self.readRecord = {}
        pass

# ===================== __init__ End ===========================

    # def getReadRecord(self):
    #     """
    #     Get record from database
    #     :type all_read_record: -*- {datetime : int}
    #     :r
    #     """

# ===================== Time Process Start============================
    @staticmethod
    def getSpecificTime(transfunc, *datetimes):
        trans = []
        for eachdate in datetimes:
            trans.append(transfunc(eachdate))
        return trans


    @staticmethod
    def timeFormatting(dateToFormatting):
        """
        :param dateToFormatting: datetime
        :return date_str: str as "yyyy/mm/dd"
        """
        date_str = str(dateToFormatting.year)+'/'+str(dateToFormatting.month)+'/'+str(dateToFormatting.day)
        return date_str
# ===================== Time Process End============================

# ===================== Updater - Start ========================

    def updateBookName(self, new_name):
        if new_name:
            self.name = new_name

    def updateBookAuthor(self, new_author_name):
        if new_author_name:
            self.name = new_author_name

    def updateBookStartDate(self, new_start_date):
        if new_start_date:
            self.startDate = new_start_date

    def updateBookPublishingCompany(self, new_publisher):
        if new_publisher:
            self.startDate = new_publisher

    def updateBookTotalPage(self, new_total_page):
        if new_total_page:
            self.startDate = new_total_page

    def updateBookReadRecord(self, day_record):
        """ :type day_record:   -*- day_record is a pair as key-value ( datetime :int ) """
        addRecord = self.timeFormatting(day_record[0])
        addPage = day_record[1]

        if addRecord in self.readRecord:
            self.readRecord[addRecord] += addPage
        else:
            self.readRecord[addRecord] = addPage

# ==================== Updater - End ==============================

    def printMessage(self):
        # print self.__name__
        print "self.__class__:", self.__class__
        print "self.__doc__:", self.__doc__
        print "self.__module__:", self.__module__
        print "self.__dict__:", self.__dict__
        print self.name
        print self.startDate
        print self.page
        print self.publishingCompany


def test():
    newBook = Book(_name="膜法师的自我修养")
    newBook.updateBookAuthor("西方记者")
    newBook.updateBookPublishingCompany("续命公社")
    newBook.printMessage()

if __name__ == '__main__':
    test()

