Vita Wallet – QA Automation (Appium + Python)

Automatización **mobile Android** con **Appium + Python (PyTest)**. Caso principal: **Intercambio ARS → USDT**.
Este README es la **única fuente** de instrucciones para ejecutar y evaluar la entrega.

Contenidos
- `pages/` Page Objects (POM)
- `tests/` Pruebas PyTest
- `evidencias/` Reporte HTML, Logcat, video, screenshots
- `docs/` Documentación de referencia (consigna PDF y guías). *No hay otros READMEs duplicados.*

Requisitos
- **Windows 10/11**
- **Android Studio** con SDK + Emulador (API 30+)
- **Node.js** y **Appium 2** con **uiautomator2**
- **Python 3.10+** y **venv**
- Appium Server corriendo en `http://127.0.0.1:4723`

Instalación
```cmd
npm i -g appium
appium driver install uiautomator2

python -m venv .venv
.\.venv\Scriptsctivate
pip install -r requirements.txt

# En otra ventana
appium
```

 Ejecución (swap ARS → USDT)
```cmd
# Variables opcionales
set VITA_PIN=123456
set SWAP_MONTO_ARS=1000

# Ejecutar el caso
pytest -q -m swap -s

# Reporte HTML (opcional)
pytest -q -m swap --html=evidencias\report.html --self-contained-html
```
> Exporta **Logcat** desde Android Studio (Logcat → `package:<package> level:V`) y guárdalo en `evidencias/logcat_app.txt`.

¿Qué valida?
- Login (si aplica) → **Cripto → Intercambiar**.
- Monto **ARS** en fila superior.
- Abrir selector **Hacia** (2ª fila), elegir **USDT** (tolerante a “USDT/Tether/USDt”).  
- **Reaplicar monto** si la app lo resetea → **Continuar/Confirmar**.
- Verificación liviana de ausencia de mensajes de error.

Estructura
```
.
├─ pages/
├─ tests/
├─ utils/
├─ docs/                  # Referencia: consigna + guías (sin READMEs duplicados)
│  ├─ Prueba técnica QA Automation mobile-API.pdf
│  ├─ Guia_Instalacion_Entorno_Appium_v2.docx
│  ├─ Guia_Appium_VitaWallet.docx
│  └─ extras/             # Material secundario (no necesario para ejecutar)
├─ evidencias/
│  ├─ report.html         # (generado)
│  ├─ logcat_app.txt      # (exportado)
│  ├─ video/              # (opcional)
│  └─ screenshots/        # (si hay)
├─ app/                   # (vacía) colocar VitaQA.apk si se desea
├─ requirements.txt
├─ pytest.ini
└─ README.md              # este archivo (único)
```

Notas técnicas
- POM: `pages/crypto_page.py` y `pages/login_page.py`.
- Robustez de flujos (taps por texto/desc y por coordenadas, reintentos, `UiScrollable`).
- Si cambia el layout, ajustar selectores con Appium Inspector.

