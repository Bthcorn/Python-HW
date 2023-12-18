class Clock():
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
    
    def setTime(self, Newh, Newm, News):
        if News >= 60:
            Newm += News // 60
            self.s = News % 60
        else:
            self.s = News

        if Newm >= 60:
            Newh += Newm // 60
            self.m = Newm % 60
        else:
            self.m = Newm
        
        if Newh >= 24: 
            self.h = Newh % 24
        else:
            self.h = Newh

    def getTime(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"
    
    def tick(self):
        self.s += 1
        if self.s >= 60:
            self.s = 0
            self.m += 1
            if self.m >= 60:
                self.m = 0
                self.h += 1
                if self.h >= 24:
                    self.h = 0
        
    def displayTime(self):
        if self.h >= 12:
            print(f"{self.h-12:02d}:{self.m:02d}:{self.s:02d} PM")
        else:
            print(f"{self.h:02d}:{self.m:02d}:{self.s:02d} AM")
            
time = Clock()
time.setTime(25,45,62)
time.getTime()
time.displayTime()
time.tick()
time.displayTime()

