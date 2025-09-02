# 🚛 Control de Combustible Flask

Sistema web para el control y gestión de transferencias de combustible entre tanques de almacenamiento y consumo. Desarrollado con Flask 3.0 y SQLite para despliegue rápido y urgente.

## 🎯 Características Principales

- ✅ **Sistema de doble entrada contable** - Registro automático de ENTRADA y SALIDA
- ✅ **Autocompletado inteligente** - Búsqueda por tanques y responsables
- ✅ **Validación de saldos** - Control de existencias disponibles
- ✅ **Base de datos SQLite** - Sin dependencias externas
- ✅ **Interfaz responsive** - Funciona en desktop y móvil
- ✅ **Carga automática de datos CSV** - 205 tanques y 382 responsables

## 🗄️ Estructura de Datos

### Tanques
- **5 tanques de almacenamiento** (5000L c/u inicialmente)
- **200 tanques de consumo** (0L inicialmente)
- Control de capacidades y tolerancias

### Personal
- **382 responsables** cargados desde CSV
- Identificación por CI y nombre completo

## 🚀 Despliegue Rápido

### Requisitos
- Python 3.10+
- Flask 3.0+
- SQLAlchemy 3.0+

### Instalación Local
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/control-combustible-flask.git
cd control-combustible-flask

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Inicializar base de datos
python scripts/init_db.py

# Ejecutar aplicación
python run.py
```

### Despliegue en PythonAnywhere
1. Sigue la guía completa: [`GUIA_DESPLIEGUE_PYTHONANYWHERE.md`](GUIA_DESPLIEGUE_PYTHONANYWHERE.md)
2. Usa los comandos de referencia: [`COMANDOS_PYTHONANYWHERE.md`](COMANDOS_PYTHONANYWHERE.md)

## 📱 Uso del Sistema

### Registro de Transferencias
1. **Seleccionar tanque origen** (almacenamiento)
2. **Buscar tanque destino** (consumo) con autocompletado
3. **Seleccionar responsable** con búsqueda por nombre o CI
4. **Ingresar cantidad** a transferir
5. **Confirmar transferencia** - Se crean automáticamente:
   - Registro de SALIDA en tanque origen
   - Registro de ENTRADA en tanque destino
   - Actualización de saldos

### Funcionalidades de Autocompletado
- **Tanques**: Filtro por código mientras escribes
- **Responsables**: Búsqueda por nombre o CI
- **Navegación por teclado**: ↑↓ Enter Escape

## 🔧 Estructura del Proyecto

```
control-combustible-flask/
├── app/
│   ├── __init__.py           # Factory pattern Flask
│   ├── models/               # Modelos SQLAlchemy
│   │   ├── tanques.py       # Modelo de tanques
│   │   ├── responsables.py  # Modelo de responsables
│   │   ├── transferencias.py # Modelo de transferencias
│   │   └── transacciones.py # Modelo de transacciones
│   ├── routes/              # Rutas Blueprint
│   │   ├── main.py         # Rutas principales + APIs
│   │   └── transferencias.py # Rutas de transferencias
│   ├── templates/           # Templates Jinja2
│   ├── static/             # CSS, JS, imágenes
│   └── data/              # Archivos CSV
├── scripts/
│   ├── init_db.py         # Inicialización de BD
│   └── verificar_despliegue.py # Verificación post-deploy
├── config.py              # Configuración Flask
├── run.py                # Punto de entrada desarrollo
├── wsgi.py              # Punto de entrada producción
└── requirements.txt     # Dependencias Python
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.0, SQLAlchemy 3.0.5
- **Base de Datos**: SQLite (para portabilidad)
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Despliegue**: PythonAnywhere (gratuito)

## 📊 APIs Disponibles

### Tanques por Tipo
```
GET /api/tanques/<tipo>
Parámetros: tipo = "Almacenamiento" | "Consumo"
Respuesta: [{"TanqueId": "TQ001", "Codigo": "TCD-VH-01-01", "Tipo": "Consumo"}]
```

### Responsables con Filtro
```
GET /api/responsables?q=<busqueda>
Parámetros: q = término de búsqueda (opcional)
Respuesta: [{"ResponsableId": "123", "Nombre": "Juan Pérez", "CI": "12345"}]
```

## 🐛 Solución de Problemas

### Error de tipos de datos (Decimal vs Float)
- ✅ **Solucionado**: Conversión automática a Decimal

### Tanques de almacenamiento no aparecen
- ✅ **Solucionado**: Corrección de propiedad `tipo` en modelo

### Campos de autocompletado
- ✅ **Implementado**: Sistema completo con navegación por teclado

## 🔄 Mantenimiento

```bash
# Reiniciar base de datos
python scripts/init_db.py

# Verificar estado del sistema
python scripts/verificar_despliegue.py

# Ver logs (en PythonAnywhere)
tail -f ~/logs/error.log
```

## 📝 Notas de Desarrollo

- **Urgencia**: Diseñado para despliegue inmediato
- **Simplicidad**: SQLite para evitar configuración de BD
- **Portabilidad**: Archivos CSV incluidos en el proyecto
- **Escalabilidad**: Estructura preparada para migrar a PostgreSQL

## 🎯 Casos de Uso

1. **Transferencia típica**: Almacén → Maquinaria
2. **Control de inventario**: Saldos automáticos
3. **Auditoría**: Registro de todas las operaciones
4. **Responsabilidad**: Asignación por persona y CI

## 📞 Soporte

Para problemas técnicos:
1. Revisar guías de despliegue
2. Consultar comandos de diagnóstico
3. Verificar logs de error

---

**🚀 Desarrollado para despliegue urgente con Flask + SQLite + PythonAnywhere**

*Sistema completo de gestión de combustible con doble entrada contable*
