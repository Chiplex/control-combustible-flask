#!/usr/bin/env python3
"""
Script de verificación post-despliegue
Ejecutar después del despliegue para verificar que todo funcione
"""

import os
import sys
from app import create_app, db
from app.models.tanques import Tanques
from app.models.responsables import Responsables

def verificar_aplicacion():
    """Verificar que la aplicación esté configurada correctamente"""
    
    app = create_app()
    
    with app.app_context():
        try:
            print("🔍 Verificando aplicación...")
            
            # Verificar conexión a la base de datos
            db.engine.execute("SELECT 1")
            print("✅ Conexión a base de datos OK")
            
            # Verificar tanques
            tanques_count = Tanques.query.count()
            almacenamiento_count = Tanques.query.filter_by(TipoId='Almacenamiento').count()
            consumo_count = Tanques.query.filter_by(TipoId='Consumo').count()
            
            print(f"✅ Tanques cargados: {tanques_count}")
            print(f"   - Almacenamiento: {almacenamiento_count}")
            print(f"   - Consumo: {consumo_count}")
            
            # Verificar responsables
            responsables_count = Responsables.query.count()
            print(f"✅ Responsables cargados: {responsables_count}")
            
            # Verificar saldos iniciales
            tanques_con_saldo = Tanques.query.filter(Tanques.Saldo > 0).count()
            print(f"✅ Tanques con saldo inicial: {tanques_con_saldo}")
            
            if tanques_count > 0 and responsables_count > 0:
                print("\n🎉 ¡Aplicación verificada correctamente!")
                print("✅ Base de datos inicializada")
                print("✅ Datos CSV cargados")
                print("✅ Sistema listo para usar")
                return True
            else:
                print("\n❌ Error: Datos no cargados correctamente")
                return False
                
        except Exception as e:
            print(f"\n❌ Error verificando aplicación: {e}")
            return False

if __name__ == "__main__":
    verificar_aplicacion()
