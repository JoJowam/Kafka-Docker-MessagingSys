#  Sistema: 
#  TP03 - Sistemas Distribuídos - RabbitMQ e Docker.
#  Autor: Josué VilLa Real.
#
 
#  Descrição: 
#  Este programa foi desenvolvido para a disciplina de Sistemas Distribuídos
#  lecionada pelo professor Carlos Frederico na Universidade Federal de Ouro Preto.
#  O Objetivo deste trabalho é desenvolver um sistema de mensagens entre conteiners
#  docker com o intermédio do RabbitMQ. O programa em questão é o consumidor, que é
#  responsavel por receber mensagens do canal do rabbitmq, que por sua vez, recebe
#  do produtor. O consumidor é responsavel por receber a mensagem e imprimi-la na tela.
 
#  Principais pontos:
#  - Para a realização do trabalho utilizei a linguagem python e a biblioteca pika que é
#  responsavel por fazer a conexão com o rabbitmq. Para a criação dos containers utilizei
#  alguns Dockerfiles e o docker-compose.yml para fazer a conexão entre os containers.
  
#  - Para a função de processamento de mensagens utilizei a função "basic_consume" da biblioteca
#  pika que é responsavel por consumir as mensagens da fila especificada. Ela recebe "queue"
#  como parâmetro, que é o nome da fila, e "process_message" como parâmetro, que é a função
#  que irá processar a mensagem recebida. O parâmetro "auto_ack" é responsável por fazer o
#  reconhecimento automatico da mensagem, onde o RabbitMQ vai marcar a mensagem como 
#  concluída assim que ela for recebida. Dentro da função "process_message" temos os parâmetros
#  "channel", "method", "properties" e "body". O parâmetro "body" é a mensagem recebida, que é
#  decodificada para uma string legível e impressa na tela. "method" e "properties" são parâmetros
#  que não foram utilizados, mas que são necessários para o funcionamento da função e representam 
#  o método de entrega e as propriedades da mensagem, respectivamente. Isso é útil para o caso de
#  ser necessário fazer o reconhecimento manual da mensagem. E por fim, o parâmetro "channel" é
#  o canal que está sendo utilizado para consumir as mensagens, no caso configurei para que produtor
#  e consumidor utilizem o mesmo canal "rabbitmq".
 
#  Uso: 
#  Para executar o programa basta rodar o docker-compose.yml que esta na pasta "Dockerfiles" do projeto.
#  Isso irá criar os containers e executar o produtor e o consumidor. 
  
from kafka import KafkaConsumer

# Definindo a função que irá processar a mensagem recebida.
def process_message(message):
    # Decodificando a mensagem recebida para uma string legível.
    message_value = message.value.decode()
    print(f"Mensagem recebida: {message_value}")

    # Processando a mensagem (simulação de tempo de processamento)
    time.sleep(2)  # Aguarda 2 segundos para simular processamento

# Configuração do Kafka Consumer
consumer = KafkaConsumer(
    'message_topic',  # Nome do tópico a ser consumido
    bootstrap_servers='localhost:9092'  # Endereço do servidor Kafka
)

print('Aguardando mensagens...')

# Inicia o consumo de mensagens
for message in consumer:
    process_message(message)