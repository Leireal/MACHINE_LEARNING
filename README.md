# 🛠️ MANTENIMIENTO PREDICTIVO EN MOTORES DE AVIÓN_ MACHINE LEARNING
## DESCRIPCIÓN
### 1. **Definición**

El **mantenimiento predictivo** es una metodología de gestión de mantenimiento basada en el estado real del sistema, que utiliza técnicas de **monitorización continua, análisis de datos, inteligencia artificial (IA)** y **modelos estadísticos** para anticipar la degradación o el fallo potencial de componentes críticos. A diferencia del mantenimiento preventivo (basado en tiempo o ciclos), el predictivo permite **intervenir justo antes de que ocurra un fallo**, reduciendo riesgos operacionales y optimizando recursos.

---

### 2. **Principios Fundamentales**

Este tipo de mantenimiento se basa en el paradigma de **Condition-Based Maintenance (CBM)**, y su evolución hacia el **Predictive Maintenance (PdM)** implica no solo evaluar la condición actual, sino **predecir el comportamiento futuro** del componente o sistema en cuestión. Esto se logra mediante:

* **Sensorización** extensiva del avión.
* **Telemetría en tiempo real** o almacenamiento en línea de vuelo.
* **Análisis histórico y contextual** del comportamiento del sistema.
* **Modelos de pronóstico** que estiman el tiempo restante antes de un fallo (Remaining Useful Life, RUL).

---

### 3. **Arquitectura Funcional del Mantenimiento Predictivo**

#### a. **Captura de Datos**

Los aviones modernos están equipados con centenares de sensores distribuidos en sistemas como:

* Motores (temperaturas de entrada y salida, vibraciones, presión de aceite, EGT)
* Sistema hidráulico (flujo, presión, fugas)
* Tren de aterrizaje (fatiga estructural, sensores de carga)
* Frenos y neumáticos (desgaste, temperatura)
* Sistema eléctrico y APU (ciclos de carga, niveles de voltaje)
* Superficies de control y actuadores (resistencia, posición, tiempo de respuesta)

#### b. **Transmisión y almacenamiento**

Los datos generados se procesan de diferentes maneras:

* **ACMS (Aircraft Condition Monitoring System)**: recopila y analiza datos abordo.
* **ACARS (Aircraft Communications Addressing and Reporting System)**: envía datos clave en vuelo.
* **FOMAX, QAR y DAR**: registradores de vuelo que almacenan datos para análisis post-vuelo.
* **Plataformas basadas en la nube**, como *Airbus Skywise*, *Boeing AnalytX* o *GE Predix*, que permiten el análisis masivo de flotas.

#### c. **Análisis Predictivo**

A través de modelos **data-driven** (IA, machine learning, redes neuronales) o **modelos físicos** (basados en ecuaciones de desgaste, fatiga o termodinámica), se predice:

* Degradación progresiva
* Patrones anómalos
* Eventos previos a fallas (precursors)

Se calcula el **RUL** y se emiten **alertas inteligentes** para programar intervenciones.

---

### 4. **Aplicaciones Específicas**

| Sistema                         | Ejemplo de Predicción                                                           |
| ------------------------------- | ------------------------------------------------------------------------------- |
| Motores  |                      Predicción de desgaste en rodamientos y eficiencia de compresores               |
| APU                             | Identificación de pérdidas de rendimiento por obstrucción o fallas electrónicas |
| Neumáticos y frenos             | Desgaste no uniforme, sobrecalentamiento o fallos hidráulicos                   |
| Superficies de control          | Fallo incipiente en actuadores electrohidráulicos (FBW)                         |
| Sistema eléctrico               | Fallo de generadores, baterías o transformadores                                |

---

### 5. **Ventajas del Mantenimiento Predictivo**

* 🔧 **Reducción de MRO no planificado** (Maintenance, Repair & Overhaul)
* 📈 **Incremento en la disponibilidad operativa**
* 💸 **Disminución de costos por mantenimiento excesivo o innecesario**
* 📉 **Reducción de AOG (Aircraft on Ground)**
* 🛡️ **Mejora de la seguridad operacional**
* 🌱 **Impacto ambiental reducido** (al evitar piezas cambiadas prematuramente)

---

### 6. **Limitaciones y Retos**

* **Alta inversión inicial**: Sensores, conectividad, software y capacitación.
* **Complejidad en la integración** de datos provenientes de distintos OEMs y subsistemas.
* **Calibración de algoritmos predictivos**: Necesidad de grandes volúmenes de datos históricos para lograr precisión.
* **Falsos positivos/negativos**: Riesgo de intervenir innecesariamente o no actuar a tiempo.
* **Regulación aeronáutica**: Las estrategias predictivas deben cumplir con normativas de la FAA, EASA, etc.

