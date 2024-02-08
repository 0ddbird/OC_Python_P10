.PHONY: rb rf sp

rb:
		python manage.py runserver

rf:
		cd front; yarn start

sp:
		python manage.py shell_plus