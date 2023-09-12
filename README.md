# 💰 FlogIt: Demonstrative Auction Platform

Welcome to **FlogIt**, my illustrative auction platform project. Crafted with precision and modern development practices, this README provides a comprehensive overview of the technologies, methodologies, and architectural choices that underpin this demo project.

## ✨ Core Functionalities

- **Real-time Bidding**: Seamlessly participate in live auctions, placing and updating bids in real-time.
- **User Authentication**: A robust mechanism ensuring secure user registration and login.
- **Notifications**: Real-time alerts on bid activities and auction progress.
- **Search**: Efficiently locate auctions and specific items.

## 🛠️ Technical Stack & Architecture

- **Frontend**: Utilized Next.js, capitalizing on its capabilities to create a dynamic and responsive user interface.
- **Backend**: Developed on the ASP.NET Core microservices framework. Duende IdentityServer is integrated for authentication, SignalR for real-time interactions, and RabbitMQ for asynchronous messaging.
- **Databases**: Chose PostgreSQL for its robustness in handling relational data and MongoDB for its flexibility with NoSQL storage.
- **Infrastructure**: Orchestrated the entire setup using Kubernetes, ensuring seamless container management and deployment.

## 🌍 Deployment Overview

- **Live Application**: Experience the platform firsthand at [FlogIt Demo App](https://app.flogitdemoapp.uk).
- **Identity Server**: Isolated hosting to optimize authentication processes.
- **Microservices**: Hosted on cloud-based Kubernetes clusters, emphasizing scalability and resilience.

## 🌐 Frontend Services

### Web Application

Constructed with the [Next.js](https://nextjs.org/) framework, the web application ensures an intuitive user experience. It communicates with backend services, providing users with real-time auction and bidding functionalities.

## 🔧 Backend Services

### Auction Service

- **Framework**: ASP.NET Core
- **Functionality**: Centralized management of auction activities. Integrates with RabbitMQ for synchronous updates and provides endpoints for auction-related tasks.

### Bidding Service

- **Framework**: ASP.NET Core
- **Functionality**: Handles bid lifecycle, liaising with the Auction Service using gRPC. RabbitMQ assists in delivering instantaneous bid notifications.

### Gateway Service

- **Framework**: ASP.NET Core
- **Functionality**: Manages incoming requests, ensuring they're dispatched to the appropriate service.

### Identity Service

- **Framework**: Duende IdentityServer
- **Functionality**: Oversees authentication and authorization, dispensing JWT tokens for verified sessions.

### Notification Service

- **Framework**: ASP.NET Core SignalR
- **Functionality**: Ensures users receive real-time notifications, leveraging the capabilities of SignalR and RabbitMQ.

### Search Service

- **Framework**: ASP.NET Core
- **Functionality**: Provides efficient item search capabilities, interacting with the Auction Service and utilizing RabbitMQ for real-time updates.

## 🚀 Microservice Architecture

Each microservice in FlogIt is optimized for deployment within a Kubernetes environment:

- **Auction Service**: Encapsulated within the `dionupton/auction-svc` container and integrated with RabbitMQ.
- **Bidding Service**: Housed in the `dionupton/bid-svc` container, it establishes connections with RabbitMQ and the Auction Service.
- **Gateway Service**: Operates from the `dionupton/gateway-svc` container.
- **Notification Service**: Positioned in the `dionupton/notify-svc` container.
- **Search Service**: Located in the `dionupton/search-svc` container.

## 🗄️ Database Infrastructure

- **PostgreSQL**: Employed for its reliability and ACID-compliant properties.
- **MongoDB**: Chosen for its adaptability in handling dynamic data structures.

## 🔄 GitHub CI/CD Integration

The project integrates a CI/CD pipeline, ensuring automated testing, building, and deployment. This approach guarantees code quality and streamlined deployments, reflecting industry best practices.
