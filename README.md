Antes de ejecutar el modelo, se necesita descargar Git y el modelo de LLaMa 3.1 8B Instruct en Hugging Faces.
# Para descargar 'LLaMa 3.1 8B Instruct', seguir los siguientes pasos:
1. Ingresar al siguiente [link](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)
2. Iniciar sesión en Hugging Faces para poder acceder al modelo, así mismo, brindar los datos personales solicitados por Meta.
3. Una vez que se cuente con acceso al modelo, ingresar a Settings > Access tokens (la opciòn settings se muestra en el desplegable que se muestra al clickear en la foto de perfil que se encuentra en la parte superior derecha de la pantalla).
4. Al ingresar a la secciòn 'Access tokens', crear un nuevo token con el boton 'Create new token'.
         - Ingresar el nombre del token, puede ingresar el que desee.
         - Brindar los siguientes permisos:
             ![image](https://github.com/user-attachments/assets/8118e632-21f0-4845-a4fa-599a86f8611c)
         - Seleccionar el modelo, este deberia de aparecer en la lista desplegable si ya se cuenta con permisos.
             ![image](https://github.com/user-attachments/assets/850b27e9-a104-4da4-b7b8-69c14b0f5da1)
        - Guardar el token con 'Save token'.     
6. Al guardar el token, se mostrará un pop-up con el token generado, copiarlo para más adelante.
7. Dirigirse al 'Explorador de archivos' en su ordenador y crear una nueva carpeta.
8. Hacer click derecho en la carpeta creada y seleccionar la opción 'Open Git Bash here'.
9. Ingresar el siguiente comando:
          ### `git clone https://<USERNAME>:<TOKEN_NAME>@huggingface.co/<MODEL_NAME>`
          - En <USERNAME> colocar su nombre de usuario de Hugging Faces; en <TOKEN_NAME>, el token copiado anteriormente.
   Por ejemplo:
            ### `git clone https://sabrinaxsln:hf_1234565678@huggingface.co/meta-llama/Llama-3.1-8B-Instruct`
10. Ejecutar el comando y esperar la descargar completa del modelo, este puede tardar dependiento de la velocidad de su red.

# Para descargar 'Git', seguir los siguientes pasos:
1. Ingresar al siguiente [link](https://git-scm.com/)
2. Click en 'Downloads'.
3. Seleccionar 'Windows 10', luego la versión de 64 bits git for Windows Setup.
4. Una vez descargado, click en el archivo descargado, dar permisos y click en 'Install'.
