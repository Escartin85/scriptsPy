

num_dominios = 25000
price_dominio = 12
price_dominios = num_dominios * price_dominio
páginas_vistas_dia_dominio = 150000
número_de_banners = 8
eCPM_medio = 0.5

ingresos_web = (páginas_vistas_dia_dominio * número_de_banners * eCPM_medio)/1000.0
ingresos_webs = ingresos_web * num_dominios

sec = 60 * 60 * 24
veces = sec / 20
total_visitas_por_mobile = páginas_vistas_dia_dominio / veces
mobiles = total_visitas_por_mobile * num_dominios

print("Ingresos day 1 web: ", ingresos_web)
print("Ingresos day webs: ", ingresos_webs)
print("Ingresos mes webs: ", ingresos_webs * 30)
print()
print("Veces por mobile: ", veces)
print("Mobiles para una web: ", total_visitas_por_mobile)
print("Mobiles totales: ", mobiles)
print()
print("---------------------")
print()

visitas_mobile = veces
ingresos_mobile = (visitas_mobile * número_de_banners * eCPM_medio)/1000.0
num_mobiles = 50500
ingresos_mobiles = ingresos_mobile * num_mobiles

print("Ingresos 1 mobile/day: ", ingresos_mobile)
print("Ingresos", num_mobiles, "mobiles/day: ", ingresos_mobiles)
print("Ingresos", num_mobiles, "mobiles/mes: ", ingresos_mobiles * 30)
print()

num_total_visitas = num_mobiles * visitas_mobile
num_total_visitas_web = num_total_visitas / num_dominios

print("Visitas de una web/dia:", num_total_visitas_web)
print("Visitas de una web/m:", num_total_visitas_web * 30)
print("Visitas de una webs/dia:", num_total_visitas)
print("Visitas de una webs/m:", num_total_visitas * 30)
print()

ingresos_web = (num_total_visitas * número_de_banners * eCPM_medio)/1000.0
ingresos_webs = ingresos_web * num_dominios

print("Ingresos web/day: ", ingresos_web)
print("Ingresos webs/day: ", ingresos_webs)
print("Ingresos web/m: ", ingresos_web * 30)
print("Ingresos webs/m: ", ingresos_webs * 30)
print()
