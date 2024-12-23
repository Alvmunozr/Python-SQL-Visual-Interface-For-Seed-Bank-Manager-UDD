@echo off
:: Activa el entorno virtual
call "C:\Users\alvar\Desktop\BancoDeSemillas_UDD\.venv\Scripts\activate.bat"

:: Ejecuta el script principal
python "C:\Users\alvar\Desktop\BancoDeSemillas_UDD\main.py"

:: Desactiva el entorno virtual automáticamente al finalizar
call "C:\Users\alvar\Desktop\BancoDeSemillas_UDD\.venv\Scripts\deactivate.bat"
