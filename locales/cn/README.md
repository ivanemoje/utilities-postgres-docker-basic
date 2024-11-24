# 使用 Docker 设置 PostgreSQL 容器
PostgreSQL 是一个功能强大的开源关系数据库管理系统。在本存储库中，我们将介绍使用 Docker 启动 PostgreSQL 容器的过程。

我们还将建立一个基本的 Python 项目结构，以便与数据库交互。

## 前提条件
- [Docker](https://www.docker.com/)

## 项目结构
首先，我们来设置项目结构。为你的项目创建一个新目录，并添加以下文件：

```markdown
postgres-docker/
│
├── .gitignore
├── Dockerfile
├── main.py
├── requirements.txt
└── database.py
├── images/
├── .gitignore
```

## 运行
执行
Powershell
docker compose up -d
```
重建
Powershell
docker compose up --build -d
```
## TODO
- 添加 .env

## 技术
Powershell
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-docker-basic-db-1
```
应该会显示 172.18.0.2