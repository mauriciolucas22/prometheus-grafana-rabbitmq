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

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/select-prometheus-datasource.png?raw=true)

Now click import

# Welcome to grafana rabbitmq monitor

![alt text](https://github.com/mauriciolucas22/prometheus-grafana-rabbitmq/blob/main/images/rabbitmq-grafana-monitor.png?raw=true)
