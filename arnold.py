import boto3
import random
import json


# dynamoDB client
db = boto3.client('dynamodb')

# list of movie titles to avoid having to scan the table for the items
primary_key_list = [
    "batman and robin",
    "collateral damage",
    "commando",
    "conan the barbarian",
    "end of days",
    "eraser",
    "kindergarten cop",
    "jingle all the way",
    "last action hero",
    "predator",
    "terminator: dark fate",
    "terminator 2: judgment day",
    "terminator 3: rise of the machines",
    "the terminator",
    "the running man",
    "total recall",
    "true lies",
    "twins"
]

def lambda_handler(event, context):
    movie_title = random.choice(primary_key_list)
    # query the table
    response = db.query(
        TableName='arnold',
        KeyConditionExpression='#title = :title',
        ExpressionAttributeNames={
            '#title': 'movie_title'
        },
        ExpressionAttributeValues={
            ':title': {'S': movie_title}
        },
        ProjectionExpression='quotes, poster_image',
    )
    if 'Items' in response:
        quotes = response['Items'][0]['quotes']['L']
        quotes_list = [quote['S'] for quote in quotes]
        quote = random.choice(quotes_list) 
        image_url = response['Items'][0]['poster_image']['S']
        return {
            'statusCode': 200,
            'body': json.dumps({"quote": quote, "poster_image": image_url}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
    return {
        'statusCode': 404,
        'body': f"No quotes found for {movie_title}"
        }

