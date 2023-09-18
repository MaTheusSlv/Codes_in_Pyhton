#AWS - CRIANDO INSTÂNCIAS EC2

# Criar a chave(key pairs) no site
# Criar função no site indicando a linguagem da função
# Adicionar a permissão IAM na função editando o JSON da policy, exemplo:
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
        "ec2:RunInstances"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}

# Adicionar o código Python na função

import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')


def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)

# Deve-se adicionar as variáveis à função de acordo com o script adicionado
# Clicar em DEPLOY e testar em um evento
# Em logs ou details da função já executada, pode-se ver o log da execução do script da função