# Project Woosh Test

## Overview

This project includes several modules for inventory quality check, custom api, and Uber Integration The project is built on Odoo 14 Community Edition and integrates various functionalities to enhance user experience and system capabilities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Inventory Quality Check](#inventory-quality-check)
  - [Custom API](#custom-api)
  - [Uber Integration](#uber-integration)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/muhrizky/woosh-test.git
   cd project-name
   ```
   **Alternative**:
extract the contents from the archive file.

2.  **Set up Odoo**
Follow Odoo's official documentation to install and configure Odoo.
Ensure that Odoo is properly set up and running before proceeding.
   
## Usage

### Inventory Quality Check

#### Short Description

This module customizes the Odoo Inventory (stock.picking) model by adding a new feature, enhancing the workflow, and implementing security and access control mechanisms

#### Key Features

* Ensure quality checks are tracked.
* Better workflow management.
* Prevents validation of stock picking unless quality checks are completed, ensuring quality standards.

#### Demo
[Watch the demo video](https://www.loom.com/share/8e13fd27f1b44b3198ba077919ffd38e?sid=8343d791-9555-49e0-a36d-4928eb8ebe63)

### Custom API

#### Short Description

This module provides JWT token-based authentication and HTTP API endpoints in Odoo for managing customers, products, and sales orders securely.

#### Key Features

* Single login endpoint with JWT token
* Active login limit per user 
* Single logout endpoint with JWT token
* **GET Customers:** Retrieves customer details including ID, name, email, and phone number.
* **GET Products:** Fetches product information such as ID, name, list price, and available quantity.
* **POST Sales Orders:** Creates new sales orders, invoices, and payments based on provided data.

#### Demo
[Watch the demo video](https://www.loom.com/share/7285c4845c574b83baa1af8ce26a68bc?sid=a67a1c7a-8747-42d6-92f6-72d5b1862619)

### Uber Integration

#### Short Description

This module integrates Uber's API into Odoo, facilitating the retrieval of Uber Eats orders. It includes methods to fetch an access token for authentication and retrieve orders from Uber Eats API endpoints

#### Key Features

* **Automatic Authentication**: Facilitates OAuth2 authentication to securely obtain access tokens for API interactions.
* **Uber API Integration**: Enables Odoo to interact with Uber's API for managing Uber Eats orders. **(On Development)**
#### Demo
[Watch the demo video](https://www.loom.com/share/c9d700fec2cf4c3eb3539b642a52a7c3?sid=32dbff86-48e2-46d3-a5d9-73e63816a0a3)


### Notes
* Complete documentation and usage guides will be provided later.
* Please contact [LinkedIn](https://www.linkedin.com/in/muhrizqi/) or [Email](muhrizqi.work@gmail.com) for any questions or issues.

### Version

* 1.0.0 (2024-06-26): Initial release.
