from . import base, dark, light, solarized
from .base import themes

root = None

def init(root, theme: str = ""):
	for name, cls in themes.items():
		themes[name] = cls(root)
	themes["base"].create_fonts()
	if theme:
		themes[theme].apply()

def select_theme(name: str):
	if name not in themes:
		raise ValueError(f"theme {name} does not exist")
	themes[name].apply()
