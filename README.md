# Personal blog on Django

<div align="center">
    <img width="1324" alt="Снимок экрана 2022-12-07 в 17 40 02" src="https://user-images.githubusercontent.com/90391143/206212492-f5632823-f773-4836-b211-7c3c75d0fdb9.png">
</div>

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
cd blogpro/
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver #localhost
```
[#localhost](http://127.0.0.1:8000/)

## All detailed information in the [django documentation](https://docs.djangoproject.com/en/4.1/)

Currently implemented user registration, login / logout , profile , edit profile.

<div align="center">
<img width="776" alt="Снимок экрана 2022-12-07 в 17 40 53" src="https://user-images.githubusercontent.com/90391143/206213794-6cbf5d13-c3a2-4d12-99b8-9af3f3f5421e.png">
</div>
