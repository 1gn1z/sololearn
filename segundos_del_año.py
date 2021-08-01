# Calcular los segundos de un mes (30 dias)

horas_mes = 24 * 30
print(horas_mes)

minutos_mes = horas_mes * 60
print(minutos_mes)

segundos_mes = minutos_mes * 60
print(segundos_mes)

# Vamos a tratar de simplificar el codigo:

horas_mes1 = 24 * 30 * 60 * 60
#      24 horas * 30 dias = 720horas
# Ya que sabemos que el mes tiene 720 horas, podemos multiplicar 720 horas * 60 minutos, y el resultado (que son los minutos totales minutos) y luego * 60 que son los segundos                                         
print(horas_mes1)
