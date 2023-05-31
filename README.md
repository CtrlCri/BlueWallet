# BlueWallet Backend (Not Available Yet)

BlueWallet Backend is the backend component of the BlueWallet application, a virtual wallet platform developed in Django Rest Framework. It provides a robust API-REST for managing virtual wallets and conducting financial operations in Money-Market funds.

## Features

- Robust and scalable API-REST.
- Integration with PostgreSQL for data storage.
- Integration with Redis for cache management and optimal performance.
- Implementation of security measures through user authentication and authorization.
- Unit and integration testing to ensure code quality.

## System Requirements

- Python 3.x
- Django 3.x
- Django Rest Framework 3.x
- PostgreSQL
- Redis

## Setup and Execution

1. Clone this repository: `git clone https://github.com/CtrlCri/BlueWallet.git`
2. Navigate to the project directory: `cd bluewallet-backend`
3. Create and activate a virtual environment: `python3 -m venv venv && source venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Configure the environment variables in the `.env` file according to your preferences.
6. Apply the database migrations: `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

## Contributions

Contributions are welcome! If you'd like to contribute to this project, please create a pull request explaining your proposed changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
