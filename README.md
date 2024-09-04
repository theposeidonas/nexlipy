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

### Notes

Please keep in mind that this framework was created entirely as a personal project for my Linux server to meet amateur needs. If you would like to support the project, feel free to report issues or feature requests in the Issues section. You are welcome to contribute to the project in any way you like. If you'd like to improve or optimize any parts of the project, feel free to submit a pull request. Thank you in advance for your interest and support!