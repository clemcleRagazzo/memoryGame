# memoryGame

Reçois un nombre le matin, retiens-le, et ressors-le le soir

Pour lancer la conversion en binaire :

```bash
python -m nuitka --standalone  --include-data-dir=assets=assets --windows-icon-from-ico=assets/img/logo.ico  --output-filename=memoryGame.exe --output-dir=dist --lto=yes --jobs=8 main.py
```
