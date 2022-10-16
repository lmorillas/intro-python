
---
title: "Jupyter"
linkTitle: "Jupyter"
weight: 10
date: 2021-09-15
description: >
  Instalación del entorno de aprendizaje

mirar: >
  * https://github.com/jerry-git/learn-python3
  * https://gitlab.erc.monash.edu.au/andrease/Python4Maths/tree/master
  * https://github.com/rajathkmp/Python-Lectures
  * https://github.com/jakevdp/WhirlwindTourOfPython
  * https://jupyter4edu.github.io/jupyter-edu-book/
  * https://github.com/BabaMalik/Coding-Ninjas-Introduction-to-Python
  * https://github.com/estimand/python-programming-101
  * https://python.awesome-programming.com/en/awesome/gh-100021/python-education
  * https://github.com/martinepalazzo/primeros_pasos_python
  * https://docs.microsoft.com/es-es/azure/machine-learning/how-to-configure-environment#jupyter
  * 
---

{{% pageinfo %}}
### Objetivos:
* Introducción a Google Colab
* Uso de notebooks en Visual Studio Code
* Instalación local de Jupyter para usar los notebooks de clase
{{% /pageinfo %}}

## Uso en Visual Studio Code

https://code.visualstudio.com/docs/datascience/jupyter-notebooks

## Google Colaboratory

https://research.google.com/colaboratory/faq.html

{{% pageinfo color="secondary" %}}
Colaboratory, también llamado Colab, es un producto de Google Research. Colab permite que todos puedan escribir y ejecutar código arbitrario de Python en el navegador. Es ideal para aplicarlo en proyectos de aprendizaje automático, análisis de datos y educación. En términos técnicos, Colab es un servicio de notebooks de Jupyter alojados que no requiere instalación para usarlo y brinda acceso sin costo a recursos computacionales, incluidas GPU.
{{% /pageinfo %}}

### Ejercicio

* Abre https://colab.research.google.com/notebooks/intro.ipynb
* Copialo en tu Drive para poderlo modificar
* Añade una celda debajo de los segundos de una semana y escribe el código para calcular los segundos de un mes (este mes)


## Instalación local

``` bash
# Crea una nueva carpeta y entra en ella
mkdir intro-python    
cd intro-python

# Crea un entorno virtual y actívalo
$ python3 -m venv venv
$ source venv/bin/activate

# En windows:
C:\> env\Scripts\activate.bat

# Instala jupyter
$ pip install jupyter

# Ejecuta jupyter
$ jupyter notebook

# Esto abrirá una ventana en tu navegador en el puerto 8888
```

