# **Aplicación de escritorio con interfaz gráfica para cifrado y descifrado de datos**
Esteban Murcia Saavedra

>En este repositorio estará alojada la actividad 3 de la asignatura de Aplicaciones I de la maestría en inteligencia artificial


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="#descripcion-de-la-actividad">Descripción de la actividad</a>
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
        <li><a href="#python">Python</a></li>
        <li><a href="#qt-y-pyqt6">Qt y PyQt6</a></li>
        <li><a href="#qt-designer">Qt Designer</a></li>
      </ul>
    </li>
    <li><a href="#screen-diseñadas">Screen diseñadas</a></li>
    <li><a href="#funcionalidad">Funcionalidad</a></li>
    <li><a href="#conclusiones">Conclusiones</a></li>

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

Se recomienda realizar esta instalación mediante los siguientes comandos y a partir del documento <a href="requirements.txt">requirements.txt</a>:

```bash
git clone https://github.com/EstebanMS77/Maestria_IA_AplicacionI_Actividad3.git

cd Maestria_IA_AplicacionI_Actividad3
.\Entorno_Actividad3\Scripts\activate    
git checkout master
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app\__init__.py
```
El repositorio incluye un entorno virtual preconfigurado; sin embargo, debido al peso de algunas bibliotecas necesarias para el proyecto, se recomienda reinstalar las dependencias ejecutando el archivo <a href="requirements.txt">requirements.txt</a>.

En caso de no utilizar el entorno virtual proporcionado, se puede crear uno nuevo siguiendo estos pasos:

```bash
python -m venv venv

.\venv\Scripts\activate
```

### **Estructura de carpetas**

Una vez garantizado lo anterior, contará con la siguiente estructura de carpetas, en esta encontrará los archivos más relevantes:

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

### Marco Teórico

#### **Programación Orientada a Objetos (POO)**

El paradigma de Programación Orientada a Objetos (POO) permite estructurar el código en clases que representen entidades con atributos y comportamientos. Utilizar los principios de encapsulamiento, herencia, polimorfismo y abstracción para organizar el software de forma modular, reutilizable y mantenible. Modelar objetos del mundo real en componentes de software que interactúen entre sí, facilitando la extensión y el mantenimiento del código.

Ejemplo: 

```bash
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def saludar(self):
            print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    # Crear una instancia de la clase
    persona1 = Persona("Ana", 30)

    # Llamar al método
    persona1.saludar()
```

#### **Modelo-Vista-Controlador (MVC)**

El patrón de arquitectura Modelo-Vista-Controlador (MVC) para separar las responsabilidades de la aplicación en tres componentes principales:

- Modelo: Gestionar los datos, la lógica de negocio y las reglas del sistema.

- Vista: Representar la interfaz de usuario y mostrar la información mediante GUI.

- Controlador: Intermediar entre la vista y el modelo, procesando entradas del usuario y actualizando la vista o los datos según corresponda.

Adoptar esta estructura para mejorar la organización del proyecto, facilitar el desarrollo colaborativo y permitir una mayor escalabilidad.

#### **Python**

Lenguaje de programación Python por su tipado dinámico, sintaxis clara y enfoque multiparadigma. Utilizarlo para desarrollar aplicaciones de alto nivel de forma rápida y mantenible, aprovechando su amplia comunidad y ecosistema de bibliotecas especializadas. Integrar sus características con herramientas externas para desarrollar interfaces gráficas, manipulación de datos y control de lógica de negocio.

#### **Qt y PyQt6**

Utilizar Qt, un framework multiplataforma desarrollado en C++, para construir interfaces gráficas robustas y modernas. Emplear PyQt6, que actúa como binding de Qt para Python, para acceder a los módulos de Qt desde código Python. Gestionar la interfaz mediante widgets, eventos y señales/slots, permitiendo una arquitectura desacoplada y orientada a objetos.

#### **Qt Designer**

Diseñar interfaces gráficas utilizando Qt Designer, una herramienta visual que permite crear archivos .ui a través de un entorno de desarrollo gráfico. Separar el diseño visual de la lógica de negocio, permitiendo modificar la interfaz sin alterar el código funcional. Exportar los diseños a clases Python utilizando herramientas como pyuic6.


### Screen diseñadas 

En esta sección encontrará el desarrollo gráfico de las pantallas, estas compartirán con un botón de inicio, este permitirá volver a la pantalla inicial, cuando el usuario lo requiera.

