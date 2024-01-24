breg1, breg2 = (
    [
        [60, 50, 40, 30, 20],
        [40, 50, 60, 73, 80],
        [10, 20, 30, 40, 50],
    ],
    [
        [30, 40, 50, 60, 70],
        [40, 60, 30, 20, 40],
        [10, 20, 90, 40, 50],
    ],
)
 
def prva (x, y):
    return x

def bacek (b1, b2):
    n = len(b1)
    m = len(b1[0])
    poti = []
    def aux (v, s, b, e, pot):
        if (v,s,b) == (n-1, m-1, 2):
            poti.append((e, pot))
        elif (v, s, b) == (0, m-1, 1):
            p = pot.copy()
            p.append("R")
            aux (0, 0, 2, e-10+b2[0][0], p)
        elif b == 1:
            if v > 1 and s > 1 and e>11 :
                p = pot.copy()
                p.append("U")
                aux (v-2, s-1, b, e-12+b1[v-2][s-1], p)
            if v > 0 and e>13 :
                p = pot.copy()
                p.append("X")
                aux (v-1, s, b, e-14+b1[v-1][s], p)
            if s < m-1 and e>9 :
                p = pot.copy()
                p.append("R")
                aux (v, s+1, b, e-10+b1[v][s+1], p)
        elif b == 2:
            if v < n-2 and s > 1 and e>11 :
                p = pot.copy()
                p.append("D")
                aux (v+2, s-1, b, e-12+b2[v+2][s-1], p)
            if v < n-1 and e>13 :
                p = pot.copy()
                p.append("X")
                aux (v+1, s, b, e-14+b2[v+1][s], p)
            if s < m-1 and e>9 :
                p = pot.copy()
                p.append("R")
                aux (v, s+1, b, e-10+b2[v][s+1], p)
    aux(n-1, 0, 1, b1[n-1][0], [])
    #return poti
    return max(poti, key = lambda x: x[0], default = "None")
            
