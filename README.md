# Personal blog on Django

<!-- <div align="center"> -->

<!-- </div> -->

## Requirements

Everything you need is prescribed in the file ->

```bash
cat pyproject.toml
```

## Installation

Clone this repository:

```bash
git clone https://github.com/SSenpo/Personal_blog
```
and install poetry:
```bash
pip install poetry
```

Run poetry in repository dir :

```bash
poetry shell
poetry update package
```
<!-- <div align="center"> -->

<!-- </div> -->

## run server:

```bash
cd conventer_app/
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver #localhost
```
[#localhost](http://127.0.0.1:8000/)
<!-- <div align="center"> -->

<!-- </div> -->

## All detailed information in the [django documentation](https://docs.djangoproject.com/en/4.1/)