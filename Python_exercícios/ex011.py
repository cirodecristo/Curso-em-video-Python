alt = float(input('Digite a altura da parede em metros:'))
lar = float(input('Digite a largura da parede em metros:'))
area = alt * lar
tint = area/2

print('Sua parede mede {}m de altura e {}m de largura. \nPortanto, sua área é de {:.1f}m²,'
      ' e a quantia de tinta necessária para pintá-la é de {:.1f} litros.'.format(alt, lar, area, tint))
