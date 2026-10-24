# todos los tests d un saque
python -m mypy arimaa.py
python -m coverage run --include arimaa.py --branch -m unittest tests.py && python -m coverage json && python cubrimiento.py
