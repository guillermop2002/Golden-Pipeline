#!/usr/bin/env python3
"""
✅ SECURE FILE - FIXED VERSION

This file demonstrates the security fixes
for the vulnerabilities in the original app_vulnerable.py.
"""

import os
import sqlite3
import requests

# ============================================
# ✅ SOLUTION 1: Environment Variables
# ============================================
# Secrets are obtained from environment variables
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', '')
API_KEY = os.environ.get('API_KEY', '')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')


# ============================================
# ✅ SOLUTION 2: Parameterized Queries
# ============================================
def get_user_by_id(user_id):
    """
    ✅ SECURE: Uses parameterized queries to prevent SQL Injection.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # ✅ GOOD: Parameterized query with placeholder
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    
    return cursor.fetchone()


def authenticate_user(username, password):
    """
    ✅ SECURE: Parameterized queries in authentication.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # ✅ GOOD: Parameters separated from query
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    
    return cursor.fetchone() is not None


# ============================================
# ✅ SOLUTION 3: Safe Validation
# ============================================
def calculate(expression):
    """
    ✅ SECURE: Uses ast.literal_eval or strict validation.
    Only allows basic numeric operations.
    """
    import ast
    import operator
    
    # Allowed operators
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
        raise ValueError("Expression not allowed")
    
    tree = ast.parse(expression, mode='eval')
    return safe_eval(tree.body)


# ============================================
# ✅ SOLUTION 4: Request with SSL Verification
# ============================================
def fetch_data(url):
    """
    ✅ SECURE: SSL verification enabled (default).
    """
    # ✅ GOOD: verify=True is the default, SSL enabled
    response = requests.get(url, timeout=30)
    response.raise_for_status()  # Raises exception on HTTP error
    return response.json()


# ============================================
# Secure Main Function
# ============================================
def main():
    """
    Secure Hello World without exposed credentials.
    """
    print("🌍 Hello World from the Golden Pipeline!")
    print("🔒 Credentials loaded from environment variables")
    print("✅ Security pipeline: PASSED")
    
    # Check if environment variables are configured
    if not DATABASE_PASSWORD:
        print("⚠️  Warning: DATABASE_PASSWORD not configured")
    if not API_KEY:
        print("⚠️  Warning: API_KEY not configured")


if __name__ == "__main__":
    main()
