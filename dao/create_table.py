import boto3

class Table():
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')

    def create_table(self, table_name):
        table = self.dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'stdSpciesNewCode',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'delngDe',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'stdSpciesNewCode',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'delngDe',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'price',
                    'AttributeType': 'N'
                }
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'code_price',
                    'KeySchema': [
                        {
                            'AttributeName': 'stdSpciesNewCode',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'price',
                            'KeyType': 'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )