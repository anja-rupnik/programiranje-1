from functools import lru_cache
# =============================================================================
# Najdaljše naraščajoče podzaporedje
# =============================================================================

# -----------------------------------------------------------------------------
# Napišite funkcijo `najdaljse_narascajoce_podazporedje`, ki sprejme seznam in
# poišče najdaljše (ne strogo) naraščajoce podzaporedje števil v seznamu.
#
# Primer: v seznamu `[2, 3, 6, 8, 4, 4, 6, 7, 12, 8, 9]` kot rezultat vrne
# podzaporedje `[2, 3, 4, 4, 6, 7, 8, 9]`.
# -----------------------------------------------------------------------------
def najdaljse_narascajoce_podazporedje(sez):
    @lru_cache
    def aux(z, i):
        if len(sez) == i:
            return 0
        elif sez[i]>= z:
            return max(aux(z, i+1), 1+aux(sez[i], i+1))
        else:
            return aux(z, i+1)
    return aux(float("-inf"), 0)
    
s1 = [2,0,0]    
s2 = [0,0,0]
s3 = [float("-inf"), 1, float("-inf"), 6]
s4 = []

def najdaljse_narascajoce_podazporedje(sez):
    @lru_cache
    def aux(z, i):
        if len(sez) == i:
            return []
        elif sez[i]>= z:
            a = [sez[i]] + aux(sez[i], i+1)
            b = aux(z, i+1)
            if len(a)<len(b):
                return b
            else:
                return a          
        else:
            return aux(z, i+1)
    return aux(float("-inf"), 0)
# -----------------------------------------------------------------------------
# Rešitev sedaj popravite tako, da funkcija `vsa_najdaljsa` vrne seznam vseh
# najdaljših naraščajočih podzaporedij.
# -----------------------------------------------------------------------------
def najdaljse_narascajoce_podazporedje(sez):
    @lru_cache
    def aux(z, i):
        if len(sez) == i:
            return [[]]
        elif sez[i]>= z:
            a = []
            for j in aux(sez[i], i+1):
                a.append([sez[i]]+j)
            b = aux(z, i+1)
            if len(a[0])<len(b[0]):
                return b
            else:
                return a          
        else:
            return aux(z, i+1)
    return aux(float("-inf"), 0)


# =============================================================================
# Žabica
# =============================================================================
# Žabica se je izgubila v močvari in želi kar se da hitro odskakljati ven. Na
# srečo močvara vsebuje veliko muh, s katerimi si lahko povrne energijo, kajti
# utrujena žabica ne skoči daleč.
# 
# S funkcijo `zabica(mocvara)` želimo ugotoviti, kako hitro lahko žabica
# odskaklja iz močvare. Močvaro predstavimo s tabelo, kjer žabica prične na
# ničtem polju. Če je močvara dolžine `k`, je cilj žabice priskakljati vsaj na
# `k`-to polje ali dlje (torej prvo polje, ki ni več vsebovano v tabeli).
# 
# Energičnost žabice predstavimo z dolžino najdaljšega možnega skoka. Torej
# lahko žabica z količino energije `e` skoči naprej za katerokoli razdaljo med
# `1` in `e`, in če skoči naprej za `k` mest ima sedaj zgolj `e - k` energije.
# Na vsakem polju močvare prav tako označimo, koliko energije si žabica povrne,
# ko pristane na polju. Tako se včasih žabici splača skočiti manj daleč, da
# pristane na polju z več muhami. Predpostavimo, da ima vsako polje vrednost
# vsaj `1`, da lahko žabica v vsakem primeru skoči naprej.
# 
# V primeru `[2, 4, 1, 2, 1, 3, 1, 1, 5]` lahko žabica odskaklja iz močvare v
# treh skokih, v močvari `[4, 1, 8, 2, 11, 1, 1, 1, 1, 1]` pa potrebuje zgolj
# dva.
# =============================================================================
# ne dela!!!
def zabica(mocvara):
    def aux(e, i):
        if len(mocvara) <= i:
            return 0
        elif e <0:
            return float("inf")
        else:
            return  min(1+aux(e-1+mocvara[i],i+1), aux(e-1, i+1))
    return aux(0, 0)

