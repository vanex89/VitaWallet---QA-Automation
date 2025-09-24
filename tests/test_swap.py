
import pytest
from pages.crypto_page import CryptoPage

@pytest.mark.crypto
@pytest.mark.swap
def test_swap_ars_a_usdt(driver):
    crypto = CryptoPage(driver)
    crypto.ir_a_cripto()
    crypto.seleccionar_origen_ars()
    crypto.seleccionar_destino_usdt()
    crypto.ingresar_monto("100")
    crypto.confirmar()

    # TODO: Ajustar assert con el texto o elemento de confirmación real
    assert ("éxito" in driver.page_source.lower()) or ("confirmación" in driver.page_source.lower())
