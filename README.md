# Aplicación Python con Docker

Esta es una aplicación Python que utiliza FastAPI y una base de datos PostgreSQL, y está configurada para ejecutarse en un contenedor Docker.

## Requisitos previos

Asegúrate de tener instalados los siguientes componentes en tu sistema:

* Docker: [Instrucciones de instalación de Docker](https://docs.docker.com/get-docker/)
* Docker Compose: [Instrucciones de instalación de Docker Compose](https://docs.docker.com/compose/install/)

## Ejecución

Sigue estos pasos para ejecutar la aplicación:

1. Abre una terminal y navega hasta el directorio raíz de la aplicación.
2. Construye la imagen de Docker ejecutando el siguiente comando:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">docker compose up --build
   </code></div></div></pre>
3. Inicia los contenedores ejecutando el siguiente comando:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">docker-compose up
   </code></div></div></pre>

   Esto iniciará los contenedores de la aplicación y la base de datos PostgreSQL.
4. Accede a la aplicación en tu navegador web ingresando la siguiente URL:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>arduino</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-arduino">http://localhost:8000/
   </code></div></div></pre>

   Verás un mensaje de "Hello world" si la aplicación se ejecuta correctamente.
5. Para detener los contenedores, puedes presionar `Ctrl + C` en la terminal donde se están ejecutando, o ejecutar el siguiente comando en otra terminal en el mismo directorio:

   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">docker-compose down
   </code></div></div></pre>

## Uso

La aplicación proporciona los siguientes puntos finales:

* `GET /`: Devuelve un mensaje de "Hello world".
* `POST /users`: Crea un nuevo usuario en la base de datos. Debe enviarse un objeto JSON con los campos "username" y "password".
* `GET /users/{user_id}`: Obtiene un usuario específico de la base de datos según su ID.

Puedes probar los puntos finales utilizando herramientas como cURL, Postman o cualquier otra herramienta similar.

## Contribución

Si deseas contribuir a esta aplicación, siéntete libre de hacerlo. Puedes abrir problemas (issues) o enviar solicitudes de extracción (pull requests) para sugerir mejoras o correcciones.
