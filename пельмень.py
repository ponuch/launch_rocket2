qna = float(input('input qna \n'))
qt = float(input('input qt \n'))
qk = float(input('input qk \n'))
Qc = float(input('input Qc \n'))
t = float(input('input t \n'))
at = float(input('input at \n'))

Qp = Qc / (2 * t)
nna = Qp / qna
print('nna = ', int(nna))

Qt = at * Qp
nt = Qt / qt
print('nt = ', int(nt))



Qf = (1 - at) * Qp
nk = Qf / qk
print('nk = ', int(nk))

input()
