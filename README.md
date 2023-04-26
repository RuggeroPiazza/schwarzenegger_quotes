# schwarzenegger_quotes


## **Description**
This project was designed as a way to practice with the interaction between the following services: API Gateway, Lambda, DynamoDB, and Amplify.

The app randomly chooses a famous quote from one of many Arnold Schwarzenegger movies and shows it on the home page, with a picture of the related movie.
If the page is refreshed, a new quote will be shown.

## **Services Overview**

- **Amplify**
The front-end deployment is taken care by AWS Amplify. 
Amplify makes the deployment of new apps extremely easy. Thanks to an intuitive and simplified interface, is the ideal solution for building, shipping or hosting an app (web and mobile) quickly. In this case, Amplify is perfect because allows us to host the app very quickly: we just need to upload our files and we quickly get a URL that can be used to show our final product. 

- **API Gateway**
API gateway is responsible for accepting and processing requests coming from the client, making sure they are directed to the specific API resources.
This service is convenient for this particular use case because it offers CORS support, traffic management, throttling and monitoring. It also has no minimum fees or startup costs, making it ideal for running apps at the lowest costs possible. 

- **Lambda**
the backend layer starts with a Lambda, a service that allows us to provision just the computing power necessary to run our code. As long as our code doesn’t need to run for more than 15 minutes, Lambda functions are a great solution to provide fully managed computing at a very low price. Because our app doesn’t have specific requirements in terms of computing configurations and it’s not computing-demanding, Lambda is a perfect choice.

- **DynamoDB**
on the storage side of the application, the DynamoDB NoSQL database is ideal. 
DynamoDB is a fully managed service, with horizontal scaling capabilities and offers the choice between provision capacity or on-demand capacity.
On top of having great performance, it has full compatibility with other AWS services, making it very easy to implement inside an architecture.

All the services mentioned are great choices for serverless architectures, where you want to build something without having to worry about the underlying infrastructure of the services you are using. 

## **Step-By-Step Guide**

![alt text](arnoldDiagram.jpg)

1. **Create a table in DynamoDB**\
Select DynamoDB from the management console and click on the orange "create table" button.\
Name the table "arnold" (if you choose to name this table differently, please remember to change to the correspondent table's name on the Python script too)\
Use "movie_title" as partition key and create the table\
When created, click the "action" dropdown button and select "create item"\
You can now manually create each table's item:\
First add the movie title as a value.\
Then click on "add new attribute", select "list" and add all the quotes relative to that specific movie.\
The following screenshot shows the structure of the items\ 


2. **Create a Lambda function**\
Select Lambda from the Management Console and click on the orange "create function" button.\
Select "Author from scratch"\
Name your function\
Select "Python 3.9" as the runtime\
Leave the other settings as default and click "Create function"

In the "code" section of the page, delete the default script alredy written and swap it with the script from this repository (arnold.py)\

When triggered, this script simply run a query on a DynamoDB table named "arnold".\
Before querying the database, the script randomly pick a movie title from the list of movie titles, then use the result as a parameter for the query (to randomise the selection of the movie choice).\
From the response of the query, we get a list of quotes and the url for the movie's poster image.\
At this stage, we randomly choose a quote from the list of quote.\
We then return both the quote (as string) and the image URL (as string) inside the body of a json.dumps\
Please notice that the header returned is important for the correct interaction with API Gateway.\
