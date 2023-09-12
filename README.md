# Documentação do Projeto de Sistema de Mensagens usando Kafka e Docker

Este repositório contém um projeto que implementa um sistema de mensagens usando Apache Kafka e Docker. O sistema é composto por dois containers Docker: um produtor e um consumidor, além de um terceiro container que executa um servidor Kafka. O projeto demonstra a comunicação assíncrona entre os componentes usando o Apache Kafka como intermediário.

## Pré-requisitos

Antes de executar este projeto, certifique-se de ter as seguintes ferramentas instaladas no seu sistema:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Estrutura do Projeto

O projeto possui a seguinte estrutura de arquivos:

````
├── Dockerfile
│   ├── Dockerfile.consumidor
│   ├── Dockerfile.kafka
│   └── Dockerfile.produtor
├── src
│   ├── consumidor.py
│   └── produtor.py
├── docker-compose.yml
└── README.md
````

- `Dockerfile.consumidor`, `Dockerfile.kafka`, e `Dockerfile.produtor` são os arquivos de configuração do Docker para a construção dos containers.
- `docker-compose.yml` define a configuração dos serviços e redes Docker.
- `consumidor.py` contém o código do consumidor de mensagens Kafka.
- `produtor.py` contém o código do produtor de mensagens Kafka.
- `README.md` é este arquivo de documentação.

## Configuração do Docker Compose

O arquivo `docker-compose.yml` define os serviços Docker necessários para executar o projeto. Ele inclui os seguintes serviços:

- `produtor`: Este serviço constrói um container a partir do arquivo `Dockerfile.produtor` e executa o script `produtor.py`, que envia mensagens para o tópico Kafka.
- `consumidor`: Este serviço constrói um container a partir do arquivo `Dockerfile.consumidor` e executa o script `consumidor.py`, que consome mensagens do tópico Kafka.
- `kafka`: Este serviço constrói um container a partir do arquivo `Dockerfile.kafka` e executa um servidor Apache Kafka. Ele expõe as portas 2181 (ZooKeeper) e 9092 (Kafka Broker) para a rede local.

## Executando o Projeto

Para executar o projeto, siga estas etapas:
1. Certifique-se de que o Docker e o Docker Compose estejam instalados no seu sistema;

2. Clone este repositório para o seu sistema;

3. Navegue até o diretório do projeto;

4. Execute o Docker Compose para construir e iniciar os containers:
```
docker-compose up --build
```
5. O projeto será iniciado, e você verá a saída do produtor e do consumidor no terminal.

6. Para interromper a execução do projeto, pressione Ctrl + C no terminal e execute o seguinte comando para parar e remover os containers:
```
docker-compose down
```

## Personalização do Projeto

Você pode personalizar este projeto fazendo alterações nos seguintes arquivos:

- `produtor.py`: Personalize a lógica do produtor de mensagens conforme necessário.
- `consumidor.py`: Personalize a lógica do consumidor de mensagens conforme necessário.
- `docker-compose.yml`: Adicione ou modifique os serviços Docker, portas expostas, volumes, etc., conforme necessário.

## Considerações Finais
Este projeto serve como um exemplo simples de como usar o Apache Kafka para implementar um sistema de mensagens assíncronas entre contêineres Docker. Lembre-se de que é uma implementação básica e pode ser expandida para atender a requisitos mais complexos.

# Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes. [MIT License](./LICENSE)
