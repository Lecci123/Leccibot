"""Config values will be loaded from here"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# CatUserBot #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Copyright (C) 2020-2023 by TgCatUB@Github.
# This file is part of: https://github.com/TgCatUB/catuserbot
# and is released under the "GNU v3.0 License Agreement".
# Please see: https://github.com/TgCatUB/catuserbot/blob/master/LICENSE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import os


class Config:
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOTLOG_CHATID = os.environ.get("BOTLOG_CHATID")
    STRING_SESSION = os.environ.get("STRING_SESSION")

    # Tambahan opsional lain jika dibutuhkan
    # OWNER_ID = os.environ.get("OWNER_ID")
    # DATABASE_URL = os.environ.get("DATABASE_URL")
    # dan lain-lain...
