"""
GDPSGear
~~~~~~~~~~~~~~~~~~~
Discord bot for managing Geometry Dash IOCore based private servers

:copyright: (c) 2023 woidzero
:license: MIT, see LICENSE for more details.
"""


def fetch_rank(rank) -> str:
    if rank == 1:
        return f"<:r:962415984671613009> {rank}"
    elif rank <= 10:
        return f"<:r:962416638811045918> {rank}"
    elif rank <= 50:
        return f"<:r:962415987494359060> {rank}"
    elif rank >= 100:
        return f"<:r:962415984831000646> {rank}"
    else:
        return rank


def fetch_role(role) -> str:
    if role == "Owner":
        role = "<:r:934856675331014699> OWNER"
    if role == "Elder Moderator":
        role = "<:r:960552165666062446> ELDER MODERATOR"
    if role == "Moderator":
        role = "<:r:934846351722811474> MODERATOR"
    else:
        return None
