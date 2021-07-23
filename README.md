
<h3 align="center">Documentacion Docker</h3>

---

## Prerequisitos

Como ya se sabe, este demo usa [Docker](https://docs.docker.com/get-started/overview/). Se debe instalar siguiendo los pasos indicados en el sitio oficial, dependiendo del OS del servidor: [documentacion](https://docs.docker.com/get-docker/).

Una vez este instalado Docker, se debe instalar [docker-compose](https://docs.docker.com/compose/). Obtener el paquete requerido dependiendo del sistema operativo usado [aqui](https://docs.docker.com/compose/install/).

Se recomienda instalar TMUX (o similar) para correr los containers en una sesion, de manera que se puedan ver los logs de Django por consola posteriormente. En el caso de Linux, TMUX se puede instalar corriendo:
```
apt-get install tmux
```

## Comandos basicos Docker

docker ps -a / docker ps
docker exec -it <container_id> bash
docker volume ls
docker volume rm <volume_id>
docker push (https://docs.docker.com/engine/reference/commandline/push/ - https://docs.docker.com/docker-hub/repos/)
docker image ls
docker stop <container_id>
docker run <image_id>

## Acceso a la base de datos en container por consola

* Obtener el ID del container donde la DB esta corriendo. Para ello, ejecutar el comando:
    ```
    docker ps
    ```

* Una vez se obtiene el ID del container, se debe ejecutar el siguiente comando para ingresar en modo root al terminal de este (reemplazar <Container-ID> por el ID obtenido en el paso anterior):
    ```
    docker exec -it <Container-ID> bash
    ```
* Para autenticarse y acceder al terminal de la base de datos (en este caso POSTGRES), ejecutar el comando:
    ```
    psql -h localhost -p 5432 -U postgres -W
    ```
    Cuando solicite password de acceso, ingresar **postgres**

## Acceso al container de la aplicacion web por consola

Para acceder al terminal donde se corre tu aplicacion web, se debe:

* Obtener el ID del container donde Django esta corriendo. Para ello, ejecutar el comando:
    ```
    docker ps
    ```
* Una vez se obtiene el ID del container, se debe ejecutar el siguiente comando para ingresar en modo root al terminal de este (reemplazar <Container-ID> por el ID obtenido en el paso anterior):
    ```
    docker exec -it <Container-ID> bash
    ```

## Operaciones importantes con los containers

* En el caso de que se necesite detener ambos containers, correr el comando para cada uno de ellos con su respectivo ID:
    ```
    docker stop <Container-ID>
    ```

* En el caso de que se necesite detener containers y remover sus imagenes y sub-redes, correr:
    ```
    docker-compose down
    ```

* De llegarse a necesitar la direccion IP de algun container, se puede ejecutar el comando (reemplazando el ID al final):
    ```
    docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id>
    ```

* Si se necesita obtener informacion sobre la subred de Docker, ejecutar:
    ```
    docker network ls
    ```

* Si se necesita eliminar todos los containers y sus volumes (hacer solo en casos extremos), ejecutar:
    ```
    docker rm -f $(docker ps -a -q)
    docker volume rm $(docker volume ls -q)
    ```

## Deployments

Seguir los siguientes para hacer un deployment de manera exitosa:

* Crear una sesion TMUX, ejecutando el comando:
    ```
    tmux new -s biometria
    ```
* Para construir las imagenes de los containers, ejecutar el comando:
    ```
    docker-compose build
    ```
* Para ejecutar las instrucciones definidas en el docker-compose.yml (crear volumes y correr ambos containers):
    ```
    docker-compose up
    ```
* Una vez ambos containers esten corriendo y la aplicacion Django tambien, se pueden observar los outputs de esta por consola. Para hacer detach de la sesion TMUX, presionar **Ctrl+B y luego D**
* Para volver a hacer attach a la sesion, ejecutar:
    ```
    tmux attach -t biometria
    ```

## Instalacion de Portainer

Portainer es una herramienta para gestionar Docker containers desde una interfaz grafica. Portainer funciona como un container mas dentro de la subred Docker. Para instalarlo, ejecutar los siguientes comandos:
```
docker volume create portainer_data
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

Estas instrucciones descargaran la imagen de Portainer, crearan un volume para dicjo container y haran correr la aplicacion por el puerto 9000. Para acceder a Portainer, abrir el explorador y dirigirse a http://url_de_la_aplicacion:9000. Se debera generar las credenciales de acceso.

## Instalacion de Nginx Proxy Manager

Una vez dentro de Portainer, dirigirse a la seccion "Stacks" en el menu izquierdo, y presionar "Add stack". Seguidamente, darle un nombre al stack de nginx y pegar el docker-compose de Nginx en el editor. El docker-compose del stack esta disponible [aqui](https://nginxproxymanager.com/guide/#quick-setup) - copia y pega ese codigo. A continuacion, presionar "Deploy the stack". Podras acceder a Nginx Proxy Manager desde http://url_de_la_aplicacion:81 .

Por ultimo, se debe configurar el SSL para el URL de la aplicacion. Para ello, crear credenciales de accesso y seguidamente dirigirse a "Proxy Hosts" -> "New Proxy Host". Desde ahi, llenar el formulario mostrado, activar "Block Common Exploits". En la tab de "SSL" llenar el dominio y activar "Force SSL" junto con "HTTP/2 Support". Finalmente, presionar en "Save".


Cualquier cosa escribanme :)

**svirahondadt** - Sergio Virahonda
