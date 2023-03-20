# Docker-python

Lo primero que tenemos que hacer es crear el fichero "Dockerfile". Este fichero tendra el siguiente formato:

      FROM python:3

      WORKDIR /usr/src/app

      COPY requisitos.txt ./
      RUN pip install --no-cache-dir -r requisitos.txt

      COPY ./ /usr/src/app

      CMD [ "python", "lanzar.py"]
      
Una vez creado dicho documento, el siguiente paso es usar el comando "docker build -t youtubeimagen:lastest ."

Ahora que ya tenemos la imagen, podremos empezar a crear nuestro fichero "docker-compose.yml". El cual tendra el siguiente formato:

      services:
      
        python:
        
          image: youtubeimagen:latest
          
          volumes:
          
            - .:/usr/src/app
            
          stdin_open: true
          
          tty: true
          
          working_dir: /usr/src/app
          
          command: python lanzar.py 
          
          
Ahora que ya tenemos todo creado, podremos probar el contenedor con el comando "docker-compose up"


El siguiente paso sera subir el repositorio a docker hub, para ello primero crearemos el repositorio desde la web de docker hub.

Ahora que el repositorio esta creado, ejecutaremos los siguientes comandos en el terminal 

- docker login -> Con este comando inicamos sesion 

- docker tag youtubeimagen:latest davidcastelao/youtubeimagen:latest .

- docker push davidcastelao/youtubeimagen:latest

Si seguimos los pasos anteriores de forma correcta, ya tendriamos todo en docker hub
