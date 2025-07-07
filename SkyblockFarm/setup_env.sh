#!/usr/bin/env bash
set -e

# 1. Vérifie la présence de Python
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
  echo "Erreur : Python n'est pas installé ou n'est pas dans le PATH."
  exit 1
fi

# Utilise python3 si dispo, sinon python
PYTHON_CMD=python3
if ! command -v python3 &> /dev/null; then
  PYTHON_CMD=python
fi

# 2. Crée l'env virtuel
ENV_DIR=env
$PYTHON_CMD -m venv $ENV_DIR

# 3. Active l'env virtuel (Git Bash vs. WSL)
if [ -f "$ENV_DIR/Scripts/activate" ]; then
  source "$ENV_DIR/Scripts/activate"
elif [ -f "$ENV_DIR/bin/activate" ]; then
  source "$ENV_DIR/bin/activate"
else
  echo "Impossible de trouver le script d'activation de l'environnement."
  exit 1
fi

# 4. Met à jour pip (via python -m pip) et installe les libs
python -m pip install --upgrade pip setuptools wheel
python -m pip install keyboard mouse tk

# 5. Génère et exécute un script de test
cat > run_libs.py << 'EOF'
import time
import keyboard
import mouse
import tkinter as tk
from threading import Thread, Event

print("✅ Modules chargés avec succès !")

# Test Tkinter : fenêtre qui se ferme après 2 secondes
root = tk.Tk()
root.title("Test Tkinter")
tk.Label(root, text="Tkinter fonctionne !").pack(padx=20, pady=20)
def fermer():
    time.sleep(2)
    root.quit()
Thread(target=fermer, daemon=True).start()
root.mainloop()
EOF

python run_libs.py

echo "🎉 Environnement prêt et script de test exécuté."
