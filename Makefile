reset:
    # Make の実行環境が無い場合は 1行ずつ実行すれば良い
	- docker compose down;
	- docker volume rm sa-sand-db-volume;
	- docker volume rm sa-sand-poetry-volume;
	docker volume create sa-sand-db-volume;
	docker volume create sa-sand-poetry-volume;
	docker compose run api bash
