#Manejo de errores:
#Para garantizar que nuestros programas sean robustos y puedan manejar 
#situaciones inesperadas, el uso de manejo de errores es fundamental

#En python los errores se conocen como excepciones y se producen
#cuando ocurre situaciones inesperadas durante la ejecucion del programa

        #try:
            #codigo sospechoso
        #except ExceptionType:
            #Manejar la excepcion

#El bloque try-except: se utiliza para capturar
#y maneja excepciones. El código que realiza la operacion
#va dentro del bloque try, y cuando se procedure alguna excepción
#se ejecuta el bloque except correspondiente
#El bloque except puede manejar excepciones especificas o genericas
#Especificas es cuando en except declaramos el error especifico
#pero si solo va el except se agrega un mensaje general

        #try:
            #codigo sospechoso
        #except ValueError:
            #Manejar la excepción ValueError
        #except:
            #Manejar cualquier otra excepción


#Bloque finally: El bloque finally se utiliza para ejecutar código que debe
#ejecutarse sin importar si se produjo una excepción o no. Este bloque se 
#coloca después del bloque try-except.

        #try:
            #codigo sospechoso
        #except ValueError:
            #Manejarla excepcion valueError
        #finally:
            #codigo que siempre se ejecuta

#Clausula raise: Esta clausula se utiliza pra generar de manera manual
#una excepcion en Python, que permite lanzar una excepcion especifica
#cuando ocurre una condicion no deseada

        #if condicion:
        #    raise ExceptionType("mensaje de error")

#Para generar una excepción TypeError, se utiliza la siguiente línea
        #raise TypeError("Se esperaba un tipo de dato diferente")



#Bloque try-except-else: En este bloque se puede usar un else para especificar
#un código que se ejecutar si no se produce ninguna excepción

        #try:
            #codigo sospechoso
        #exceptExceptionType:
            #Manejar la excepción
        #else:
            #Código que seehecta si no hay excepciones

#Manejo de excepciones específicas: Así como podemos capturar excepciones genéricas
#también podemos manejar excepciones específicas y personalizadas, lo cuál permite
#un manejo más granular, adaptándolo a situacones particulares

        #try:
            #codigo sospechoso
        #except ValueError as ve:
            #manejo excepción ValueError
        #except TypeError as te:
            #manejo excepción TypeError

