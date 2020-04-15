    class Date:
        def __init__(self, day, month, year):
            self.day = day
            self.month = month
            self.year = year

        def __str__(self):
            return "{}/{}/{}".format(
                self.day,self.month,self.year)
        
        def resolveTask(self, date):
            if self.year < date.year:
                return 0
            if self.year == date.year:
                if self.month < date.month:
                    return 0 
                if self.month == date.month and\
                    self.day <= date.month:
                    return 0
            
            if self.month == date.month and\
                self.year == date.year:
                return 15 * (self.day - date.day)
            
            if self.year == date.year:
                return 500*(self.month - date.month)
            
            return 10000

    d = [x for x in map(int,input().split())]
    d1 = Date(d[0], d[1], d[2])

    d = [x for x in map(int,input().split())]
    d2 = Date(d[0], d[1], d[2])

    print(d1.resolveTask(d2))