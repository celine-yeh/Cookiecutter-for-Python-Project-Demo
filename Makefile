package_name = cookiecutter_for_python_project_demo
docker_username = celineyeh

docker_opts = \
	--rm
docker_compose_opts = -f docker-compose.yml
docker_compose_up_opts =
pytest_opts = \
	-vvv \
	--cov=$(package_name) \
	--cov-branch \
	--cov-report=term \
	--cov-report=html \
	-m '$(TEST_MARK)'

APP_PORT ?= 4500
TEST_MARK ?= not large
VERSION ?= $(shell cat VERSION)
image = $(docker_username)/$(package_name)
image_base = $(docker_username)/$(image)_base
image_dev = $(docker_username)/$(image)_dev

export APP_PORT
export APP_IMAGE = $(image)
export APP_IMAGE_DEV = $(image_dev)
define docker_run_dev
	docker-compose $(docker_compose_opts) run $(docker_opts) dev $(1)
endef


build:
ifndef CI
	docker build --target base -t $(image_base) .
ifeq ("$(wildcard Pipfile.lock)","")
	$(MAKE) lock
endif
endif
	docker build --target dev -t $(image_dev) .
	docker build -t $(image) .

lock: docker_opts += --volume $(PWD):/workspace
lock:
	docker run $(docker_opts) $(image_base) pipenv lock

shell:
	$(call docker_run_dev,bash)

up:
	docker-compose $(docker_compose_opts) up $(docker_compose_up_opts)
	until docker-compose logs db 2>&1 | grep 'port: 3306  MySQL Community Server (GPL)'; do continue; done

down ps:
	docker-compose $@

lint:
	$(call docker_run_dev,pylint $(package_name) tests)

test:
	$(call docker_run_dev,pytest $(pytest_opts) tests)

test-large: TEST_MARK = large
test-large: docker_compose_up_opts = -d
test-large: up test down

bump-version:
ifeq ($(BUMP),)
	$(error BUMP=major|minor|patch make bump-version)
endif
	$(call docker_run_dev,bumpversion $(BUMP))

publish:
ifdef CI
ifneq ($(VERSION),$(TRAVIS_TAG))
	$(error TRAVIS_TAG $(TRAVIS_TAG) != $(VERSION))
endif
endif
ifeq ($(DOCKER_PASSWORD),)
	$(error DOCKER_PASSWORD=... make publish)
endif
	echo $(DOCKER_PASSWORD) | docker login -u $(docker_username) --password-stdin
	$(eval image_version = $(image):$(VERSION))
	$(eval image_latest = $(image):latest)
	docker tag $(image) $(image_version)
	docker tag $(image) $(image_latest)
	docker push $(image_version)
	docker push $(image_latest)
