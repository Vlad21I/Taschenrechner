print('Willkommen beim Python-Rechner')
q1 = int(input('Geben Sie die Zahl 1 ein: '))
q2 = int(input('Geben Sie die Zahl 2 ein: '))

v = int(input('Welche Operation möchten Sie durchführen? \n 1 Zusatz \n 2 Subtraktion \n 3 Spaltung \n 4 Multiplikation \n'))

if v == 1:
    r = q1 + q2
    p = 'Zusatz'
    t = p
if v == 2:
    r = q1 - q2
    l = 'Subtraktion'
    t = l
if v == 3:
    r = float(q1 / q2)
    m = 'Spaltung'
    t = m
if v == 4:
    r = q1 * q2
    n = 'Multiplikation'
    t = n
print('Ergebnis ', t, ' = ', r)