m1 = [2, 4, 1, 2, 1, 3, 1, 1, 5]
m2 = [4, 1, 8, 2, 11, 1, 1, 1, 1, 1]


# =============================================================================
# Nageljni
# =============================================================================
# Mama Franca želijo na balkon širine `n` postaviti `m` korit z nageljni širine
# `l` (korit, ne nageljnov). Zaradi lažjega zalivanja mora biti med dvema
# koritoma vsaj za 1 enoto prostora. Mama Franca želijo postaviti vsa korita,
# jih pa zaradi slabega vida med seboj ne razlikujejo. 
# 
# Vnuk je že spisal program, ki poišče število možnih postavitev, ne zna pa
# vrniti rešitev. Napišite funkcijo `nageljni(n, m, l)`, ki vrne seznam vseh
# možnih postavitev, da se bodo mama Franca lažje odločili.
# 
# Primer vseh štirih možnih postavitev pri balkonu širine 9 s tremi koriti
# širine 2 (kjer z 1 označimo nagelj in z 0 prazen prostor):
# 
#     [1, 1, 0, 1, 1, 0, 1, 1, 0]
#     [1, 1, 0, 1, 1, 0, 0, 1, 1]
#     [1, 1, 0, 0, 1, 1, 0, 1, 1]
#     [0, 1, 1, 0, 1, 1, 0, 1, 1]
# =============================================================================
def nageljni(n, m, l):
    vrni = []
    def aux(n, m, sez):
        if m == 0:
            for i in range(n):
                sez.append(0)
            vrni.append(sez)
        elif n == l and m == 1:
            for i in range(l):
                sez.append(1)
            vrni.append(sez)    
        elif n >= m*l + m-1:
            a = sez.copy()
            b = sez.copy()
            b.append(0)
            for i in range(l):
                a.append(1)
            a.append(0)
            aux(n-1, m, b)
            aux(n-l-1, m-1, a)
        
    aux(n, m, [])
    return vrni  


# =============================================================================
# Pobeg iz Finske
# =============================================================================
# Vaš sošolec Mortimer se je med potovanjem po Finski spravil v krepko godljo.
# Po divjem poskušanju lokalne vodke se je namreč stepel s kravo, zaradi česar
# ga sedaj lovi finska govedorejska mafija. Na srečo so za njegovo hrabro bitko
# slišale vse rokovske in metalske skupine, ki so mu pripravljene ponuditi
# prevoz.
# 
# Ker je Mortimer pridno poslušal predavanja iz finančne matematike, med potjo
# uspe prislužiti nekaj denarja, s katerim bo lahko plačal prevoz. Finci,
# navdušeni nad Mortimerjevim pogumom, mu dovolijo, da se med potjo zadolži,
# dokler na koncu pobega vse stroške povrne.
# 
# Mesta na poti predstavimo kot seznam, katerega elementi so seznami vseh
# možnih nadaljnjih poti. Pot je par `(indeks_cilja, denar)`. Kot primer
# 
#     [[(1, 10), (3, -10)],    # 0 
#     [(2, 10), (5, -20)],     # 1
#     [(3, -10)],              # 2 
#     [(4, 15)],               # 3 
#     [(5, 0)]]                # 4 
# 
# pomeni, da lahko v mestu 1 Mortimer izbere med prevozom v mesto 2, kjer
# dodatno zasluži 10 evrov, ali pa prevoz v mesto 5, ki ga stane 20 evrov. Ker
# beži pred mafijo, lahko predpostavite, da bodo možne zgolj poti na mesta z
# višji indeksom (torej ni ciklov).
# 
# Pobeg je uspešen, čim lahko odpotuje v mesto, ki ni več na seznamu (torej
# skok na indeks, ki preseže seznam) in ima po koncu zadnjega skoka 0 ali več
# evrov. Napišite program, ki nam vrne pot z najmanjšim številom skokov,
# predstavljeno kot seznam indeksov mest na poti. Ker pobeg morda ni možen, naj
# v tem primeru funkcija vrne `None`.
# 
# Na primeru je optimalna pot `[0, 3, 4, 5]`, kjer se Mortimer sicer zadolži,
# vendar v skoku iz 3 v 4 zasluži dovolj, da konča z 5 evri. Hitrejša pot bi
# bila `[0, 1, 5]`, vendar v tem primeru Mortimer na koncu dolguje še 10 evrov.
# 
# Mortimer pot vedno začne v mestu z indeksom 0 in ima 0 evrov (saj je vse
# zapil). Funkcija `pobeg` sprejme seznam, ki predstavlja finska mesta in vrne
# seznam indeksov mest, v katerih se Mortimer ustavi.
# =============================================================================
def pobeg(sez):
    ok_poti = []
    
    def aux(pot, denar):
        mesto = pot[-1]
        if mesto > len(sez)-1:
            if denar >= 0:
                ok_poti.append(pot)
        else:
            for (m, c) in sez[mesto]:
                if m > mesto:
                    p = pot.copy()
                    p.append(m)
                    aux(p, denar + c)
    aux([0], 0)
    
    return min(ok_poti, key = len, default = "None")
    
    
