# How to use

```
docker-compose up -d && docker-compose logs -f
```

# Verify rabbitmq connection with prometheus

> Status menu -> Targets

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/rabbitmq-prometheus.png?raw=true)

http://localhost:9090/targets?search=

# Grafana login

http://localhost:3000

Uses user ans password: admin and press login

Now setup a new password or click "Skip"

# Get rabbitmq dashboard ID

https://grafana.com/grafana/dashboards/10991-rabbitmq-overview/

In this site we can copy the rabbitmq-overview dashboard ID. Click in button page to copy dashboard ID

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/grafana-id-dashboard-page-button.png?raw=true)

# Add new grafana datasource

http://localhost:3000

In home page click in "Add your first data source"

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/grafana-add-data-source.png?raw=true)

Select Prometheus option

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/prometheus-option.png?raw=true)

Add http://prometheus:9090 url in field

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/prometheus-url.png?raw=true)

Save & test

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/save-datasource.png?raw=true)

# Import grafana dashboard

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/import-grafana-dashboard.png?raw=true)

Now we past grafana dashboard ID in field and click in load button

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/import-grafana-dashboard-load.png?raw=true)

after loaded select prometheus datasource

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/select-prometheus-datasource.png?raw=true)

Finally click in import

# Welcome to grafana rabbitmq monitor

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/rabbitmq-grafana-monitor.png?raw=true)

# Show random values in grafana rabbitmq dasboard

## Setup environment

### # Optional virtualenv

```
virtualenv venv
source venv/bin/activate
```

## Install libs

```
pip install -r requirements.txt
```

## Produce messages

```
python producer.py
```

## Consume messages

```
python worker.py
```

## Change the number of messages the consumer gets on each call

```python
# alter prefetch_count
channel.basic_qos(prefetch_count=1000)
```

# Use prefetch_count with care. If your app can't process a lot of messages, consider using prefetch_count=1 to have other consumers work together

# How producer works?

Producer create a handle fake message:

```python
message = {
        "name": fake.name(),
        "email_id": fake.email(),
        "address": fake.address()
        }
```

and send 5000000000 message in a for loop

```python
for i in range(1, 5000000000):
    message = {
        "name": fake.name(),
        "email_id": fake.email(),
        "address": fake.address()
        }
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    print(" [x] Sent %r" % json.dumps(message))
```

## random message example

> Random name

> Random email_id

> Random address

```
[x] Received '{"name": "Travis Wilcox", "email_id": "nguyenjustin@example.net", "address": "082 Adams Isle\\nSouth Colleenmouth, DE 51675"}'
```

# Dashboard

Runs producer.pyand wait a few minutes to show data in dashbard and after runs worker.py to consume

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/console.png?raw=true)

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/dashboard-demo.png?raw=true)
