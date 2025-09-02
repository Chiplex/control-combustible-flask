# 📝 COMANDOS ÚTILES PARA PYTHONANYWHERE

## 🚀 COMANDOS INICIALES (Ejecutar en Bash Console)

```bash
# Navegar al directorio del proyecto
cd ~/control-combustible-flask

# Verificar archivos
ls -la

# Verificar versión de Python
python3.10 --version

# Instalar dependencias
pip3.10 install --user -r requirements.txt

# Verificar instalación
pip3.10 list --user

# Inicializar base de datos
python3.10 scripts/init_db.py

# Verificar que todo funcione
python3.10 scripts/verificar_despliegue.py
```

## 🔄 COMANDOS DE MANTENIMIENTO

```bash
# Reiniciar aplicación web
# (Hacer desde el dashboard web, botón "Reload")

# Verificar logs de errores
tail -f ~/logs/error.log

# Limpiar base de datos y recargar
rm -f control_combustible.db
python3.10 scripts/init_db.py

# Verificar estructura de base de datos
python3.10 -c "
from app import create_app, db
app = create_app()
with app.app_context():
    print('Tablas en BD:', db.engine.table_names())
"

# Ver tanques de almacenamiento
python3.10 -c "
from app import create_app
from app.models.tanques import Tanques
app = create_app()
with app.app_context():
    tanques = Tanques.query.filter_by(TipoId='Almacenamiento').all()
    for t in tanques:
        print(f'{t.Codigo} - Saldo: {t.Saldo}L')
"
```

## 📊 COMANDOS DE DIAGNÓSTICO

```bash
# Verificar espacio en disco
df -h

# Verificar procesos Python
ps aux | grep python

# Ver archivos CSV
head -5 app/data/tanques.csv
head -5 app/data/personal.csv

# Verificar permisos
ls -la app/data/

# Test de conectividad a la aplicación
curl -I https://yourusername.pythonanywhere.com
```

## 🗄️ COMANDOS DE BASE DE DATOS

```bash
# Backup de base de datos
cp control_combustible.db backup_$(date +%Y%m%d).db

# Restaurar backup
cp backup_YYYYMMDD.db control_combustible.db

# Ver contenido de BD con SQLite
python3.10 -c "
import sqlite3
conn = sqlite3.connect('control_combustible.db')
cursor = conn.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type=\"table\"')
print('Tablas:', cursor.fetchall())
cursor.execute('SELECT COUNT(*) FROM tanques')
print('Total tanques:', cursor.fetchone()[0])
conn.close()
"
```

## ⚠️ SOLUCIÓN DE PROBLEMAS COMUNES

### Error: ModuleNotFoundError
```bash
# Reinstalar dependencias
pip3.10 install --user --force-reinstall -r requirements.txt
```

### Error: Database locked
```bash
# Reiniciar aplicación web desde dashboard
# O eliminar y recrear BD:
rm -f control_combustible.db
python3.10 scripts/init_db.py
```

### Error 500 en la aplicación
```bash
# Revisar logs
tail -20 ~/logs/error.log
tail -20 ~/logs/server.log
```

### Archivos CSS/JS no cargan
```bash
# Verificar archivos estáticos
ls -la app/static/css/
ls -la app/static/js/
# Configurar Static Files en Web dashboard:
# URL: /static/
# Directory: /home/yourusername/control-combustible-flask/app/static/
```

## 🔄 ACTUALIZAR APLICACIÓN

```bash
# Si tienes cambios en el código
cd ~/control-combustible-flask

# Respaldar BD actual
cp control_combustible.db backup_$(date +%Y%m%d).db

# Subir nuevos archivos (manual o git pull)
# Después:
pip3.10 install --user -r requirements.txt
python3.10 scripts/verificar_despliegue.py

# Reiniciar desde Web dashboard
```

---

**💡 Tip:** Guarda estos comandos para referencia futura. PythonAnywhere mantiene las consolas abiertas, así que puedes tener una pestaña de Bash siempre disponible para mantenimiento.
