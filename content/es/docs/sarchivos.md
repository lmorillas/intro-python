
---
title: "Sistema de archivos"
linkTitle: "Sistema de archivos"
weight: 45
date: 2021-09-15
description: >
  Archivos

---

{{% pageinfo %}}
### Objetivos:
* Archivos y directorios
* Windows y linux
{{% /pageinfo %}}


# Gestión de archivos y directorios

### Linux and Windows Paths

En windows y linux, los directorios se separan de forma diferente. En windows, se usa `\` y en linux, se usa `/`. Por ejemplo, en windows, el directorio `C:\Users\joe`  en linux `/home/joe` 

Tenemos que usar `os.path.join`

```python
>>> import os

>>> os.path.join('usr', 'bin', 'spam')
# 'usr\\bin\\spam'
```

o `pathlib` 

```python
>>> from pathlib import Path

>>> print(Path('usr').joinpath('bin').joinpath('spam'))
# usr/bin/spam
```

Ejemplo en Windows:

```python
>>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']

>>> for filename in my_files:
...     print(os.path.join('C:\\Users\\asweigart', filename))
...
# C:\Users\asweigart\accounts.txt
# C:\Users\asweigart\details.csv
# C:\Users\asweigart\invite.docx
```

## The current working directory


```python
>>> import os

>>> os.getcwd()
# 'C:\\Python34'
>>> os.chdir('C:\\Windows\\System32')

>>> os.getcwd()
# 'C:\\Windows\\System32'
```

En linux 

```python
>>> from pathlib import Path
>>> from os import chdir

>>> print(Path.cwd())
# /home/asweigart

>>> chdir('/usr/lib/python3.6')
>>> print(Path.cwd())
# /usr/lib/python3.6
```

## Crear carpetas


```python
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')
```

```python
>>> from pathlib import Path
>>> cwd = Path.cwd()
>>> (cwd / 'delicious' / 'walnut' / 'waffles').mkdir(parents=True)
```

## Validar rutas y archivos

### Existe el archivo o directorio?


```python
>>> import os

>>> os.path.exists('.')
# True

>>> os.path.exists('setup.py')
# True

>>> os.path.exists('/etc')
# True

>>> os.path.exists('nonexistentfile')
# False
```

```python
from pathlib import Path

>>> Path('.').exists()
# True

>>> Path('setup.py').exists()
# True

>>> Path('/etc').exists()
# True

>>> Path('nonexistentfile').exists()
# False
```

### Comprobando si es un archivo


```python
>>> import os

>>> os.path.isfile('setup.py')
# True

>>> os.path.isfile('/home')
# False

>>> os.path.isfile('nonexistentfile')
# False
```


### O si es directorio


```python
>>> import os

>>> os.path.isdir('/')
# True

>>> os.path.isdir('setup.py')
# False

>>> os.path.isdir('/spam')
# False
```



```python
>>> from pathlib import Path

>>> Path('/').is_dir()
# True

>>> Path('setup.py').is_dir()
# False

>>> Path('/spam').is_dir()
# False
```

## Tamaño de un archivo en bytes


```python
>>> import os

>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
# 776192
```

## Listar directorios

```python
>>> import os

>>> os.listdir('C:\\Windows\\System32')
# ['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
# --snip--
# 'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']
```


```python
>>> from pathlib import Path

>>> for f in Path('/usr/bin').iterdir():
...     print(f)
...
# ...
# /usr/bin/tiff2rgba
# /usr/bin/iconv
# /usr/bin/ldd
# /usr/bin/cache_restore
# /usr/bin/udiskie
# /usr/bin/unix2dos
# /usr/bin/t1reencode
# /usr/bin/epstopdf
# /usr/bin/idle3
# ...
```

### Tamaño de un directorio

```python
>>> import os
>>> total_size = 0

>>> for filename in os.listdir('C:\\Windows\\System32'):
...     total_size = total_size + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
...
>>> print(total_size)
# 1117846456
```

## Copiar archivos y carpetas


```python
>>> import shutil, os

>>> os.chdir('C:\\')
>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
# C:\\delicious\\spam.txt'

>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
# 'C:\\delicious\\eggs2.txt'
```


```python
>>> import shutil, os

>>> os.chdir('C:\\')
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
# 'C:\\bacon_backup'
```

## Mover y renombrar

```python
>>> import shutil

>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
# 'C:\\eggs\\bacon.txt'
```

```python
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
# 'C:\\eggs\\new_bacon.txt'
```

## Eliminar archivos y carpetas

- Calling `os.unlink(path)` or `Path.unlink()` will delete the file at path.

- Calling `os.rmdir(path)` or `Path.rmdir()` will delete the folder at path. This folder must be empty of any files or folders.

- Calling `shutil.rmtree(path)` will remove the folder at path, and all files and folders it contains will also be deleted.

## Archivos zip

* https://docs.python.org/3/library/zipfile.html
* https://realpython.com/python-zipfile/

```python
>>> import zipfile

>>> with zipfile.ZipFile("sample.zip", mode="r") as archive:
        archive.printdir()   # listado
        archive.getinfo("file.txt")  # info de un archivo
        archive.extractall()  # extraer todo
```


