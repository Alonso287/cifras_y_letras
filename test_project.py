import letras, cifras, project

def test_extraer_operacion():
    assert cifras.extraer_operacion("1+1") == [1, "+", 1]
    assert cifras.extraer_operacion("1+ 1") == [1, "+", 1]
    assert cifras.extraer_operacion("1 +1") == [1, "+", 1]
    assert cifras.extraer_operacion("1 + 1") == [1, "+", 1]
    assert cifras.extraer_operacion(" 1+1 ") == [1, "+", 1]
    assert cifras.extraer_operacion("1+1") == [1, "+", 1]
    assert cifras.extraer_operacion("    256841  /  1658  ") == [256841, "/", 1658]

def test_quitar_tildes():
    assert letras.quitar_tildes("á") == "a"
    assert letras.quitar_tildes("é") == "e"
    assert letras.quitar_tildes("í") == "i"
    assert letras.quitar_tildes("ó") == "o"
    assert letras.quitar_tildes("ú") == "u"
    assert letras.quitar_tildes("áéíóú") == "aeiou"

def test_buscar_palabra():
    assert letras.buscar_palabra("casa") == True
    assert letras.buscar_palabra("CS50") == False
    assert letras.buscar_palabra("coche") == True

def test_generar_cifras_disponibles():
    assert len(cifras.generar_cifras_disponibles()) == 6

def test_generar_letras_disponibles():
    assert len(letras.generar_letras_disponibles()) == 10
    assert len(letras.generar_letras_disponibles(modo_anagrama=True)) == 10

def test_operar():
    assert cifras.operar(1, "+", 1) == 2
    assert cifras.operar(1, "-", 1) == 0
    assert cifras.operar(1, "*", 1) == 1
    assert cifras.operar(1, "/", 1) == 1
