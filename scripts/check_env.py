
import sys
from pathlib import Path

# 1. Recupera la versione di Python
version = sys.version_info
python_version = f"{version.major}.{version.minor}.{version.micro}"

# 2. Recupera il percorso dell'interprete
interpreter_path = sys.executable

# 3. Controlla se un ambiente virtuale è attivo
venv_active = sys.prefix != sys.base_prefix

# 4. Recupera il percorso del venv, se attivo
if venv_active:
    venv_path = Path(sys.prefix)
else:
    venv_path = None

# 5. Stampa i risultati
print(f"Versione Python: {python_version}")
print(f"Interprete Python: {interpreter_path}")
print(f"Ambiente virtuale attivo: {'sì' if venv_active else 'no'}")

if venv_active:
    print(f"Cartella ambiente virtuale: {venv_path}")
