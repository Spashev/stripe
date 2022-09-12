# Python 3 + Django 4.* + PgsSql + VueJs3 + Docker + Nginx 

## Развертывание тестового проекта

### ENV
<pre>
cp .env.xample .env
</pre>

### 1) Makefile Deployment
<pre>make install</pre>

### 2) Create superuser
<pre>
make shell
python manage.py createsuperuser
</pre> 

### Run all containers
<pre>
make test
</pre>

### Stop all containers
<pre>
make stop
</pre>

### Run tests
<pre>
make test
</pre>

### Run migrations
<pre>
make migrate
</pre>

### Destroy all docker containers
<pre>
make destroy
</pre>
