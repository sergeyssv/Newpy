import sys


FILENAME = "DANN_OP_MYFILE1.txt"

cnt = 40000
c_lengop = 1000
c_rvop = 500
c_wfop = 900
c_maxwfop = 8000
c_procop = 25
c_azmop = 180
c_cfgop = 0
c_sw1op = 0
c_sw2op = 0
c_rlop = 0
c_depop = 0
c_kzapop = 0
c_heighop = 600
c_t1op = 1111
c_t2op = 7
c_lgusop = 0
c_anglstrop = 0
c_anglgusop = 0
c_kzazmleftop = 0
c_kzazmrigthop = 0
c_kzazmwallop = 0
c_kzrvwall = 0
c_kzheighop = 0
c_kzrvop = 0


def change_Dn(A_min_h, A_max_h, A_dia_tim, A_tim):
    A_Tmp = (A_max_h - A_min_h) * A_tim / A_dia_tim + A_min_h
    return int(A_Tmp)


datecikl = '2021-01-01 '
sec = 0
minut = 1
hour = 2

Strdttim = datecikl + str(hour) + ':' + str(minut) + ':' + str(sec)

myf = open(FILENAME, "w", -1)

SecNagr = 30
for i in range(SecNagr):
    sec = sec + 1
    Strdttim = datecikl + str(hour) + ':' + str(minut) + ':' + str(sec)
    c_lengop = change_Dn(1000, 2000, SecNagr, i)
    StrDann_op = "%s\t211111\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
    cnt, Strdttim, c_lengop, c_rvop, c_wfop, c_maxwfop, c_procop, c_azmop, c_cfgop, c_sw1op, c_sw2op, c_rlop, c_depop,
    c_kzapop, c_heighop, c_t1op, c_t2op, c_lgusop, c_anglstrop, c_anglgusop, c_kzazmleftop, c_kzazmrigthop,
    c_kzazmwallop, c_kzrvwall, c_kzheighop, c_kzrvop)
    cnt = cnt + 1
    myf.write(StrDann_op)
myf.close



