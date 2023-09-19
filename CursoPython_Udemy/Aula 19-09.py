#AWS - REDUZINDO TAMANHO DE IMAGENS

# Criar as buckets, de origem e destino, na S3
# Criar função no site
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
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::NOMADABUCKET-ORIGEM/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::NOMEDABUCKET-DESTINO/*"
    }
  ]
}

# Criar um trigger S3 para a bucket de origem
# Baixar a biblioteca PIL (Pillow 7.2.0) e upar na máquina do AWS
# Adicionar o código Python na função

import os
import tempfile

import boto3
from PIL import Image

s3 = boto3.client('s3')
DEST_BUCKET = os.environ['NOMEDABUCKET-DESTINO']
SIZE = 128, 128


def lambda_handler(event, context):

    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        thumb = 'thumb-' + key
        with tempfile.TemporaryDirectory() as tmpdir:
            download_path = os.path.join(tmpdir, key)
            upload_path = os.path.join(tmpdir, thumb)
            s3.download_file(source_bucket, key, download_path)
            generate_thumbnail(download_path, upload_path)
            s3.upload_file(upload_path, DEST_BUCKET, thumb)

        print('Thumbnail image saved at {}/{}'.format(DEST_BUCKET, thumb))


def generate_thumbnail(source_path, dest_path):
    print('Generating thumbnail from:', source_path)
    with Image.open(source_path) as image:
        image.thumbnail(SIZE)
        image.save(dest_path)

# Deve-se adicionar as variáveis à função de acordo com o script adicionado
# Clicar em DEPLOY e testar em um evento
# Em logs ou details da função já executada, pode-se ver o log da execução do script da função
# Se necessário, aumentar o timeout no Basic Settings da função, se as imagens forem muito grandes por exemplo

#AWS - BACKUP PROGRAMADO DE INSTÂNCIA EC2

# Snapshots = Imagens da instância que podem ser restaurada em caso de problemas

# Ter uma instância EC2 (t2.micro)
# Adicionar uma TAG de BACKUP com valor TRUE
# Criar uma função no site
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
      "Effect": "Allow",
      "Action": [
        "ec2:CreateSnapshot",
        "ec2:CreateTags",
        "ec2:DeleteSnapshot",
        "ec2:Describe*",
        "ec2:ModifySnapshotAttribute",
        "ec2:ResetSnapshotAttribute"
      ],
      "Resource": "*"
    }
  ]
}

# Adicionar o código Python na função:

from datetime import datetime

import boto3


def lambda_handler(event, context):
    # Listando regioes
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    for region in regions:

        print('Instances in EC2 Region {0}:'.format(region))
        ec2 = boto3.resource('ec2', region_name=region)

        instances = ec2.instances.filter(
            Filters=[
                {'Name': 'tag:backup', 'Values': ['true']}
            ]
        )

        # Adicionando timestamp
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

        for i in instances.all():
            for v in i.volumes.all():

                desc = 'Backup of {0}, volume {1}, created {2}'.format(
                    i.id, v.id, timestamp)
                print(desc)

                snapshot = v.create_snapshot(Description=desc)

                print("Created snapshot:", snapshot.id)

# Deve-se adicionar as variáveis à função de acordo com o script adicionado
# Aumentar o timeout da função
# Criar um agendamento de quando rodará essa função no Cloudwatch indicando o target(Função que foi criada)