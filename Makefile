build:
	docker run --rm -ti \
		--user=`id -u`:`id -g` \
		-e HOME=/tmp \
		-v /etc/passwd:/etc/passwd:ro \
		-v `pwd`:/app/jellyfin-kodi \
		-w /app \
		python:3 \
		bash -c " \
		set -e ;\
		python3 -m pip install --user pyyaml; \
		python3 jellyfin-kodi/.config/generate_xml.py py2; \
		"
