# **Aplicación de escritorio con interfaz gráfica para cifrado y descifrado de datos**
Esteban Murcia Saavedra

>En este repositorio estara alojada la actividad 3 de la asignatura de Aplicaciones I de la maestria en inteligencia artificial


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="#descripcion-de-la-actividad">Descripcion de la actividad</a>
      <ul>
        <li><a href="#requerimientos-de-la-actividad">Requerimientos de la actividad</a></li>
      </ul>
    </li>    
    <li>
      <a href="#desarrollo-de-la-actividad">Desarrollo de la actividad</a>
      <ul>
        <li><a href="#requerimientos">Requerimientos</a></li>
        <li><a href="#instalacion">Instalacion</a></li>
      </ul>
    </li>
    <li><a href="#estructura-de-carpetas">Estructura de carpetas</a></li>
    <li><a href="#marco-teorico">Marco Teorico</a>
        <ul>
        <li><a href="#programación-orientada-a-objetos-poo">Programación Orientada a Objetos (POO)</a></li>
        <li><a href="#modelo-vista-controlador-mvc">Modelo-Vista-Controlador (MVC)</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## **Descripcion de la actividad**

Desarrollar una aplicación de escritorio con interfaz gráfica en Python, utilizando Tkinter, PyQt5 o PyQt6. Aplicar buenas prácticas de programación y diseño de interfaces para construir una solución funcional que permita cifrar y descifrar datos de manera eficiente. Implementar validación de entradas, manejo de eventos y una estructura de código modular, garantizando usabilidad y rendimiento en la aplicación final.

### Requerimientos de la actividad

1. Ventana principal

    - Mostrar información del autor (nombre, código estudiantil).

    - Incluir dos botones funcionales para navegar a las ventanas de cifrado y descifrado.

2. Ventana de cifrado

    - Permitir el ingreso de un número entero de exactamente 6 dígitos.

    - Implementar el algoritmo de cifrado:

        - Sumar 7 a cada dígito y calcular el módulo 10.

        - Intercambiar posiciones (1°↔3°, 2°↔4°, 5°↔6°).

    - Mostrar el resultado cifrado en la interfaz.

3. Ventana de descifrado

    - Permitir el ingreso de un número cifrado de 6 dígitos.

    - Revertir el proceso de cifrado:

        - Intercambiar posiciones (1°↔3°, 2°↔4°, 5°↔6°).

        - Restar 7 a cada dígito y aplicar módulo 10.

    - Mostrar el número original descifrado.

## **Desarrollo de la actividad**

Esta aplicación ha sido desarrollada utilizando el lenguaje de programación <a href="https://www.python.org/">Python</a>, con una interfaz gráfica construida mediante <a href="https://doc.qt.io/qtforpython-6/">PyQt6</a> y <a href="https://doc.qt.io/qtforpython-6/tools/pyside-designer.html#pyside6-designer">Qt Widgets Designer</a>. Su arquitectura se basa en el patrón de diseño MVC (Modelo-Vista-Controlador), y su implementación sigue el paradigma de programación orientada a objetos (POO), lo que permite una estructura modular, escalable y fácil de mantener.

### Requerimientos
Antes de entrar en materia y en conceptos, se requiere un ambiente con:

```markdown
contourpy==1.3.2
cycler==0.12.1
fonttools==4.57.0
git-filter-repo==2.47.0
kiwisolver==1.4.8
matplotlib==3.10.3
numpy==2.2.5
packaging==25.0
pandas==2.2.3
pillow==11.2.1
pyparsing==3.2.3
PyQt6==6.9.0
PyQt6-Qt6==6.9.0
PyQt6_sip==13.10.0
PySide6==6.9.0
PySide6_Addons==6.9.0
PySide6_Essentials==6.9.0
python-dateutil==2.9.0.post0
pytz==2025.2
setuptools==80.4.0
shiboken6==6.9.0
six==1.17.0
tzdata==2025.2
wheel==0.45.1
```

### Instalacion

Se recomienda realizar esta instalacion mediante los siguientes comandos y apartir del documento <a href="requirements.txt">requirements.txt</a>:

