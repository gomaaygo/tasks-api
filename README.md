# ✨ TASK API PROJECT ✨

This project consists of a task manager. It includes user management and their respective tasks. Below are the instructions needed to install and run the application.


## 📦 Tools you’ll need

- Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) on your machine.
- Install [Redis] (https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/)

## 📁 Clone the repository

```bash
git clone https://github.com/gomaaygo/tasks-api
cd tasks-api
```

## ⚙️ Configure the environment

1. Copy the sample .env file
```bash
cp .env.example .env
```

2. Edit the .env with your settings (ex: SECRET_KEY, database name...).


## 🛠️ Migration permission and automatic creation of administrator user

Run this command to grant execution permission to this file. This is where the database migrations are made and an administrator user is created to access the application's dashboard.
```bash
chmod +x entrypoint.sh
```

## 🐳 Starting containers with docker
```bash
docker-compose up --build
```

## 🎉 The api is running!

- Access the home: http://localhost:8000/
- Access the administrative panel at: http://localhost:8000/admin

Credentials
- user: admin
- password: adminpass

