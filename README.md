# many-api-calls
Exploring background jobs to make many api calls via deployment on Kubernetes using Helm 

Scenario:  I am integrating with a third-party billing service.  In order to charge for 'usage' when the service generates monthly invoices, I need to make many API calls to the service to record what my customers have used.

To do this, I'll use a CSV file that represents usage data.  In reality these events might be coming from various other systems.

I'll use Python and Pandas to read the CSV file, then send tasks to RabbitMQ that Celery workers will process.

First, I'll get this running with docker-compose to start the three containers -- the app, the Celery workers, and RabbitMQ -- and execute the code.

Then I'll learn how to write a Helm chart to deploy it all to Kubernetes.
