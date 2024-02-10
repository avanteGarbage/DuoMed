import os
from aqt import mw
from . import answer_buttons
from .answer_effects import *

addon_path = os.path.dirname(__file__)
user_files = os.path.join(addon_path, "user_files")
config = mw.addonManager.getConfig(__name__)
