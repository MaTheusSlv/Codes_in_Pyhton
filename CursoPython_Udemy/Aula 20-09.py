#AWS - DESLIGANDO INSTÂNCIAS EC2

# Criar a função no Lambda
# Dar as permissões no IAM para a função, alterando a policy para a seguinte:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeRegions",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    }
  ]
}

# Adicionar o código Python na função

import boto3


def lambda_handler(event, context):

    # Listar as regioes
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    # Buscar em todas as regioes
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        print("Region:", region)

        # Filtrar somente as instancias ligadas
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['running']}])

        # Parar as Instancias
        for instance in instances:
            instance.stop()
            print('Stopped instance: ', instance.id)

# Clicar em DEPLOY
# Aumentar o timeout no Basic Settings da função para 2 Min
# No Cloudwatch, criar uma nova regra de agendamento usando uma Cron Expression e setando a função como a target da regra

#AWS - LIGANDO INSTÂNCIAS EC2

# Criar a função no Lambda
# Dar as permissões no IAM para a função, alterando a policy para a seguinte:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeRegions",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "*"
    }
  ]
}

# Adicionar o código Python na função

import boto3


def lambda_handler(event, context):

    # Listar as regioes
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    # Buscar em todas as regioes
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        print("Region:", region)

        # Filtrar somente as instancias Desligadas
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['stopped']}])

        # Iniciar as Instancias
        for instance in instances:
            instance.start()
            print('Started instance: ', instance.id)

# Clicar em DEPLOY
# Aumentar o timeout no Basic Settings da função para 2 Min
# No Cloudwatch, criar uma nova regra de agendamento usando uma Cron Expression e setando a função como a target da regra