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
<div align="center">
     <img width="1434" alt="Снимок экрана 2022-12-08 в 00 43 16" src="https://user-images.githubusercontent.com/90391143/206302987-7d3ce402-390f-41b6-b95f-478bf76882e7.png">
</div>

## run server:

```bash
cd blogpro/
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver #localhost
```
[#localhost](http://127.0.0.1:8000/)

## All detailed information in the [django documentation](https://docs.djangoproject.com/en/4.1/)

Currently implemented user registration, login / logout , profile , edit profile, posts.

<div align="center">
    <img width="1202" alt="Снимок экрана 2022-12-08 в 00 40 39" src="https://user-images.githubusercontent.com/90391143/206303329-1f8f1564-2e09-42b8-a91c-f07ff5ee931d.png">
</div>
