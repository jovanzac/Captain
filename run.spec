# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


added_files = [
    ('C:\\Users\\jovan\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\pygame','pygame')
]


a = Analysis(['run.py'],
             pathex=['C:\\Jovan\\Captain!!Project\\Captain_repo'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
