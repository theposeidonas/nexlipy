# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Nexlipy Framework](https://github.com/theposeidonas/nexlipy).

## [0.2.0] - 2024-09-17

### Added

-   **Error Handling:** Implemented `errors/error_handler.py` to manage exceptions across modules.
    -   Added `ModuleFailedException` for handling modules that exceed maximum retry attempts.
    -   Integrated logging configuration to record errors and events in `logs/service.log`.
-   **Configuration:** Set up `config/service.yaml` to manage service behavior and retry attempts.
-   **Module Structure:** Created `modules/Hello` with `Hello` class to demonstrate module operations.
-   **Threading Support:** Introduced threading in `main.py` to allow modules to run concurrently.

### Changed

-   **Logging Enhancements:** Updated logging format to include class names instead of function names.
    -   Ensured logs are encoded in UTF-8 for proper character display.
-   **Error Handler Improvements:** Modified `error_handler` to access the `name` attribute of classes.
-   **Main Service Loop:** Refined `start_service()` in `main.py` for better module execution flow.
    -   Added checks and balances to ensure modules run continuously without premature termination.

### Fixed

-   **Single Execution Issue:** Resolved an issue where modules only executed once if no error occurred. Implemented loops and threading to ensure continuous execution.
-   **Log Encoding:** Fixed encoding issues in `service.log` by specifying UTF-8 encoding in logging configuration.
-   **Function vs Class Names in Logs:** Corrected the logging output to display class names instead of function names in error messages.
-   **Requirements file issue:** Fixed requirements file issues.

## [0.1.0] - 2024-09-04

### Added

-   **Initial Release:** Set up the basic structure of the `Nexlipy` project.
    -   Created `main.py` with a foundational service loop.
    -   Established `modules` directory for modular development.
-   **Module Loader:** Implemented `load_modules()` function to dynamically load modules.
-   **Configuration Files:** Added initial configuration files for service settings.