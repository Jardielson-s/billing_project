# Billing API

## Requisitos

- Docker
- Docker Compose
- Python 3

## Como Executar

1. Clone o repositório.
2. export as envs, no arquivo example.env
3. rode o banco: `docker-compose up -d db`
4. Rode as migrations com o comando:
```
python3 manage.py migrate
```
5. rode a aplicação com o comando `python3 manage.py runserver`

## Executar container

1. Execute `docker-compose up -d db && docker-compose up -d --build web` para rodar em as aplicações em background.
2. Acesse `http://localhost:8000/api/billing/upload/` para enviar arquivos CSV.

## Testes

para rodar o teste de integração execute(para rodar esses testes é preciso rodar o banco e as migrations do arquivo docker-compose: `docker-compose up -d db` depois do banco ser iniciado execute: `python3 manage.py migrate`):
```
python3 manage.py test billing.tests.test_integration
python3 manage.py test billing.services.tests.create_bill_service_test
python3 manage.py test billing.services.tests.update_bill_service_test


```

para rodar os demais testes execute:
```
python3 manage.py test billing.services.tests.unity_test_service_model
python3 manage.py test billing.services.tests.unity_test_service_email

```