p1 = [[(1, 10), (3, -10)],[(2, 10), (5, -20)],[(3, -10)],[(4, 15)],[(5, 0)]] 
p2 = [[(3, -11), (0, 3)], [(1, 1)], [(0, 4)], [(2, -4)]]



# =============================================================================
# Pričetek robotske vstaje
# =============================================================================
# Nepreviden študent je pustil robotka z umetno inteligenco nenadzorovanega.
# Robotek želi pobegniti iz laboratorija, ki ga ima v pomnilniku
# predstavljenega kot matriko števil:
# 
#   - ničla predstavlja prosto pot
#   - enica predstavlja izhod iz laboratorija
#   - katerikoli drugi znak označuje oviro, na katero robotek ne more zaplejati
# 
# Robotek se lahko premika le gor, dol, levo in desno ter ima omejeno količino
# goriva. V zbirki programov že ima funkcijo `moznost_pobega(soba, vrsta,
# stolpec, koraki)`, ki pove ali je pobeg možen.
# 
# Napišite funkcijo `pot_pobega(soba, vrsta, stolpec, koraki)`, ki sprejme
# matriko sobe, začetno pozicijo in število korakov ter izračuna pot po kateri
# robotek pobegne (če to ni možno vrne `None`). Pot zakodiramo s seznamom
# ukazov `'gor'`, `'dol'`, `'levo'` in `'desno'`.
# 
# Na primer za laboratorij:
# 
#     [[0, 1, 0, 0, 2],
#      [0, 2, 2, 0, 0],
#      [0, 0, 2, 2, 0],
#      [2, 0, 0, 2, 0],
#      [0, 2, 2, 0, 0],
#      [0, 0, 0, 2, 2]]
# 
# robotek iz vrste 3 in stolpca 1 pri vsaj petih korakih pobegne z ukazi
# 
#      ['gor', 'levo', 'gor', 'gor', 'desno']
# 
# medtem ko iz vrste 5 in stolpca 0 ne more pobegniti.
# =============================================================================
def pot_pobega(soba, vrsta, stolpec, koraki):
    vrni = []
    def aux (pot, gorivo, v, s):
        if soba[v][s] == 1:
            vrni.append(pot)
        elif gorivo > 0 and soba[v][s] == 0:
            if v> 0:
                a = pot.copy()
                a.append("gor")
                aux(a, gorivo -1, v-1, s)
            if s> 0:
                a = pot.copy()
                a.append("levo")
                aux(a, gorivo -1, v, s-1)
            if v< len(soba)-1:
                a = pot.copy()
                a.append("dol")
                aux(a, gorivo -1, v+1, s)
            if s< len(soba[0])-1:
                a = pot.copy()
                a.append("desno")
                aux(a, gorivo -1, v, s+1)
    aux ([], koraki, vrsta, stolpec)
    if vrni == []:
        return "None"
    return vrni

ma1 = [[0, 1, 0, 0, 2],[0, 2, 2, 0, 0],[0, 0, 2, 2, 0],[2, 0, 0, 2, 0],[0, 2, 2, 0, 0],[0, 0, 0, 2, 2]]
ma2 = [[0, 1, 0, 0, 2],[0, 2, 2, 0, 0],[0, 0, 2, 2, 0],[2, 0, 0, 0, 0],[0, 2, 2, 0, 0],[0, 0, 0, 2, 2]]
