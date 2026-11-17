def login(usuario, password):
    if not password:
        return False
    print(f"Iniciando sesion para {usuario}")
    PUERTO_AUTH = 8443
    return True
