# Workshop_1 Candidates Hired Job

![Ejemplo](https://ix-cdn.b2e5.com/images/208444/208444_30e22a1f13434888a1e7b330d0bf087f_1600957198.png)

# Herramientas utilizadas para este proyecto
![Ejemplo](https://miro.medium.com/v2/resize:fit:1137/1*OnDVcS17HTWZ2L2vPaaQ1A.png)
- Python 
- MySQL
- Jupyter Notebook
- Power BI
- Variables de entorno para la encriptqacion de las credenciales

# Situacion
### Se nos da un archivo csv llamado Candidates, en el cual encontramos un total de 50000 registros los cuales abarcan la siguiente informacion: 
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
# Guia del repositorio
### En este repositorio encontraras todo el proceso, de lectura, migracion y transformacion de datos pero es importante que conozcas el ¿por que? de cada carpeta y archivo que trae consigo
## Workshop_Code
### En esta carpeta encontraras todo el codigo de la lectura,conexion y migracion de datos, ademas de todo esto tambien estaran las modificaciones y consultas SQL que se le hicieron a la base de datos, cada proceso tiene su propio archivo .py propio. Cabe reaclar que el archivo que hace referencia a la conexion tambien hace la carga a la ase de datos y esto estara resaltado en su commit final.
- Workshop_csv.py trabaja la lectura del csv de candidates con pandas, ademas de eso hace unos print al dataframe buscando poder visualizarlo y ver informacion ya detallada del dataset, como el numero de datos y campos con su tipo de dato correspondiente.
- Workshop_connector.py empieza ya importando varias bibliotecas que nos van a permitir poder conectarnos con nuestra base de datos MySQL, tambien la biblioteca que nos ayudara a que la lectura de nuestr archivo .env sea correcta y tambien importamos desde un comienzo el datafram que hicimos en el anterior archivo gracias a pandas.
- Workshop_querys trabaja una nueva conexion y es que si! desde el anterior archivo de la conexion, tenemo que hacer una solicitud en forma de conexion para validar las restricciones, despues de esto este archivo trabaja por medio de consultas SQL la creacion dela nueva tabla candidates_hired, con su nuevo campo "Hired", incorporando las restricciones que este campo tienen que tener con una consulta SQL.
- database.config.json contiene las credenciales que el archivo .env debe de tener, y que posteriormente se leen en Workshop_connector y Workshop_querys para poder conectarse a la base de datos

