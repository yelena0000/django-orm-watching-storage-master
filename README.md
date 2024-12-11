# Bank security console
This is an internal repository for employees of one bank. If you have accidentally accessed this repository, you won’t be able to run it since you don’t have access to the database. However, you are free to use the layout code or explore how database queries are implemented.
The Security Console is a website that can connect to a remote database containing information about employee visits and access cards in our bank.

### How to install
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```
Configure environment variables. Create a `.env` file in the project's root directory and fill it with the following values:
```env
DATABASE_ENGINE=<database engine>
DATABASE_HOST=<database host address>
DATABASE_PORT=<database port>
DATABASE_NAME=<database name>
DATABASE_USER=<database user>
DATABASE_PASSWORD=<database password>
SECRET_KEY=<Django secret key>
DEBUG=<True or False for debug mode>
```
Run the development server:
```bash
python manage.py runserver 127.0.0.1:8000
```

The application will be available at: <http://127.0.0.1:8000>
### Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.