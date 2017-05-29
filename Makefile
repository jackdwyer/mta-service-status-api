build:
	docker build -t jackdwyer/mta-service-status-api:latest .

publish:
	docker push jackdwyer/mta-service-status-api:latest

run-dev:
	docker run -i -p 5000:5000 -v $(PWD):/opt/mta-service-status-api -t jackdwyer/mta-service-status-api python /opt/mta-service-status-api/app.py

work-dev: build
	docker run -i -p 5000:5000 -v $(PWD):/opt/mta-service-status-api -t jackdwyer/mta-service-status-api /bin/sh
