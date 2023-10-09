from time import sleep
class Clock:
    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss
        
    def run(self):
        while True:
            self.ss += 1
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
            if self.hh == 24:
                self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
            sleep(1)
        
        
    def setTime(self, h, m, s):
        self.hh = h
        self.mm = m 
        self.ss = s
        
        
class AlarmClock(Clock):
    def __init__(self, hh, mm, ss, alarm_on_off):
        super().__init__(hh, mm, ss)
        self.alarm_hh = hh
        self.alarm_mm = mm
        self.alarm_ss = ss
        self.alarm_on_off =  alarm_on_off
        
    def setAlarmTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s
        
    def alarm_on(self):
        self.alarm_on_off = True
    
    def alarm_off(self): 
        self.alarm_on_off = False
    
    def run(self):
        while self.alarm_on_off == True:
            self.ss += 1
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
            if self.hh == 24:
                self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
            
            if self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
                print("Time's up!")
                self.alarm_off()

            sleep(1)
            
         
        
    
# x = Clock(20,50,49)
# x.setTime(20,59,49)
# x.run()
x = AlarmClock(20,50,49, True)
x.setTime(20,59,49)
x.setAlarmTime(21,0,0)
# x.alarm_off()
x.alarm_on()
x.run()
        