# Sistema de Control de Combustible - Flask + SQLite

Sistema de gestión de transferencias de combustible desarrollado con Flask y SQLite para despliegue urgente en PythonAnywhere.

## 🚀 Características

- **Transferencias de Combustible**: Registro de transferencias desde tanques de almacenamiento hacia tanques de consumo
- **Doble Registro**: Cada transferencia genera dos registros (salida del origen y entrada al destino)
- **Gestión de Responsables**: Asignación de responsables para cada transferencia  
- **Historial Completo**: Visualización de todas las transferencias con filtros
- **Base de Datos SQLite**: Perfecta para PythonAnywhere y fácil migración posterior
- **Carga Automática**: Datos iniciales desde archivos CSV

## Flujo de Trabajo

1. **Selección de Tanques**: Usuario selecciona tanque origen (almacenamiento) y destino (consumo)
2. **Asignación de Responsable**: Selecciona el responsable de la transferencia
3. **Registro de Cantidad**: Especifica la cantidad a transferir y detalles adicionales
4. **Procesamiento**: El sistema crea:
   - Un registro de salida (cantidad negativa) en el tanque origen
   - Un registro de entrada (cantidad positiva) en el tanque destino
   - Ambos unidos por un ID de transacción único

## Estructura del Proyecto

```
control-combustible-flask/
├── app/
│   ├── __init__.py
│   ├── data/
│   │   ├── personal.csv        # Datos de responsables
│   │   └── tanques.csv         # Datos de tanques
│   ├── models/
│   │   ├── __init__.py
│   │   ├── responsables.py     # Modelo de responsables
│   │   ├── tanques.py          # Modelo de tanques
│   │   ├── transferencias.py   # Modelo de transferencias
│   │   └── transacciones.py    # Modelo de transacciones
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py            # Rutas principales
│   │   └── transferencias.py  # Rutas de transferencias
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css      # Estilos CSS
│   │   └── js/
│   │       └── main.js        # JavaScript
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── registro_combustible.html
│       └── transferencias/
│           ├── detalle.html
│           └── listar.html
├── migrations/                 # Migración de Alembic
├── scripts/
│   └── init_db.py             # Script de inicialización
├── config.py                  # Configuración de la aplicación
├── requirements.txt           # Dependencias Python
├── run.py                     # Punto de entrada
└── README_DEPLOY.md          # Este archivo
```

## 🚀 Despliegue URGENTE en PythonAnywhere (5 minutos)

### Paso 1: Subir Archivos
1. Crear cuenta gratuita en [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Ir a **Files** y crear carpeta `control-combustible-flask`
3. Subir todos los archivos del proyecto

### Paso 2: Configurar Aplicación Web
1. Ir a pestaña **Web** → **Add a new web app**
2. Seleccionar **Manual configuration** → **Python 3.10**
3. En **Code section**:
   - **Source code**: `/home/TUUSUARIO/control-combustible-flask`
   - **Working directory**: `/home/TUUSUARIO/control-combustible-flask`
   - **WSGI configuration file**: `/home/TUUSUARIO/control-combustible-flask/wsgi.py`

### Paso 3: Configurar Entorno Virtual
1. Abrir **Bash console**
2. Ejecutar:
```bash
cd control-combustible-flask
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Paso 4: Editar WSGI
1. En **Files**, abrir `wsgi.py`
2. Cambiar `yourusername` por tu nombre de usuario real
3. Guardar el archivo

### Paso 5: Activar
1. Volver a pestaña **Web**
2. En **Virtualenv**: `/home/TUUSUARIO/control-combustible-flask/venv`
3. Hacer clic en **Reload**
4. ¡Listo! Tu aplicación estará en `https://TUUSUARIO.pythonanywhere.com`

### ⚠️ IMPORTANTE: 
- Reemplaza `TUUSUARIO` con tu nombre de usuario real de PythonAnywhere
- La base de datos SQLite se crea automáticamente
- Los datos de tanques y responsables se cargan desde los CSV

## 📊 Base de Datos SQLite

### Ventajas para Urgencia:
- ✅ **Sin configuración**: No requiere servidor de base de datos
- ✅ **Archivos simples**: Un solo archivo `.db`
- ✅ **Soporte nativo**: PythonAnywhere incluye SQLite por defecto
- ✅ **Migración fácil**: Exportar datos a SQL Server después

### Estructura de Datos:
- **Tanques**: Cargados desde `app/data/tanques.csv`
- **Responsables**: Cargados desde `app/data/personal.csv`  
- **Transferencias**: Se crean automáticamente con cada transacción
- **Transacciones**: Agrupan las transferencias de entrada y salida

### Migración Posterior a SQL Server:
```python
# Cuando esté listo, cambiar en config.py:
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://user:pass@server/db?driver=ODBC+Driver+17+for+SQL+Server'
```

## Uso del Sistema

### Registro de Transferencia

1. Accede a la URL principal de tu aplicación
2. Haz clic en "Registrar Transferencia"
3. Selecciona:
   - **Tanque Origen**: Debe ser de tipo "Almacenamiento"
   - **Tanque Destino**: Debe ser de tipo "Consumo"
   - **Responsable**: Persona encargada
   - **Cantidad**: Litros a transferir
   - **Detalles**: Información adicional (opcional)
4. Haz clic en "Registrar Transferencia"

### Ver Historial

1. Desde el inicio, haz clic en "Ver Transferencias"
2. Utiliza los filtros para buscar:
   - Por tipo (Entrada/Salida)
   - Por rango de fechas
3. Haz clic en cualquier transferencia para ver el detalle completo

## 🧪 Prueba Local (Opcional)

```bash
git clone <repositorio>
cd control-combustible-flask
python -m venv venv

# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
python run.py
```

La aplicación estará en `http://localhost:5000`

## ⚡ PythonAnywhere - Plan Gratuito

**Perfecto para urgencias:**
- ✅ 1 aplicación web gratis
- ✅ 512MB de almacenamiento
- ✅ SQLite incluido
- ✅ Dominio: `tuusuario.pythonanywhere.com`
- ✅ SSL automático
- ✅ 2 usuarios pueden usar sin problemas

**Tiempo de despliegue: ~5 minutos**

## 📝 Notas Importantes

1. **Datos iniciales**: Se cargan automáticamente desde los archivos CSV
2. **Persistencia**: Los datos se guardan en SQLite automáticamente  
3. **Backups**: Puedes descargar el archivo `.db` desde Files
4. **Escalabilidad**: Migración a SQL Server disponible cuando sea necesario
5. **Urgencia cumplida**: Sistema funcional en minutos

¡Perfecto para la urgencia actual! 🚀
