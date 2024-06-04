cuenta_general = 1500
num_personas = 5
propina_porcentaje = 12

#valor_pagar = ((cuenta_general/num_personas)*112/100)
#print (f"Cada persona debe pagar: $ {valor_pagar}") 

valor_pagar = float(input("¿Cuál fue la factura total?:  $"))
tu_propina_es = int(input("¿Cuánta propina te gustaría dar:? ¿10, 12 o 15? "))
num_personas = int(input("¿Cuántas personas para dividir la cuenta:? "))



print(f"Cada persona debe pagar: ${round((valor_pagar * tu_propina_es/100 + valor_pagar) / num_personas,2)}")

