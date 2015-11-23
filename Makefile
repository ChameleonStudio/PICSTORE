VENV = /home/daniel/Desktop/taxi/venv/bin/activate

locale_update:
	bash -c "source $(VENV) && \
		python manage.py generate_po_dummy && \
		python manage.py xmakemessages -l ru --verbosity=1 --ignore 'venv/*' --ignore 'static/*'"

locale_compile:
	bash -c "cd locale/ru/LC_MESSAGES && msgfmt -o django.mo django.po"