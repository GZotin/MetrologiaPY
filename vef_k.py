# Tabelas de correlação k e v_ef

# Insere o v_ef e retorna k
def k(vef: float):
    if vef >= 1 and vef < 2:
       return 13.97
    elif vef >= 2 and vef < 3:
        return 4.53
    elif vef == 3:
        return 3.31
    elif vef == 4:
        return 2.87
    elif vef == 5:
        return 2.65
    elif vef == 6:
        return 2.52
    elif vef == 7:
        return 2.43
    elif vef == 8:
        return 2.37
    elif vef == 10:
        return 2.28
    elif vef == 12:
        return 2.23
    elif vef == 14:
        return 2.20
    elif vef == 16:
        return 2.17
    elif vef == 18:
        return 2.15
    elif vef == 20:
        return 2.13
    elif vef == 25:
        return 2.11
    elif vef == 30:
        return 2.09
    elif vef == 35:
        return 2.07
    elif vef == 40:
        return 2.06
    elif vef == 45:
        return 2.06
    elif vef == 50:
        return 2.05
    elif vef == 60:
        return 2.04
    elif vef == 80:
        return 2.03
    elif vef == 100:
        return 2.02
    elif ((vef > 3) and (vef < 4)):
        return (((vef - 3)*(2.87 - 3.31))/(4 - 3)) + 3.31
    elif ((vef > 4) and (vef < 5)):
        return (((vef - 4)*(2.87 - 2.65))/(5 - 4)) + 2.87
    elif ((vef > 5) and (vef < 6)):
       return (((vef - 5)*(2.52 - 2.65))/(6 - 5)) + 2.65
    elif ((vef > 6) and (vef < 7)):
       return (((vef - 6)*(2.43 - 2.52))/(7 - 6)) + 2.52
    elif ((vef > 7) and (vef < 8)):
        return (((vef - 7)*(2.37 - 2.43))/(8 - 7)) + 2.43
    elif ((vef > 8) and (vef < 10)):
        return (((vef - 8)*(2.28 - 2.37))/(10 - 8)) + 2.37
    elif ((vef > 10) and (vef < 12)):
        return (((vef - 10)*(2.23 - 2.28))/(12 - 10)) + 2.28
    elif ((vef > 12) and (vef < 14)):
        return (((vef - 12)*(2.20 - 2.23))/(14 - 12)) + 2.23
    elif ((vef > 14) and (vef < 16)):
        return (((vef - 14)*(2.17 - 2.20))/(16 - 14)) + 2.20
    elif ((vef > 16) and (vef < 18)):
        return (((vef - 16)*(2.15 - 2.17))/(18 - 16)) + 2.17
    elif ((vef > 18) and (vef < 20)):
        return (((vef - 18)*(2.13 - 2.15))/(20 - 18)) + 2.15
    elif ((vef > 20) and (vef < 25)):
        return (((vef - 20)*(2.11 - 2.13))/(25 - 20)) + 2.13
    elif ((vef > 25) and (vef < 30)):
        return (((vef - 25)*(2.09 - 2.11))/(30 - 25)) + 2.11
    elif ((vef > 30) and (vef < 35)):
        return (((vef - 30)*(2.07 - 2.09))/(35 - 30)) + 2.09
    elif ((vef > 35) and (vef < 40)):
        return (((vef - 35)*(2.06 - 2.07))/(40 - 35)) + 2.07
    elif ((vef > 40) and (vef < 45)):
        return 2.06
    elif ((vef > 45) and (vef < 50)):
        return (((vef - 45)*(2.05 - 2.06))/(50 - 45)) + 2.06
    elif ((vef > 50) and (vef < 60)):
        return (((vef - 50)*(2.04 - 2.05))/(60 - 50)) + 2.05
    elif ((vef > 60) and (vef < 80)):
        return (((vef - 60)*(2.03 - 2.04))/(80 - 60)) + 2.04
    elif ((vef > 80) and (vef < 100)):
        return (((vef - 80)*(2.02 - 2.03))/(100 - 80)) + 2.03
    else:
        return 2.00
        
# Insere o k e retorna v_ef
def vef(k: float):
    
    if k > 4.53:
        return 1
    elif k > 3.31:
        return 2
    elif k > 2.87:
        return 3
    elif k > 2.65:
        return 4
    elif k > 2.52:
        return 5
    elif k > 2.43:
        return 6
    elif k > 2.37:
        return 7
    elif k > 2.28:
        return 8
    elif k > 2.23:
        return 10
    elif k > 2.20:
        return 12
    elif k > 2.17:
        return 14
    elif k > 2.15:
        return 16
    elif k > 2.13:
        return 18
    elif k > 2.11:
        return 20
    elif k > 2.09:
        return 25
    elif k > 2.07:
        return 30
    elif k > 2.06:
        return 35
    elif k > 2.05:
        return 45
    elif k > 2.04:
        return 50
    elif k > 2.03:
        return 60
    elif k > 2.02:
        return 80
    elif k > 2.00:
        return 100
    elif k == 2.0:
        return 50
    else:
        return float("inf")