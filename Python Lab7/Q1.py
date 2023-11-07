class Time():
    def __init__(self, h=0, m=0, s=0):
        if not (0 <= h < 24):
            raise ValueError("Invalid hour value. Hour must be between 0 and 23.")
        if not (0 <= m < 60):
            raise ValueError("Invalid minute value. Minute must be between 0 and 59.")
        if not (0 <= s < 60):
            raise ValueError("Invalid second value. Second must be between 0 and 59.")
        
        self.h = h
        self.m = m
        self.s = s
    
    def print_out(self):
        if 0 <= self.h <= 24 and 0 <= self.m <= 60 and 0 <= self.m <=60:
            print(f"{self.h:02d}:{self.m:02d}:{self.s:02d} Hrs.")
        else:
            print("Please input the correct values.")

time1 = Time(9, -1, 0)
time1.print_out()