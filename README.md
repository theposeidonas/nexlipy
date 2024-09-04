# Nexlipy Framework Documentation
Nexlipy is a modular framework designed for creating persistent services on Linux-based servers. It allows developers to easily configure, schedule, and manage various modules that can run indefinitely or based on specific intervals. The framework provides a flexible structure for handling multiple service tasks, logging, API calls, and service behaviors. This documentation outlines the structure of Nexlipy and provides guidelines on how to build modules and services using the framework.

## Key Features:
<ul>
    <li>Modular architecture allowing for easy creation and management of service modules.</li>
    <li>YAML-based configuration for environment, scheduling, and API settings.</li>
    <li>Logging functionality to capture service behaviors and events.</li>
    <li>Ability to differentiate between development and production environments.</li>
    <li>Scheduling capabilities for modules with specific execution intervals.</li>
</ul>


## Install the Required Dependencies

All dependencies are listed in the requirements.txt file. Use the following command to install them:

`pip install -r requirements.txt`

## Configuration
The configuration is managed through a YAML file (service.yaml), which is located in the config/ directory. This file defines global settings for the service environment, API connections, logging, and scheduling.

## Project Structure
The Nexlipy framework follows a clean and organized structure:
```
nexlipy/
│
├── config/
│   └── __init__.py     # Loads configuration from service.yaml
│   └── service.yaml    # Configuration file for services, API, and logging
│
├── modules/            # Directory where service modules are stored
│   ├── __init__.py     # Loads and manages all modules
│   ├── Hello/          # Example module directory
│   │   └── __init__.py # Example service module
│
├── main.py             # Main script to start and run all services
└── README.md           # Project documentation
```

## Creating Modules
Service modules are defined within the modules/ directory. Each module must reside within its own directory and include an __init__.py file where the service logic is implemented.

### Example Module: modules/Hello/
The Hello module demonstrates how a service module can be created within the Nexlipy framework. Below is an example of how to define a simple service task that executes depending on the environment: