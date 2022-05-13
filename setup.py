import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os', 'selenium', 'PIL'], 'excludes': ['tkinter']}

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Medição de internet',
    vesion='1.0',
    description='Entrar em sites de medição de velocidade de internet e tirar print para futura geração de relátorios',
    options={'build.exe': build_exe_options},
    executables=[Executable('main.py', base=base)]
)
