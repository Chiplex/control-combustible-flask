# 🚀 GUÍA DE DESPLIEGUE EN PYTHONANYWHERE - Control de Combustible

## ✅ PREREQUISITOS
- Cuenta gratuita en PythonAnywhere creada
- Proyecto funcionando localmente

## 📋 PASO A PASO PARA SUBIR EL PROYECTO

### 1. 💻 SUBIR ARCHIVOS

**Opción A: Desde consola de PythonAnywhere (Recomendado)**
```bash
# Abrir consola Bash en PythonAnywhere Dashboard
$ cd ~
$ git clone https://github.com/tu-usuario/control-combustible-flask.git
```

**Opción B: Subir archivos manualmente**
1. Ve a "Files" en tu dashboard de PythonAnywhere
2. Crea una carpeta llamada `control-combustible-flask`
3. Sube todos los archivos del proyecto (excepto __pycache__, .git, venv)

### 2. 🔧 CONFIGURAR WEB APP

1. **Ir a "Web" en el Dashboard**
2. **Crear nueva Web App:**
   - Click "Add a new web app"
   - Seleccionar "Manual configuration"
   - Seleccionar Python 3.10

3. **Configurar WSGI file:**
   - En la sección "Code", editar el archivo WSGI
   - Reemplazar el contenido con el archivo `wsgi.py` del proyecto
   - ⚠️ **IMPORTANTE:** Cambiar la línea:
     ```python
     project_home = '/home/yourusername/control-combustible-flask'
     ```
     Reemplazar `yourusername` con tu usuario real de PythonAnywhere

### 3. 📦 INSTALAR DEPENDENCIAS

1. **Abrir consola Bash**
2. **Instalar paquetes:**
   ```bash
   $ cd ~/control-combustible-flask
   $ pip3.10 install --user -r requirements.txt
   ```

### 4. 🗃️ CONFIGURAR BASE DE DATOS

1. **Ejecutar en consola Bash:**
   ```bash
   $ cd ~/control-combustible-flask
   $ python3.10 scripts/init_db.py
   ```

### 5. 📁 CONFIGURAR ARCHIVOS ESTÁTICOS

1. **En la configuración Web App:**
   - Ir a sección "Static files"
   - Agregar entrada:
     - URL: `/static/`
     - Directory: `/home/yourusername/control-combustible-flask/app/static/`

### 6. ▶️ ACTIVAR LA APLICACIÓN

1. **En la página Web:**
   - Click en "Reload yourusername.pythonanywhere.com"
2. **Visitar:** `https://yourusername.pythonanywhere.com`

## 🔧 CONFIGURACIÓN DEL ARCHIVO WSGI

El archivo `wsgi.py` debe tener esta estructura:
```python
import sys
import os

# CAMBIAR 'yourusername' por tu usuario real
project_home = '/home/yourusername/control-combustible-flask'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.environ['FLASK_CONFIG'] = 'production'

from app import create_app
application = create_app()
```

## ✅ VERIFICAR FUNCIONAMIENTO

1. **Acceder a la aplicación:** `https://yourusername.pythonanywhere.com`
2. **Probar funciones:**
   - Página principal debe cargar
   - Formulario de registro debe mostrar tanques de almacenamiento
   - Campos de autocompletado deben funcionar
   - Registro de transferencias debe procesarse

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error 500:
1. Revisar logs en "Web" > "Error log"
2. Verificar que el path en wsgi.py sea correcto
3. Verificar que todas las dependencias estén instaladas

### Base de datos no carga:
1. Ejecutar nuevamente: `python3.10 scripts/init_db.py`
2. Verificar que los archivos CSV estén en `app/data/`

### Archivos estáticos no cargan:
1. Verificar configuración en "Static files"
2. Verificar permisos de archivos

## 📧 DATOS DE LA APLICACIÓN

- **Tanques de almacenamiento:** 5 tanques con 5000L cada uno
- **Tanques de consumo:** 200 tanques 
- **Responsables:** 382 personas cargadas
- **Funcionalidades:**
  - ✅ Autocompletado en formularios
  - ✅ Validación de saldos
  - ✅ Doble entrada contable
  - ✅ Interface responsive

## 🎉 ¡LISTO!

Tu aplicación de Control de Combustible estará funcionando en:
`https://yourusername.pythonanywhere.com`

---
*Aplicación desarrollada con Flask 3.0, SQLAlchemy y SQLite*
*Diseñada para gestión de transferencias de combustible con doble entrada contable*
