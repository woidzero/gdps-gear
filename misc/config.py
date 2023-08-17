"""
GDPSGear
~~~~~~~~~~~~~~~~~~~
Discord bot for managing Geometry Dash IOCore based private servers

:copyright: (c) 2023 woidzero
:license: MIT, see LICENSE for more details.
"""
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

CONFIG = {
    "token": os.getenv("TOKEN"),
    "owner_id": os.getenv("OWNER_ID"),
    "gdps_api": os.getenv("GDPS_API"),
    "prefix": os.getenv("PREFIX"),
}
