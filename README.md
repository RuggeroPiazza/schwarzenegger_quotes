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