---

### 7. **Futuro del Mantenimiento Predictivo**

Con el avance de la **inteligencia artificial generativa**, el **edge computing**, y el **gemelo digital (digital twin)**, el mantenimiento predictivo evoluciona hacia una estrategia aún más autónoma, donde:

* Se podrá **simular en tiempo real el estado de cada componente**.
* Se integrarán fuentes externas como clima, rutas o historial del piloto.
* Habrá una colaboración más estrecha entre **aerolíneas, fabricantes y talleres MRO**, compartiendo datos de manera segura para beneficio común.


## DATOS OBTENIDOS

DATASET_1:  Parámetros de motores de aviones. Para simplificar, los nombres de las variables están codificados con una letra y un número. ​

​
Los datos son de 100 motores de avion y para cada uno se dan una serie de ciclos hasta que falla.​

Cada fila representa un ciclo de operación de un motor, con un total de 26 columnas numéricas (variables).​

​

20631 filas × 26 columnas​

​

DATASET_2:  En que ciclo se da el fallo en cada motor.​

​

100 filas × 2 columnas

### DATASET_1
Se dispone de un set de datos sobre diferentes parametros de motores de aviones. Para simplificar, los nombres de las variables estan codificados con una letra y un numero. Seguidamente se muestra una tabla donde se describe cada uno.

Los datos son de 100 motores de avion y para cada uno se dan una serie de ciclos hasta que falla.
Cada fila representa un ciclo de operación de un motor, con un total de 26 columnas numéricas (variables).

 Variable   | Inglés                         | Español                                                    |
| ---------- | ------------------------------ | ---------------------------------------------------------- |
| `id`       | Engine ID                      | ID del motor                                               |
| `cycle`    | Time cycle / operating cycle   | Ciclo de operación                                         |
| `setting1` | Operational setting 1          | Parámetro operativo 1                                      |
| `setting2` | Operational setting 2          | Parámetro operativo 2                                      |
| `setting3` | Operational setting 3          | Parámetro operativo 3                                      |
| `s1`       | Total temperature at fan inlet | Tempe|ratura total en la entrada del ventilador             |
| `s2`       | LPC outlet temperature         | Temperatura a la salida del compresor de baja presión      |
| `s3`       | HPC outlet temperature         | Temperatura a la salida del compresor de alta presión      |
| `s4`       | LPT outlet temperature         | Temperatura a la salida de la turbina de baja presión      |
| `s5`       | Fan inlet pressure             | Presión en la entrada del ventilador                       |
| `s6`       | Bypass-duct pressure           | Presión en el conducto de derivación (bypass)              |
| `s7`       | HPC outlet pressure            | Presión a la salida del compresor de alta presión          |
| `s8`       | Physical fan speed             | Velocidad física del ventilador                            |
| `s9`       | Physical core speed            | Velocidad física del núcleo                                |
| `s10`      | Engine pressure ratio          | Relación de presión del motor                              |
| `s11`      | Static pressure at HPC outlet  | Presión estática a la salida del compresor de alta presión |
| `s12`      | Fuel flow / Ps30               | Flujo de combustible relativo a Ps30                       |
| `s13`      | Corrected fan speed            | Velocidad corregida del ventilador                         |
| `s14`      | Corrected core speed           | Velocidad corregida del núcleo                             |
| `s15`      | Bypass ratio                   | Relación de bypass                                         |
| `s16`      | Burner fuel-air ratio          | Relación combustible-aire del quemador                     |
| `s17`      | Bleed enthalpy                 | Entalpía del sangrado                                      |
| `s18`      | Demanded fan speed             | Velocidad deseada del ventilador                           |
| `s19`      | Demanded corrected core speed  | Velocidad corregida deseada del núcleo                     |
| `s20`      | HPT coolant bleed              | Flujo de refrigerante en la turbina de alta presión        |
| `s21`      | LPT coolant bleed              | Flujo de refrigerante en la turbina de baja presión        |




NOTA: El sangrado de aire (bleed air) en un motor de avión se refiere al aire extraído del compresor de un motor a reacción para diversos fines, como la presurización y climatización de la cabina, el deshielo de las alas y la operación de sistemas auxiliares. Este aire, que se toma a alta temperatura y presión, se utiliza para alimentar estos sistemas en lugar de ser utilizado directamente para la propulsión.  

### DATASET_2

Se extraen los datos de este segundo csv y se comprueba que en cada id, osea en cada motor, los fallos se dan en diferentes ciclos.


