# -*- mode: python -*-
a = Analysis(['SiLaS.py'],
             pathex=['/home/owner/workspaces/SiLaS_WS2/SiLaS/core'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='SiLaS',
          debug=False,
          strip=True,
          upx=True,
          console=True )
