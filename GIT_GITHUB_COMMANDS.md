# 🚀 COMANDOS GIT PARA SUBIR A GITHUB

## 📋 PREPARACIÓN DEL REPOSITORIO

### 1. Inicializar Git (si no está inicializado)
```bash
cd C:\dev\cc\control-combustible-flask
git init
```

### 2. Agregar archivos
```bash
# Agregar todos los archivos (el .gitignore filtrará automáticamente)
git add .

# Verificar qué archivos se agregarán
git status
```

### 3. Hacer commit inicial
```bash
git commit -m "Initial commit: Control de Combustible Flask

- Sistema completo de gestión de transferencias
- 205 tanques (5 almacenamiento, 200 consumo) 
- 382 responsables cargados desde CSV
- Autocompletado en formularios
- Validación de saldos y doble entrada contable
- Base de datos SQLite para portabilidad
- Configurado para PythonAnywhere
- Guías de despliegue incluidas"
```

## 🌐 CREAR REPOSITORIO EN GITHUB

### Opción A: Desde GitHub Web
1. Ve a https://github.com
2. Click "New repository"
3. Nombre: `control-combustible-flask`
4. Descripción: "Sistema web Flask para control de transferencias de combustible"
5. ✅ Public (para cuenta gratuita)
6. ❌ NO inicializar con README (ya tienes uno)
7. ❌ NO agregar .gitignore (ya tienes uno)
8. Click "Create repository"

### Opción B: Desde GitHub CLI (si tienes gh instalado)
```bash
gh repo create control-combustible-flask --public --description "Sistema web Flask para control de transferencias de combustible"
```

## 🔗 CONECTAR REPOSITORIO LOCAL CON GITHUB

```bash
# Agregar origin remoto (CAMBIAR 'tu-usuario' por tu usuario de GitHub)
git remote add origin https://github.com/tu-usuario/control-combustible-flask.git

# Verificar remote
git remote -v

# Subir a GitHub
git branch -M main
git push -u origin main
```

## 📝 ACTUALIZAR README

```bash
# Reemplazar README actual con la versión mejorada
mv README_NEW.md README.md

# Commitear el cambio
git add README.md
git commit -m "docs: Update README with comprehensive project documentation"
git push
```

## 🔄 COMANDOS PARA ACTUALIZACIONES FUTURAS

```bash
# Ver estado
git status

# Agregar cambios
git add .

# Commit con mensaje descriptivo
git commit -m "feat: descripción del cambio"

# Subir cambios
git push
```

## 📂 ARCHIVOS QUE SE SUBIRÁN

✅ **Se incluirán:**
- Código fuente completo (`app/`, `scripts/`)
- Archivos de configuración (`config.py`, `wsgi.py`, `run.py`)
- Templates y archivos estáticos (`templates/`, `static/`)
- Datos CSV (`app/data/tanques.csv`, `app/data/personal.csv`)
- Dependencias (`requirements.txt`)
- Documentación (`*.md`)
- Guías de despliegue

❌ **Se EXCLUIRÁN (por .gitignore):**
- Base de datos (`*.db`, `*.sqlite`)
- Entorno virtual (`venv/`)
- Archivos temporales (`__pycache__/`)
- Logs (`*.log`)
- Archivos de configuración local (`*.local`)

## 🎯 RESULTADO FINAL

Después de ejecutar estos comandos tendrás:

1. **Repositorio público** en GitHub: `https://github.com/tu-usuario/control-combustible-flask`
2. **Código completo** disponible para descargar
3. **Documentación completa** con guías de instalación y despliegue
4. **Historial de cambios** con Git
5. **Fácil despliegue** desde GitHub a PythonAnywhere

## 🚀 DESDE GITHUB A PYTHONANYWHERE

Una vez en GitHub, puedes clonar directamente en PythonAnywhere:

```bash
# En consola Bash de PythonAnywhere
cd ~
git clone https://github.com/tu-usuario/control-combustible-flask.git
cd control-combustible-flask
pip3.10 install --user -r requirements.txt
python3.10 scripts/init_db.py
```

## 💡 TIPS ADICIONALES

### Para colaboración:
```bash
# Crear rama para nuevas funcionalidades
git checkout -b nueva-funcionalidad

# Después de desarrollar
git add .
git commit -m "feat: nueva funcionalidad"
git push -u origin nueva-funcionalidad

# Crear Pull Request en GitHub
```

### Para releases:
```bash
# Crear tag de versión
git tag -a v1.0.0 -m "Primera versión estable del sistema"
git push origin v1.0.0
```

---

**📌 Recuerda:** Cambia `tu-usuario` por tu username real de GitHub en todos los comandos.
