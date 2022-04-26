codigos_postales = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____.*"
datos = {"1":".____", "2":"..___", "3":"...__", "4":"...._" , "5":".....", "6":  "_....", "7": "__...", "8":"___.."  , "9":"____.", "0": "_____"}
codigos_postales = codigos_postales.replace("*","\n")
for i in datos:
    codigos_postales = codigos_postales.replace(datos[i],i)
print(codigos_postales)