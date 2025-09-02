# 🚀 Guía de Despliegue URGENTE - PythonAnywhere

## ✅ Sistema Listo para Despliegue

Tu sistema de control de combustible está **100% funcional** y listo para PythonAnywhere. 

### 📊 Datos Cargados
- **205 tanques** (incluye Almacenamiento, Consumo y Demanda)
- **382 responsables** del personal
- **Base de datos SQLite** completamente configurada

## 🚀 Pasos para Despliegue en PythonAnywhere (15 minutos)

### 1. Crear Cuenta FREE en PythonAnywhere
- Ve a: https://www.pythonanywhere.com
- Registrar cuenta gratuita
- Confirma tu email

### 2. Subir Archivos
```bash
# En la pestaña "Files" de PythonAnywhere, sube toda la carpeta:
control-combustible-flask/
```

### 3. Configurar Entorno Virtual
```bash
# En "Bash Console" de PythonAnywhere:
cd control-combustible-flask
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Inicializar Base de Datos
```bash
python scripts/init_db.py
```

### 5. Configurar Web App
1. Ve a la pestaña **"Web"**
2. **"Add a new web app"**
3. Selecciona **"Manual configuration"**
4. Elige **Python 3.9**

### 6. Configuración WSGI
- **Source code**: `/home/tu-usuario/control-combustible-flask`
- **WSGI file**: Editar y pegar:

```python
import sys
import os

# Ruta del proyecto (cambiar tu-usuario por tu username real)
project_home = '/home/tu-usuario/control-combustible-flask'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from run import app as application

if __name__ == "__main__":
    application.run()
```

### 7. Configurar Virtual Environment
- **Virtualenv**: `/home/tu-usuario/control-combustible-flask/venv`

### 8. Archivos Estáticos
- **Static files**: 
  - URL: `/static/`
  - Directory: `/home/tu-usuario/control-combustible-flask/app/static/`

### 9. ¡LISTO! 
- Haz clic en **"Reload"**
- Tu app estará en: `https://tu-usuario.pythonanywhere.com`

## 🎯 Funcionalidades Disponibles

### ✅ Registro de Transferencias
1. Selecciona **tanque origen** (Almacenamiento)
2. Selecciona **tanque destino** (Consumo)  
3. Asigna **responsable**
4. Especifica **cantidad en litros**
5. Agrega **detalles opcionales**

### ✅ Sistema Automático
- Crea automáticamente 2 registros:
  - **SALIDA** del tanque origen (-cantidad)
  - **ENTRADA** al tanque destino (+cantidad)
- Ambos unidos por **ID de transacción único**
- Actualiza **saldos automáticamente**

### ✅ Historial Completo
- Lista todas las transferencias
- Filtros por tipo y fecha
- Detalle completo de cada transacción

## 🔧 Mantenimiento

### Agregar más tanques:
Edita `app/data/tanques.csv` y ejecuta:
```bash
python scripts/init_db.py
```

### Agregar más responsables:
Edita `app/data/personal.csv` y ejecuta:
```bash
python scripts/init_db.py
```

### Backup de datos:
La base de datos SQLite está en: `control_combustible.db`
¡Descárgala regularmente como backup!

## 🆘 Solución de Problemas

### Si algo falla:
1. Revisa los **Error logs** en PythonAnywhere
2. Verifica las **rutas de archivos** (reemplaza `tu-usuario`)
3. Asegúrate que el **virtualenv** esté activado

### URLs importantes:
- **Registro**: `/registro_combustible`
- **Historial**: `/transferencias/`
- **API**: `/transferencias/api/resumen`

## 🎉 ¡ÉXITO!

Tu sistema está **LISTO** para:
- ✅ 2 usuarios simultáneos
- ✅ Gestión urgente de combustible  
- ✅ Registro de transferencias
- ✅ Historial completo
- ✅ Interfaz responsive

**Tiempo total de despliegue**: ~15 minutos en PythonAnywhere

---
*Sistema desarrollado con Flask + SQLite para despliegue urgente*
