# Proyecto American Express - Default Prediction

## Integrantes del equipo de desarrollo del proyecto

- Santiago García Castrillón, CC 1152469548, Ingeniería Mecánica
- Juan Daniel Tabáres Goez, CC 1037663427, Ingeniería Mecánica

## Datos

Los datos del proyecto vienen de [American Express - Default Prediction](https://www.kaggle.com/competitions/amex-default-prediction/), y se pueden hacer disponibles después de haber descargado el archivo `.json` desde Kaggle en Account, API, Create New API Token. Luego ejecutamos desde cualquier notebook en Colab los siguientes comandos y cargamos el archivo `.json` cuando se nos pida. 

    ! pip install -q kaggle

    from google.colab import files

    files.upload()

    ! mkdir ~/.kaggle

    ! cp kaggle.json ~/.kaggle/

    ! chmod 600 ~/.kaggle/kaggle.json

    ! kaggle datasets list

    ! kaggle competitions download -c amex-default-prediction

    !unzip amex-default-prediction.zip

    !rm amex-default-prediction.zip

En la  última línea borramos el archivo comprimido dado que necesitaremos este espacio de disco en Google Colab.
    

## Videos

- [Video entrega final](https://youtu.be/jFFy-aXcy2c)

