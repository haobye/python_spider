'''
t=0.1
a=2
v=0


#第一段位移：
v0=v
s0=v0*t+0.5*a*(t**2)

#第二段位移：
v1=v0+a*t
s1=v1*t+0.5*a*(t**2)

#第三段位移：
v2=v1+a*t
s2=v2*t+0.5*a*(t**2)

'''

def get_tracks(distance):
    t = 0.2
    v = 0
    mid=distance*3/5
    tracks=[]

    current=0
    while current < distance:
        if current < mid:
            a=2
        else:
            a=-3
        v0 = v
        s = v0 * t + 0.5 * a * (t ** 2)
        current+=s
        v=v0+a*t
        # print(round(s))

        tracks.append(round(s))
    return tracks

print(get_tracks(165))






