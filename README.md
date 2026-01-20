# 🛡️ Golden Pipeline - Security as Code Demo

![Security Pipeline](https://img.shields.io/badge/Security-Pipeline-green?style=for-the-badge&logo=github-actions)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Gitleaks](https://img.shields.io/badge/Gitleaks-Enabled-red?style=for-the-badge)
![Semgrep](https://img.shields.io/badge/Semgrep-SAST-purple?style=for-the-badge)

## 🎯 Objetivo

Este repositorio demuestra la implementación de un **pipeline CI/CD seguro** utilizando GitHub Actions. El objetivo es detectar y **bloquear automáticamente** código vulnerable antes de que llegue a producción.

## 🔒 Herramientas de Seguridad Integradas

| Herramienta | Propósito | Tipo |
|-------------|-----------|------|
| **Gitleaks** | Detecta secretos y contraseñas hardcodeadas | Secret Detection |
| **Semgrep** | Análisis estático de código (SAST) | Code Analysis |

## 🚀 Flujo del Pipeline

```mermaid
graph LR
    A[Push Code] --> B[GitHub Actions]
    B --> C[Gitleaks Scan]
    B --> D[Semgrep SAST]
    C --> E{Secrets Found?}
    D --> F{Vulnerabilities?}
    E -->|Yes| G[❌ Block Merge]
    E -->|No| H[✅ Pass]
    F -->|Yes| G
    F -->|No| H
```

## 📁 Estructura del Proyecto

```
Golden-Pipeline/
├── .github/
│   └── workflows/
│       └── security-pipeline.yml    # Pipeline de seguridad
├── src/
│   ├── app_vulnerable.py            # ⚠️ Código vulnerable (demo)
│   └── app_secure.py                # ✅ Código seguro (solución)
├── .gitleaks.toml                   # Configuración de Gitleaks
├── .semgrepignore                   # Exclusiones de Semgrep
└── README.md
```

## ⚠️ Vulnerabilidades Intencionadas (Demo)

El archivo `src/app_vulnerable.py` contiene vulnerabilidades **intencionadas** para demostrar el funcionamiento del pipeline:

1. **🔑 Secreto Hardcodeado**: Contraseña en texto plano
2. **💉 SQL Injection**: Query vulnerable a inyección
3. **🔓 Credenciales de API**: API key expuesta

## 🧪 Cómo Probar

### 1. Hacer push con código vulnerable
```bash
git add .
git commit -m "feat: add vulnerable code for testing"
git push origin main
```

### 2. Ver el pipeline fallar
- Ve a la pestaña **Actions** en GitHub
- Observa cómo el pipeline detecta las vulnerabilidades
- **Screenshot perfecto para tu portfolio!** 📸

### 3. Arreglar y ver el pipeline pasar
```bash
# Usa app_secure.py como referencia
git add .
git commit -m "fix: remove hardcoded secrets and SQL injection"
git push origin main
```

## 📸 Capturas para Portfolio

1. **Pipeline Fallido (Rojo)**: Actions > Security Pipeline > Ver logs de error
2. **Detección de Secretos**: Logs de Gitleaks mostrando el secreto encontrado
3. **Detección de SQLi**: Logs de Semgrep mostrando la vulnerabilidad
4. **Pipeline Exitoso (Verde)**: Después de arreglar el código

## 🏆 Skills Demostradas

- ✅ Security as Code
- ✅ CI/CD con GitHub Actions
- ✅ Análisis Estático de Código (SAST)
- ✅ Detección de Secretos
- ✅ DevSecOps Best Practices
- ✅ Shift-Left Security

## 📚 Recursos

- [Gitleaks Documentation](https://github.com/gitleaks/gitleaks)
- [Semgrep Documentation](https://semgrep.dev/docs/)
- [GitHub Actions Security](https://docs.github.com/en/actions/security-guides)

---

**Autor:** Guillermo  
**Propósito:** Portfolio de Ciberseguridad/DevSecOps  
**Licencia:** MIT
