problem set 1:

ANS -> REGEX -  r'"(?:id|code)":(\d+)'

problem set 3:

ANS -> 

I would prefer celery and i have handson experience with django celery.
For scheduling periodic tasks (like downloading ISINs every 24 hours), Celery with Celery Beat is a reliable choice in a Django-based system.

Why Celery?
Asynchronous & Distributed – Celery allows background tasks to run separately from the main application, preventing delays in request-response cycles.

Scheduled Tasks with Celery Beat – Celery Beat extends Celery to handle periodic tasks using Django’s database or Redis.

Reliability – It supports task retries, error handling, and monitoring with Flower.
Scalability – Celery works well with Redis/RabbitMQ, allowing horizontal scaling with multiple workers.

Is It Reliable & Scalable?
Reliability: Celery is battle-tested and widely used, but requires proper configuration (e.g., task acknowledgment, retries, monitoring).

Scalability Issues:

A single Celery worker can become a bottleneck if too many tasks are scheduled.
Redis as a broker may face memory constraints under heavy loads.
Task execution order is not guaranteed if many tasks are queued.

Alternatives for Production-Scale Workloads
Kubernetes CronJobs – Suitable for large-scale deployments, avoiding Celery’s limitations in task reliability.

Apache Airflow – Ideal for complex task dependencies and workflow management.

AWS Lambda + EventBridge – Serverless option with auto-scaling and no infrastructure overhead.

Redis Queue (RQ) or Dramatiq – Simpler alternatives to Celery if lightweight background processing is needed.

For a Django project requiring simple periodic tasks, Celery + Celery Beat is a great choice. However, at a larger scale, Airflow or Kubernetes-based scheduling is more robust.

B. Flask vs. Django – When to Use

Flask(i prefer for single page applications):
If Need a Lightweight & Flexible API – Flask is minimal and gives more control over architecture.

while Building a Microservice – Flask works well for APIs that don’t require a full-featured backend.

Performance – Less overhead than Django, making it faster for simple apps.

Django(dynamic - scallable web):
If Need a Full-Featured Web Framework – Django includes ORM, authentication, admin panel, and security features out-of-the-box.

While Building a Large, Scalable App – Django is structured and opinionated, making large projects easier to maintain.

IF Need an Admin Interface – Django’s built-in admin panel is useful for CRUD operations.

Security is a Priority – Django protects against SQL injection, CSRF, and XSS by default.