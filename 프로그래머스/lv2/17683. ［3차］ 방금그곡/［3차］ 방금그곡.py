def str2min(string):
    h, m = string.split(':')
    return int(h)*60 + int(m)

def preprocess_tones(tones):
    res = []
    for t in tones:
        if t == '#':
            res[-1] += 1
        else:
            res.append(ord(t)*2)
    return res

def solution(m, musicinfos):
    answer = ''
    infos = []
    for i, mi in enumerate(musicinfos):
        start, end, name, tones = mi.split(',')
        start = str2min(start)
        end = str2min(end)
        duration = end-start
        tones = preprocess_tones(tones)
        tones = (tones*duration)[:duration]
        infos.append((i, name, tones))
        
    infos = sorted(infos, key=lambda x: (-len(x[2]), x[0]))
    m = preprocess_tones(m)
    
    for info in infos:
        _, name, tones = info
        for i in range(len(tones)-len(m)+1):
            if tones[i:i+len(m)] == m:
                return name
    return "(None)"