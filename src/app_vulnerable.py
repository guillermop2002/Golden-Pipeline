#!/usr/bin/env python3
"""
🚨 ARCHIVO VULNERABLE - SOLO PARA DEMOSTRACIÓN 🚨

Este archivo contiene vulnerabilidades INTENCIONADAS para demostrar
el funcionamiento del pipeline de seguridad.

NUNCA uses código como este en producción.
"""

import sqlite3
import requests

# ============================================
# 🔴 VULNERABILIDAD 1: Secreto Hardcodeado
# ============================================
# Gitleaks detectará esta contraseña
DATABASE_PASSWORD = "SuperSecretP@ssw0rd123!"
API_KEY = "sk-proj-abc123xyz789secretapikey"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


# ============================================
# 🔴 VULNERABILIDAD 2: SQL Injection
# ============================================
# Semgrep detectará esta inyección SQL
def get_user_by_id(user_id):
    """
    ⚠️ VULNERABLE: Esta función es susceptible a SQL Injection.
    Un atacante podría inyectar: ' OR '1'='1
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # 🚨 MAL: Concatenación directa de input del usuario
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    
    return cursor.fetchone()


def authenticate_user(username, password):
    """
    ⚠️ VULNERABLE: SQL Injection en autenticación.
    Un atacante podría bypassear el login con: admin'--
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # 🚨 MAL: f-string con input del usuario directamente
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    return cursor.fetchone() is not None


# ============================================
# 🔴 VULNERABILIDAD 3: Uso inseguro de eval()
# ============================================
# Semgrep detectará el uso peligroso de eval
def calculate(expression):
    """
    ⚠️ VULNERABLE: eval() ejecuta código arbitrario.
    Un atacante podría ejecutar: __import__('os').system('rm -rf /')
    """
    # 🚨 MAL: eval() con input del usuario
    result = eval(expression)
    return result


# ============================================
# 🔴 VULNERABILIDAD 4: Request sin verificación SSL
# ============================================
def fetch_data(url):
    """
    ⚠️ VULNERABLE: Deshabilitando verificación SSL.
    Susceptible a ataques Man-in-the-Middle.
    """
    # 🚨 MAL: verify=False deshabilita la verificación de certificados
    response = requests.get(url, verify=False)
    return response.json()


# ============================================
# Función principal (Hola Mundo)
# ============================================
def main():
    """
    Simple Hola Mundo con credenciales expuestas.
    """
    print("🌍 ¡Hola Mundo desde el Golden Pipeline!")
    print(f"📧 Conectando a la base de datos con password: {DATABASE_PASSWORD}")
    print(f"🔑 Usando API Key: {API_KEY}")
    
    # Simular uso de funciones vulnerables
    user = get_user_by_id("1")
    print(f"👤 Usuario encontrado: {user}")


if __name__ == "__main__":
    main()
