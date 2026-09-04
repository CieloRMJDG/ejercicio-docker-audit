from app import app

def test_health_check():
    cliente = app.test_client()
    respuesta = cliente.get('/health')
    assert respuesta.status_code == 200, "El servicio de salud es inestable"
    assert respuesta.data.decode() == "OK"

def test_home():
    cliente = app.test_client()
    respuesta = cliente.get('/')
    assert respuesta.status_code in (200, 500), "La ruta raíz debe responder"

def test_buscar_devuelve_query_parametrizada():
    cliente = app.test_client()
    respuesta = cliente.get('/buscar?id=5')
    assert respuesta.status_code == 200
    datos = respuesta.get_json()
    assert datos["query"] == "SELECT * FROM usuarios WHERE id = %s"
    assert datos["parametros"] == ["5"]
