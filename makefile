DATE=`date -Iminutes`
MSG=$(DATE) - Automatic commit from build
PYTHON=python
SH=sh
GIT=git

all: build deploy commit

dev: build deploy

build:
	$(PYTHON) build.py

deploy:
	$(SH) deploy.sh

commit:
	$(GIT) add . --all
	$(GIT) commit -a -m "$(MSG)" --allow-empty

