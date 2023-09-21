#AWS - AGENDANDO BACKUPS NO DynamoDB

# No DynamoDB criar uma tabela com seus conteúdos
# Criar função de backup no Lambda
# Dar as permissões no IAM para a função, alterando a policy para a seguinte:

{
  "Version": "2012-10-17",
  "Statement": [{
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Action": [
        "dynamodb:CreateBackup",
        "dynamodb:DeleteBackup",
        "dynamodb:ListBackups"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}

# Adicionar o código Python na função

import boto3
from datetime import datetime

dynamo = boto3.client('dynamodb')

# Verificar as tabelas
def lambda_handler(event, context):
    if 'TableName' not in event:
        raise Exception("No table name specified.")
    table_name = event['TableName']

    create_backup(table_name)

# Ciar o backup da tabela
def create_backup(table_name):
    print("Backing up table:", table_name)
    backup_name = table_name + '-' + datetime.now().strftime('%Y%m%d%H%M%S')

    response = dynamo.create_backup(
        TableName=table_name, BackupName=backup_name)

    print(f"Created backup {response['BackupDetails']['BackupName']}")

# Clicar em DEPLOY
# Aumentar o timeout no Basic Settings da função a depender do tamanho da tabela
# No Cloudwatch criar uma regra de agendamento com a função criada como Target e nas opções de Input
#selecionar Constant (JSON text) com o valor {"TableName":"nomedatabela"}

# CISCO - GNS3

# "É um emulador de topologia de rede utilizado por engenheiros de rede para simular infraestruturas"

# Adicionar roteadores no GNS3
# Adicionar switches no GNS3
# Mudar os hostnames dos aparelhos adicionados
# Adicionar as conexões entre os aparelhos
# Configurar os IPs dos roteadores
# Mudar a configuração da VM do GSN3 para Bridge no Network Adapter