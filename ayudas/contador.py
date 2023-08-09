def contar_coincidencias(texto, caracter):
    contador = 0
    for c in texto:
        if c == caracter:
            contador += 1
    return contador

texto = "551|39269099|PROTECTOR DE PLASTICO PARA CAJAS TRANSPORTADORES DE METERIAL|AJUPER6435|463.15|3000.000|06|213.000|0.00|1|6|||KOR|USA||3000.000|C62_1||0||213|||USD|0.||||||||||0.15438333||463.15|1|0.07100000|0.07766667||DEF-2303011|||"
texto2= "551|84191101|CALENTADOR DE GAS INSTANTANEO PARA AGUA|JXI400P|1048.38|1.000|06|1.000|0.10|0|0|||USA|USA||1.000|C62_1||0||63.957|||USD|0||||||||||1048.38000000||1048.38|6|63.95760000|63.95760000||CNP-1375||||00|"
texto3="551|85371099|CONTROL ALAMBRICO PARA TELESCOPIO|35-4700-20ES|198.45|5.00|06|0.94|0.00|1|0|||USA|USA||5.00|C62_1||0||0.94|||USD|0.000||||||||||39.69||198.45|1|0.19|0.19||MP-04189|||99|"
texto4="501|2|A1|3005201|1|0|0|0|0|0|1439.997|2|7|7|7|1|DEF23-002|||||||||"
caracter_buscado = '|'
cantidad_coincidencias = contar_coincidencias(texto4, caracter_buscado)

print(f"El número de coincidencias de '{caracter_buscado}' en el texto es: {cantidad_coincidencias}")