1. Pestaña Inicial

    Esta es la pantalla que lanzará la app cuando se ejecute por primera vez, esta contara con la informaciondel "Hacker" encargado de desarrollar la applicación, esta contará con:

    - Boton de cifrado
    - Boton de descifrado

    <img src ="app\views\UI\resources\ScreenshotPantallaInicial.png" height="400">

2. Pestaña Cifrado

    Esta es la pantalla que permirirá el ingreso por parte del usuario con el fin de poder cifrar el código:

    <img src ="app\views\UI\resources\ScreenshotPantallaCifrado.png" height="400">

3. Pestaña Descifrado

    Esta es la pantalla que permirira el ingreso por parte del usuario con el fin de poder cifrar el codigo:

    <img src ="app\views\UI\resources\ScreenshotPantalladescifrado.png" height="400">

3. Pestaña Warning

    Esta es la pantalla que permite el control de las excepciones, en caso de que el aplicativo falle, este permitira la visualización más amigable del error:

    <img src ="app\views\UI\resources\ScreenshotPantallaWarning.png" height="400">


### Funcionalidad

En el siguiente GIF se realiza una prueba de cifrado y descifrado de unos números, donde se busca que cada uno retorne el valor esperado, ademas de lo anteror se corrobora la navegabilidad entre pantallas:

1. Funcionamiento optimo:

    <img src="app\views\UI\resources\VideoFuncionalidad.gif">



2. Funcionamiento con excepciones:

    Para este escenario se fuerza la excepcion mediante, la modificacion del codigo, dejando una funcion no funcional:

    <img  src="app\views\UI\resources\VideoNoFuncionalidad.gif">


En caso de requerir visualizar mejor estos escenarios, los videos se encontraran alojados en la carpeta de <a href="app\views\UI\resources">resources</a>



### Conclusiones

He trabajado en el desarrollo de aplicaciones en distintas plataformas como Windows Forms, Power Apps y Android Studio, cada una con enfoques y niveles de control diferentes. Actualmente, el desarrollo de software se está orientando cada vez más hacia plataformas low-code, que si bien facilitan la creación de soluciones, también reducen el nivel de control que tenemos sobre el comportamiento interno de la aplicación. Por ello, sigue siendo fundamental comprender en profundidad cómo desarrollar aplicaciones desde cero, especialmente cuando se trata de estructurar proyectos de forma ordenada.

La arquitectura MVC (Modelo-Vista-Controlador) es una de las herramientas clave para lograr esta estructuración, ya que permite dividir claramente la lógica del programa, la interfaz de usuario y el control de flujo. Esta segmentación facilita la organización del código, la reutilización de componentes y la asignación adecuada de responsabilidades. Asimismo, entender la abstracción de objetos y su representación a través de clases es un valor agregado que potencia cualquier proyecto.

Python, por su parte, es un lenguaje sumamente versátil, con una gran comunidad, una vasta colección de librerías y una sintaxis que favorece una curva de aprendizaje rápida. Aunque anteriormente no había trabajado con interfaces gráficas en Python ni profundizado demasiado en la programación orientada a objetos (POO) dentro de este lenguaje, esta actividad me permitió aplicar ambos conceptos en nuevos contextos. Sin embargo, no todo fue sencillo: por ejemplo, integrar imágenes en Qt resultó ser más complejo de lo esperado, y la falta de un widget específico para insertar imagenes, tener que utilizar un label con texto enriquecido complicó un poco más esa necesidad que deberia ser sencilla.

Tanto la programación orientada a objetos como la arquitectura MVC tienen sus propios desafíos. Comprender su funcionamiento lógico puede ser una tarea que requiere reflexión constante. Siempre surge el cuestionamiento: ¿esta funcionalidad debería pertenecer a esta clase?, ¿estamos respetando el patrón arquitectónico si un controlador ejecuta un método de la vista?, ¿no deberían las vistas limitarse únicamente a la presentación? Estos dilemas son parte del proceso. Lo interesante es que, muchas veces, cuando enfrentamos estas dudas, la propia arquitectura o el paradigma nos da pistas de que quizás estamos complicando más de lo necesario. Esa lucha por no romper las "reglas" del diseño es, en sí misma, parte del aprendizaje y del crecimiento como desarrolladores.





