nm = float(input('Digite uma medida em metros:'))
nkm = nm / 1000
nhm = nm / 100
ndam = nm / 10
ndm = nm * 10
nc = nm * 100
nmm = nm * 1000

print('\n{} metros correspondem a: \n\nkm = {} \nhm = {} \ndam = {} '
      '\ndm = {} \ncm = {} \nmm = {}'.format(nm, nkm, nhm, ndam, ndm, nc, nmm))
