def time24To12hour(time) :
    time_list = time.split(":")
    con_to_num = []
    con_to_str = []
    for i in time_list:
        con_to_num.append(int(i))
    # con_to_num
    
    if con_to_num[0] > 12:
        con_to_num[0] -= 12
        for j in con_to_num:
            con_to_str.append(str(j))
        new_time = ":".join(con_to_str)
        print(f"\"{new_time} PM\"")
    else:
        for j in con_to_num:
            con_to_str.append(str(j))
        new_time = ":".join(con_to_str)
        print(f"\"{new_time} AM\"")

time24To12hour("23:24")
time24To12hour("6:30")