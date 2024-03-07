# Workshop_1 Candidates Hired Job

![Ejemplo](https://ix-cdn.b2e5.com/images/208444/208444_30e22a1f13434888a1e7b330d0bf087f_1600957198.png)

# Situacion
## Se nos da un archivo csv llamado Candidates, en el cual encontramos un total de 50000 registros los cuales abarcan la siguiente informacion: 
- First Name: Nombre del candidato
- Last Name: Apellido del candidato
- Email: Correo electrónico del candidato
- Application Date: Fecha de solicitud del candidato
- Country: País del candidato
- YOE: Años de experiencia del candidato
- Seniority: Nivel de seniority del candidato
- Technology: Tecnología relacionada con la posición para la que el candidato se postuló
- Code Challenge Score: Puntuación del desafío de código
- Technical Interview Score: Puntuación de la entrevista técnica
### Se tiene qu leer el archivo csv con python y migrar esta tabla a nuestra base de datos, ya desde ahi nos conectamos desde python a la base de datos para leer el cvs y poder hacer la modificacion que se nos pide, la cual es agregarle a esta tabla un nuevo campo "Hired" el cual tendra como valores unicos YES or NO dependiendo si el registro xumple con las siguientes restricciones ( Todo este proceso se tiene que hacer con python conectada a nuesta base de datos SQL).
- El valor en el campo de Code Challenge Score debe ser mayor o igual a 7, y la misma restriccion para el campo Tecnical Interview Score, si el registro solo cumple solo con una de estas restricciones, su valor en el registro sera "NO" y si el registro cumple con las dos restricciones el valor del registro sera "YES".
- Hired: Indica si el candidato fue contratado o no
# Herramientas utilizadas para este proyecto
- Python
- MySQL
- Jupyter Notebook
- Power BI
- Variables de entorno para la encriptqacion de las credenciales
