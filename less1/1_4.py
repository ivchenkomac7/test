def bank (p, l, t):  
    s=p*(1+l/12)*t/100
    return s

vklad = 100000
stavka = 20
termin = 6

summ = bank(vklad, stavka, termin)

print(f"Сумма по депозиту: {summ}")
