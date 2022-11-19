.PHONY: install
install:
	apt install -y --no-install-recommends apt-utils gettext python3-dev gcc g++ libffi-dev zlib1g-dev
	python3 -m venv env
	. ./env/bin/active && pip install -r requirements.txt
	cp /var/www/gcp-cloud/systemd/gcp-cloud-demo-app.service /etc/systemd/system/
	service gcp-cloud-demo-app.service start
	service gcp-cloud-demo-app.service enable
