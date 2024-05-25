# Generador de Presupuestos en PDF

Este proyecto es una aplicación para generar presupuestos en formato PDF. Está programado en un solo archivo Python llamado "main.py", el cual contiene toda la lógica e información sobre la interfaz gráfica de la aplicación.

## Recursos Utilizados

La aplicación utiliza los siguientes recursos:

- **Tkinter:** Biblioteca para la interfaz gráfica.
- **WeasyPrint:** Herramienta para transformar código HTML en PDF.
- **PyInstaller:** Utilizado para compilar el programa en un ejecutable.

Para instalar los recursos necesarios, puedes ejecutar el siguiente comando:

```bash
pip install tk weasyprint pyinstaller
```

## Ejecución de la Aplicación

### Prueba de Funcionamiento

Si deseas probar el funcionamiento de la aplicación, puedes ejecutarla desde el directorio raíz usando el siguiente comando:

```bash
python main.py
```

### Compilación del Programa

Para compilar el programa en un ejecutable, utiliza el siguiente comando:

```bash
pyinstaller --onefile "--name=SM Presupuestos" --icon=media/autorojo.ico main.py
```

## Recomendaciones

Se recomienda utilizar la versión más reciente y estable de cada recurso para evitar posibles conflictos. Actualmente, la aplicación está siendo ejecutada con la siguiente configuración:

- **Python:** 3.12.2
- **Tkinter:** 8.6.13
- **WeasyPrint:** 61.1
- **PyInstaller:** 6.7.0

---
