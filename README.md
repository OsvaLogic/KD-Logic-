# KD-Logic Video Downloader (V8.6)

```text
========================================================================================
 :::    ::: :::::::::          :::        ::::::::   ::::::::   :::::::::::  :::::::: 
 :+:   :+:  :+:    :+:         :+:       :+:    :+: :+:    :+:      :+:     :+:    :+: 
 +:+  +:+   +:+    +:+         +:+       +:+    +:+ +:+            +:+     +:+        
 +#++:++    +#+    +:+         +#+       +#+    +#+ :#:            +#+     +#+        
 +#+  +#+   +#+    +:+         +#+       +#+    +#+ +#+    +#+      +#+     +#+        
 #+#   #+#  #+#    #+#         #+#       #+#    #+# #+#    #+#      #+#     #+#    #+# 
 ###    ### #########          ##########  ########   ########   ###########  ######## 
========================================================================================
                      KD-LOGIC V8.6 | KICK CLIP FIX | OSVA.LOGIC
```

KD-Logic es una herramienta por consola desarrollada en Python diseñada para forzar la extracción y descarga de clips de plataformas como Kick y TikTok, haciendo bypass al modo "En Vivo" y permitiendo elegir la resolución deseada.

## ✨ Características Principales

- **Selección de Múltiples Calidades:** El script detecta todas las resoluciones disponibles del clip original y te permite elegir exactamente en qué calidad de video deseas descargarlo.
- **Bypass "En Vivo":** Fuerza la extracción y descarga de clips incluso cuando la plataforma los bloquea o los marca como streams.
- **Evasión de Restricciones:** Utiliza las cookies de tu navegador local para saltar bloqueos de región o de edad automáticamente.

##  Guía de Instalación y Uso

Sigue estos pasos para poner en marcha el programa.

### Paso 1: Instalar Requisitos

1.  **Python 3.7 o superior**
    - **Descarga:** python.org
    - **Importante:** Durante la instalación, asegúrate de marcar la casilla que dice **"Add Python to PATH"**.

2.  **Google Chrome**
    - El script extrae las cookies de tu navegador Chrome para evitar bloqueos y restricciones de edad o región.
    - **Descarga:** google.com/chrome

### Paso 2: Descargar FFmpeg

FFmpeg es una herramienta esencial que el script utiliza para unir el video y el audio de alta calidad y para la conversión de formatos.

1.  **Descarga FFmpeg:**
    - Ve a la página de compilaciones de FFmpeg para Windows: gyan.dev/ffmpeg/builds/
    - En la sección `release builds`, descarga el archivo ZIP llamado **`ffmpeg-release-essentials.zip`**.

2.  **Extrae y ubica los archivos:**
    - Descomprime el archivo `.zip` que acabas de descargar.
    - Entra en la carpeta que se ha creado (ej. `ffmpeg-7.0-essentials_build`) y luego en la carpeta `bin`.
    - Copia los archivos **`ffmpeg.exe`** y **`ffprobe.exe`**.
    - Pega ambos archivos en la **misma carpeta** donde se encuentra el script `KD-Logic.py`.

### Paso 3: Ejecutar el Script

¡Ya está todo listo! El script se encarga de instalar el motor de descarga (`yt-dlp`) por sí mismo la primera vez que lo ejecutas.

1.  Ejecuta el script haciendo doble clic en el archivo `KD-Logic.py` (si tienes Python asociado a los archivos `.py`) o ábrelo desde una terminal:
   ```bash
   python KD-Logic.py
   ```

2.  Pega el enlace del clip de Kick o TikTok cuando el programa te lo solicite y presiona Enter.
3.  El programa mostrará las resoluciones disponibles. Escribe el **número** de la calidad que deseas y presiona Enter.
4.  ¡Listo! El clip se descargará y se guardará en una nueva carpeta llamada `Descargas_KDLogic`.

## ⚠️ Solución de Problemas

-   **Error "FFmpeg not found" / "FFmpeg no encontrado"**:
    -   Este es el error más común. Asegúrate de haber seguido el **Paso 2** correctamente. Los archivos `ffmpeg.exe` y `ffprobe.exe` deben estar en la misma carpeta que `KD-Logic.py`.

-   **La descarga falla o el clip no se encuentra**:
    -   Verifica que el enlace del clip sea correcto y no esté roto.
    -   Asegúrate de tener la sesión iniciada en Kick/TikTok en tu navegador Google Chrome, especialmente para contenido privado o con restricción de edad. El script usará esa sesión.

-   **Para salir de la aplicación**:
    -   Simplemente escribe `salir` cuando el programa te pida un enlace y presiona Enter.