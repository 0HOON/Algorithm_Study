def time2int(hhmm):
    return int(hhmm[0:2])*60 + int(hhmm[3:])

def make_room(book_time):
    i = 0
    end_time = time2int(book_time[0][1])
    del book_time[0]
    while i < len(book_time):
        if (time2int(book_time[i][0]) - end_time) >= 10 :
            end_time = time2int(book_time[i][1])
            del book_time[i]
        else:
            i += 1

def solution(book_time):
    book_time = sorted(book_time)
    answer = 0
    
    while len(book_time) > 0:
        make_room(book_time)
        answer += 1

    return answer