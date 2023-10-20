# Wait database service.
wait_database() {
while ! nc -z database 5432; do
  echo "Waiting for PostgreSql to start..."
  sleep 1
done
}

server() {
  # Wait database before run backend
  wait_database

  echo "Start migrations"
  alembic upgrade head

  echo "Start server"
  uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 8000 --reload
}

$1
