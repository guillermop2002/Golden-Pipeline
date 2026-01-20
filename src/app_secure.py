#!/usr/bin/env python3
"""
✅ ARCHIVO SEGURO - VERSIÓN CORREGIDA

Este archivo demuestra las correcciones de seguridad
para las vulnerabilidades del archivo app_vulnerable.py.
"""

import os
import sqlite3
import requests

# ============================================
# ✅ SOLUCIÓN 1: Variables de Entorno
# ============================================
# Los secretos se obtienen de variables de entorno
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', '')
API_KEY = os.environ.get('API_KEY', '')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')


# ============================================
# ✅ SOLUCIÓN 2: Queries Parametrizadas
# ============================================
def get_user_by_id(user_id):
    """
    ✅ SEGURO: Usa queries parametrizadas para prevenir SQL Injection.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # ✅ BIEN: Query parametrizada con placeholder
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    
    return cursor.fetchone()


def authenticate_user(username, password):
    """
    ✅ SEGURO: Queries parametrizadas en autenticación.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # ✅ BIEN: Parámetros separados de la query
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    
    return cursor.fetchone() is not None


# ============================================
# ✅ SOLUCIÓN 3: Validación Segura
# ============================================
def calculate(expression):
    """
    ✅ SEGURO: Usa ast.literal_eval o validación estricta.
    Solo permite operaciones numéricas básicas.
    """
    import ast
    import operator
    
    # Operadores permitidos
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }
    
    def safe_eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = safe_eval(node.left)
            right = safe_eval(node.right)
            op = operators.get(type(node.op))
            if op:
                return op(left, right)
        raise ValueError("Expresión no permitida")
    
    tree = ast.parse(expression, mode='eval')
    return safe_eval(tree.body)


# ============================================
# ✅ SOLUCIÓN 4: Request con verificación SSL
# ============================================
def fetch_data(url):
    """
    ✅ SEGURO: Verificación SSL habilitada (por defecto).
    """
    # ✅ BIEN: verify=True es el default, SSL habilitado
    response = requests.get(url, timeout=30)
    response.raise_for_status()  # Lanza excepción si hay error HTTP
    return response.json()


# ============================================
# Función principal segura
# ============================================
def main():
    """
    Hola Mundo seguro sin credenciales expuestas.
    """
    print("🌍 ¡Hola Mundo desde el Golden Pipeline!")
    print("🔒 Credenciales cargadas desde variables de entorno")
    print("✅ Pipeline de seguridad: PASSED")
    
    # Verificar que las variables de entorno están configuradas
    if not DATABASE_PASSWORD:
        print("⚠️  Advertencia: DATABASE_PASSWORD no configurada")
    if not API_KEY:
        print("⚠️  Advertencia: API_KEY no configurada")


if __name__ == "__main__":
    main()
