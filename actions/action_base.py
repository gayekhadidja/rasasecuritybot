import sqlite3
import logging
import json
import pathlib
import ruamel.yaml
from typing import Dict , Text , Any

logging = logging.getLogger(__name__)

here = pathlib.Path(__file__).parent.absolute()

json_headers = {
    "content-Type": "applications/json ",
    "Accept " : "application/json"
}