# Workshop_1 Candidates Hired Job

![Ejemplo](https://ix-cdn.b2e5.com/images/208444/208444_30e22a1f13434888a1e7b330d0bf087f_1600957198.png)

# Tools used for this project
![Ejemplo](https://miro.medium.com/v2/resize:fit:1137/1*OnDVcS17HTWZ2L2vPaaQ1A.png)
- Python 
- MySQL
- Jupyter Notebook
- Power BI
- Environment variables for credential encryption

# Context

### We are given a csv file called Candidates, in which we find a total of 50000 records which include the following information: 
![Candidates](https://media.discordapp.net/attachments/1068002173448896532/1215730303432269894/image.png?ex=65fdd013&is=65eb5b13&hm=ee52260ee3a296dd388208def2ae0f20a3408f58474ca56514353d01cefeda4e&=&format=webp&quality=lossless)

- First Name: Name of candidate
- Last Name: Last name
- Email: Candidate’s email
- Application Date: Application date
- Country: Country of candidate
- YOE: Candidate’s years of experience
- Seniority: Seniority level of the candidate
- Technology: Technology related to the position for which the candidate applied
- Code Challenge Score: Code challenge score
- Technical Interview Score: Technical interview score
### You have to read the csv file with python and migrate this table to our database, since here we connect from python to the database to read the cvs and make the modification that is asked, which is to clone the original table and add it a new field called "Hired" which will have as unique values YES or NO depending if the record meets the following restrictions (All this process has to be done with python connected to our SQL database).
- The value in the Code Challenge Score field must be greater than or equal to 7, and the same restriction for the Technical Interview Score field, if the record only meets one of these restrictions, its value in the record will be "NO" and if the record complies with the two restrictions the value of the record will be "YES".
- Hired: Indicates whether the candidate was hired or not
![Candidates Hired](https://media.discordapp.net/attachments/1068002173448896532/1215734499120517130/image.png?ex=65fdd3fb&is=65eb5efb&hm=3d16a85f493e3405a00cd80505277d2019cd66db5cacfea7d69de90849d54c1c&=&format=webp&quality=lossless)

# Guide to the repository
### In this repository you will find all the process, read, migrate and transform data but it is important that you know the why? of each folder and file it brings with it
## Workshop_Code
### In this folder you will find all the code of the reading, connection and migration of data, in addition to all this will also be the modifications and SQL queries that were made to the database, each process has its own file. own py. It should be recalled that the file that refers to the connection also makes the upload to the database and this will be highlighted in its final commit.
- Workshop_csv.py works with the reading of the csv of candidates with pandas, besides that it makes some print to the dataframe seeking to visualize it and to see already detailed information of the dataset, like the number of data and fields with its corresponding type of data.
- Workshop_connector.py already starts importing several libraries that will allow us to connect with our MySQL database, also the library that will help us read our file . env is correct and we also imported from the beginning the datafram we made in the previous file thanks to pandas.
- Workshop_querys works a new connection and is that yes! from the previous connection file, we have to make a request in the form of a connection to validate the restrictions, after that this file works by means of SQL queries the creation of the new candidate table, with its new field "Hired", incorporating the constraints that this field must have with a SQL query.
- database.config.json contains the credentials that the file . env must have, and subsequently read in Workshop_connector and Workshop_querys to be able to connect to the database.
## Notebook
![Hires By Technology](https://todobi.com/content/images/2020/04/10-great-google-analytics-alternatives-5e4175671fa6a.png)
### In this folder you will find the jupyter notebook of this work which apart from covering together all the code of the previous folder, each fragment of the code is explained, which helps a lot when you want to understand the process through which the csv passes and later the dataset. In addition, the added value and why this jupyter is fundamental is the analysis it does, focusing on understanding the context of the dataset with the new field, looking to take advantage of it analyzing trends and behavior between the data so later to approach the dataset in a better way in the Dashboard with an ephoque and idea already designed thanks to the process of analysis that was made in this notebook.
- Workshop_1_Analysis.ipynb focuses on the analysis of the dataset, thus being able to look for relationships and trends in the form of various graphs that will help define the approach and idea to be shown in a future dashboard.
## Document
![Hires By Technology](https://ceosa.org.za/wp-content/uploads/shutterstock_519437803.jpg)
### In this folder you will find the project document, which covers all the evidence throughout the development of the workshop and the conclusions that were obtained at the end of the whole process. This document also has preliminary comments that need to be taken into account when evaluating and contextualizing the process. 
- Workshop_1_docx is the downloadable world file of the document
- link.json is a file which will give us the direct link to view the document from our website
## Dashboard
![Hires By Technology](https://media.discordapp.net/attachments/1068002173448896532/1215721355828527214/image.png?ex=65fdc7be&is=65eb52be&hm=d2f6c6968e4ab868872248183da7f4d0ae17139a9a43a1abd5caf0206498bff9&=&format=webp&quality=lossless)
### In this folder you will find the dashboard with the graphs that were requested as a requirement for this work, in JPG format and in "Power BI" format that will allow you to run the dashboard from this same application to interact in real time with graphs and data
![Hires By Seniority](https://media.discordapp.net/attachments/1068002173448896532/1215723663920336956/image.png?ex=65fdc9e4&is=65eb54e4&hm=c281f97ed5ba698b4aa0924b307d4af55dd5fbfbcb7bca3cbed3be508c3e6bb1&=&format=webp&quality=lossless&width=1205&height=675)

![Hires By Year](https://media.discordapp.net/attachments/1068002173448896532/1215725921152147557/image.png?ex=65fdcbfe&is=65eb56fe&hm=f37a15b8aeb9d1915b7bf3ab636338170af897e5c5d5219e5381371fd271095f&=&format=webp&quality=lossless&width=1205&height=675)

![Hires By Country Over Years](https://media.discordapp.net/attachments/1068002173448896532/1215726952070127666/image.png?ex=65fdccf4&is=65eb57f4&hm=e24822ded23fd01d19bed63a3066259e216fc6bba8b28c38ccf7ba0bbb9b02ce&=&format=webp&quality=lossless&width=1206&height=675)

- Analysis_Candidates_Hired_Dashboard.pbix is the original format of the dashboards that are made in power bi, download it and you can arir the dashboard from the application.
- Analysis_Candidates_Hired.JPG is a picture of the dashboard that you can view from github.

## Data
![Data](https://cdn-icons-png.freepik.com/512/8242/8242984.png)
### In this folder you will find the csv candidates file which is the only data source used in this process
- Candidates_csv
## .gitignore
![.gitignore](https://res.cloudinary.com/practicaldev/image/fetch/s--J88XdmpA--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://dev-to-uploads.s3.amazonaws.com/i/gqvc4folezic8qvkjbca.png)
### This file specifies files and folders that were created in our own directory, files that do not add value to the presentation and structure of this repository
