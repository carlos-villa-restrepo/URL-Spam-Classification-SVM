# 🛡️ Detector de URLs Spam (SVM)
"Este proyecto consiste en el despliegue de un modelo de clasificación mediante una aplicación web interactiva desarrollada con Streamlit. El núcleo del proyecto es un sistema de NLP basado en Aprendizaje Supervisado, que utiliza un algoritmo de Support Vector Machine (SVM) para identificar y clasificar URLs como seguras o potenciales SPAM."


## 🚀 Funcionalidades

* **Análisis en tiempo real:** Introduce cualquier URL y obtén una respuesta inmediata.
* **Procesamiento de Texto:** Utiliza `TfidfVectorizer` para convertir texto en datos numéricos procesables.
* **Interfaz amigable:** Construida totalmente en Python.


## 🛠️ Tecnologías utilizadas

**Lenguaje:**Python 3.10
**Streamli:** Para el despliegue de la interfaz web.
**Scikit-Learn:** Para el entrenamiento y ejecución del modelo SVM.
**Joblib/Pickle:** Para la serialización del modelo y el vectorizador.


## 📦 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone <https://github.com/carlos-villa-restrepo/URL-Spam-Detector-Streamlit.git>
   ```


## 📁 Archivos del Modelo

Para que la aplicación funcione, el proyecto requiere de dos archivos esenciales generados durante el entrenamiento, almacenados en la carpeta `models/`:
* `models/svm_model.pkl`: El modelo clasificador SVC entrenado.
* `models/svm_vectorizer.pkl`: El vectorizador TF-IDF.


## 📊 Pruebas de Funcionamiento

Prueba de URL segura
[Prueba no-spam](assets/prueba-url-segura.png)

Prueba  de URL SPAM
[Prueba spam](assets/prueba-url-spam.png)


## Insignias

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Licencia](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)


## ⚖️ Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.