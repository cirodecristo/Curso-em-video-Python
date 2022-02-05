km = float(input('Digite a quantidade de KMs rodados:'))
dias = int(input('Digite por quantas diárias o carro foi alugado:'))
val_dia = dias * 60
val_km = km * 0.15
val_total = val_dia + val_km

print('\n----------\nEXTRATO DO CLIENTE:\n   * O custo por KMs rodados é de: R${:.2f} \n'
      '   * O custo das diárias é de: R${:.2f} \n   * O valor total a ser pago é de: R${:.2f} \n----------'
      .format(val_km, val_dia, val_total))