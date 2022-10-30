import boto3

dynamodb = boto3.resource("dynamodb", region_name='us-east-1')

table = dynamodb.create_table(
    TableName ="Throwback_Songs",
       KeySchema =[
           {
               'AttributeName': "title",
               'KeyType': "HASH"
           },
           {
               'AttributeName': "year",
               'KeyType': "RANGE"
           }
           ],
           AttributeDefinitions =[
               {
                   'AttributeName': "title",
                   'AttributeType': "S"
               },
               {
                   'AttributeName':"year",
                   'AttributeType': "N"
               }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10,
            }
           )
           
table.wait_until_exists()



print(table.item_count)
