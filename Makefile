migrate:
	@echo "Migrating database..."
	alembic upgrade head

run_dev: migrate
	@echo "Running server..."
	uvicorn src.main:app --host 0.0.0.0 --port 5000 --reload

run: migrate
	@echo "Running server..."
	gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000
