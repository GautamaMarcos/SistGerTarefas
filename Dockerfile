FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DATABASE_URL=postgres://usuario:@matheus#02@host:porta/sist_ger_tarefas
ENV DJANGO_SETTINGS_MODULE=sist_ger_tarefas.settings
ENV SUPABASE_URL=https://lsrdvqtgszvdfgowcmqp.supabase.co
ENV SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxzcmR2cXRnc3p2ZGZnb3djbXFwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjk1NTQ2NzksImV4cCI6MjA0NTEzMDY3OX0._oTK0ScLNnvzBTofrBoEAFY8SBWQqmX5W-HntYVSGbs
# ENV DATABASE_URL=postgres://usuario:senha@host:porta/sist_ger_tarefas
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput
EXPOSE 8000
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "sist_ger_tarefas.wsgi:application" ]