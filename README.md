# Project: IAM & Access Manager

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

Prerequisites

Make sure you have the following software installed on your system:

    Docker & Docker Compose: To run the containerized application.

    Git: To clone the repository.

## Introduction

In any organization, tracking "who has access to what" can quickly become complex. This project is a straightforward Identity and Access Management (IAM) system designed to solve that problem. Its primary goal is to provide a reliable, centralized source of truth for user permissions.

With this tool, you can easily grant, revoke, and—most importantly—audit user access to a variety of services, from internal dashboards to cloud infrastructure. The core feature is a simple API endpoint that allows you to see all permissions assigned to a specific user, making security reviews and compliance checks significantly easier.

The system is built on a robust and normalized **PostgreSQL** schema, ensuring data integrity and scalability.

## 📂 Project Structure

The repository is organized as a mono-repo with a clear separation between the frontend and backend services.

/
├── backend/          # Python (FastAPI) Backend Application
├── database/         # Contains the DB schema and migration scripts
├── frontend/         # React.js Frontend Application
├── docs/             # Documentation and assets like the DB diagram
├── .gitignore        # Specifies intentionally untracked files to ignore
└── docker-compose.yml # Orchestrates all services for local development

## 🏛️ Database Schema

The database architecture is designed to be scalable and normalized. Below is the Entity-Relationship Diagram (ERD) that illustrates the relationship between users, services, roles, and their accesses.

![Database Schema Diagram](./docs/images/db_schema.png)

* **Users**: Stores user information.
* **Services**: Defines the applications or platforms that users can access.
* **Roles**: Defines specific permissions within each service.
* **Accesses**: A join table that links a user to a role within a specific service.

### ⚙️ Installation & Running

1. Clone the Repository

2. Open your terminal and clone the project from GitHub, then navigate into the project directory.

```Bash
git clone https://github.com/[your-github-username]/iam-manager.git
cd iam-manager
```
Build and Run with Docker Compose

Execute the following command from the project's root directory. This single command will build the necessary Docker images and start all the services in the background.

```Bash
docker-compose up -d --build
```
This process will:

🚀 Start the PostgreSQL database server.

📝 Automatically create all required tables by running the schema.sql script on the first launch.

🐍 Launch the Python (FastAPI) backend API.

⚛️ Launch the React frontend application.