import logging
from logging.handlers import RotatingFileHandler
import os
import locale
from datetime import datetime


def setup_logger():
    # Intentar establecer locale en español, pero sin romper si no existe
    try:
        # Primero probar con es_ES.UTF-8 (Linux)
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    except locale.Error:
        try:
            # Probar con es_ES genérico (a veces existe)
            locale.setlocale(locale.LC_ALL, 'es_ES')
        except locale.Error:
            # Último recurso: locale por defecto del sistema
            locale.setlocale(locale.LC_ALL, '')

    # Ruta del log
    log_dir = os.getenv("LOG_DIR", ".")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, "wallbot.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        handlers=[
            RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=10),
            logging.StreamHandler()
        ]
    )

    logging.info("Logger inicializado")
