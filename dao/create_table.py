import boto3

class Table():
    def __init__(self, table_name):
        self.dynamodb = boto3.resource('dynamodb')
        self.table_name = table_name

    def create_table(self):
        table = self.dynamodb.create_table(
            TableName=self.table_name,
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
        print(table)

    def insert(self, row):
        table = self.dynamodb.Table(self.table_name)
        r = table.put_item(Item=row)
        return r

    def select_all(self):
        table = self.dynamodb.Table(self.table_name)
        r = table.scan()
        return r

    def select(self):
        table = self.dynamodb.Table(self.table_name)
        qdata = table.get_item(Key={"id": "qwer1234"})

        print(qdata['Item'])

# stdSpciesNewCode + whsalMrktNewCode + delngDe로 id를 생성해서 넣는 것은 어떨까?
# 새 record가 들어갈 때 key를 생성해야 하는 이슈가 있다.
# partition key로 할 수 있는 검색은 일치 검색만 되는 것인가?
# unique면서도 검색이 되어야 한다.
# 속성 두 개를 기본 키로 사용합니다(복합키). 첫 번째 속성은 해시 기본 키로 사용하고
# 두 번째 속성은 범위 기본 키로 사용하여 두 가지를 복합적으로 사용합니다.
# 일치(Equal), 부등호, 포함, ~로 시작등의 검색을 지원합니다.

'''
response = table.query(
    KeyConditionExpression=Key('username').eq('johndoe')
)
'''