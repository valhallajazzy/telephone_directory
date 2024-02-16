import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
path = os.getenv("PATH_TO_FOLDER", default=Path.cwd() / 'database')
