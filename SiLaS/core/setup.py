# Probably will not need.

from cx_Freeze import setup, Executable



# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('SiLaS.py', 'Console')
]

setup(name='SiLaS',
      version = '1.0',
      description = 'Simple Lan Server',
      options = dict(build_exe = buildOptions),
      executables = executables)