```bash
git clone https://github.com/EstebanMS77/Maestria_IA_AplicacionI_Actividad3.git

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app\__init__.py
```
El repositorio incluye un entorno virtual preconfigurado; sin embargo,Debido al peso de algunas bibliotecas necesarias para el proyecto, se recomienda reinstalar las dependencias ejecutando el archivo <a href="requirements.txt">requirements.txt</a>.

En caso de no utilizar el entorno virtual proporcionado, se puede crear uno nuevo siguiendo estos pasos:

```bash
python -m venv venv

.\venv\Scripts\activate
```

### **Estructura de carpetas**

Una vez garantizado lo anterior, contara con la siguiente estructura de carpetas, en esta encontrara los archivos más relevantes:

```bash
Actividad3/
├── README.md
├── .gitattributes
├── requirements.txt
├── Entorno_Actividad3/                
├── app/                    # Código fuente principal
│   ├── __init__.py         # Archivo principal
│   ├── models/             # Lógica de datos
│   │   └── Model.py
│   ├── views/              # Interfaz gráfica (Qt Designer .ui o código generado)
│   │   └── View_Cifrado.py
│   │   └── View_Descifrado.py
│   │   └── View_Inicial.py
│   │   └── View_Warning.py
│   │   └── UI/             
│   │   │   └── View_Warning.ui
│   │   │   └── View_Inicio.ui
│   │   │   └── View_Decepcriptar.ui
│   │   │   └── View_Cifrado.ui
│   │   │   └── resources/
│   └── controllers/       # Lógica de control
│       └── controler.py 
```

### Marco Teorico

#### **Programación Orientada a Objetos (POO)**

    El paradigma de Programación Orientada a Objetos (POO) permite estructurar el código en clases que representen entidades con atributos y comportamientos. Utilizar los principios de encapsulamiento, herencia, polimorfismo y abstracción para organizar el software de forma modular, reutilizable y mantenible. Modelar objetos del mundo real en componentes de software que interactúen entre sí, facilitando la extensión y el mantenimiento del código.

    Ejemplo: 

    ```bash
        ## Librerias requeridas para la vista inicial
        import sys
        from PyQt6 import uic 
        from PyQt6.QtWidgets import *
        from PyQt6.QtGui import *
        from views.UI import resources
        from PyQt6.QtCore import pyqtSignal

        ##Definicion de la clase View_Inicial
        class View_Warning(QMainWindow):

            #   #Propiedades de la clase
            PathFile_ViewWarning = r"app\views\UI\View_Warning.ui"
            PathFile_ViewIcon = r"app\views\UI\resources\cyber-criminal.png"
            Sig_Btn_Clicked_Inicio = pyqtSignal() 

            ## Constructor de la clase
            def __init__(self):  
            super().__init__()
            uic.loadUi(self.PathFile_ViewWarning, self)
            self.setWindowIcon(QIcon(self.PathFile_ViewIcon))
            self.Label_Error = self.findChild(QLabel,"Label_Error")

            self.Btn_Inicio = self.findChild(QPushButton, "Button_Inicio") 
            self.Btn_Inicio.clicked.connect(self._Enviar_Btn_Inicio)


            def Write_Error(self,Str_Error):      

            self.Label_Error.setText(Str_Error)

            def _Enviar_Btn_Inicio(self):
            self.Sig_Btn_Clicked_Inicio.emit()
    ```

#### **Modelo-Vista-Controlador (MVC)**

    El patrón de arquitectura Modelo-Vista-Controlador (MVC) para separar las responsabilidades de la aplicación en tres componentes principales:

        - Modelo: Gestionar los datos, la lógica de negocio y las reglas del sistema.

        - Vista: Representar la interfaz de usuario y mostrar la información mediante GUI.

        - Controlador: Intermediar entre la vista y el modelo, procesando entradas del usuario y actualizando la vista o los datos según corresponda.

Adoptar esta estructura para mejorar la organización del proyecto, facilitar el desarrollo colaborativo y permitir una mayor escalabilidad.






