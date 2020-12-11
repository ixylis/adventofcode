inp="""77
58
25
92
14
154
105
112
147
63
84
109
24
129
49
102
130
128
134
88
95
70
80
4
153
17
145
122
39
117
93
65
3
2
139
101
148
37
27
1
87
64
23
59
42
146
43
151
116
46
115
118
131
94
19
33
12
107
10
7
73
78
53
11
135
79
60
32
141
31
140
98
136
72
38
152
30
74
106
50
13
26
155
67
20
66
91
56
34
125
52
51
18
108
57
81
119
71
144"""
inp1="""16
10
15
5
1
11
7
19
6
12
4"""
inp2="""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
inpa1 = inp.split("\n")
inpa = [int(x) for x in inpa1]
inpa = sorted(inpa)
memo = {}
dev = max(inpa)+3
def getArrangements(possibleSeq, curSeq):
    if dev-curSeq[-1]<=3:
        memo[tuple([curSeq[-1]]+possibleSeq)]=1
        return 1
    if not possibleSeq:
        return 0
    if tuple([curSeq[-1]]+possibleSeq) in memo.keys():
        return memo[tuple([curSeq[-1]]+possibleSeq)]
    c1 = getArrangements(possibleSeq[1::], curSeq+[possibleSeq[0]])
    if len(possibleSeq)<=1:
        c2 = 0
    elif possibleSeq[1]-curSeq[-1]<=3:
        c2 = getArrangements(possibleSeq[1::], curSeq)
    else:
        c2 = 0
    memo[tuple([curSeq[-1]]+possibleSeq)]=c1+c2
    return c1+c2
ans = getArrangements(inpa, [0])
print(ans)
