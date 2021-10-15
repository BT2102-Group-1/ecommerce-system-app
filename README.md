# E-commerce System App (OSHES)
## BT2102 Group 1

### Members
- Goh Hong Pei
- Kee Xian Hui
- Keith Charles Chan Yao Song
- Lyn Tan
- Remus Kwan Hao Hui
- Yee Dong Ying, Megan

### Procedure to Run
To run the database, open MySQL Workbench and run `Database.sql` and `Insert.sql`. Skip the first line from `Database.sql` if you do not have a database `oshes`.

To run the app:
```
$ cd ecommerce-system-app
$ pip install -r requirements.txt
$ python app.py
```

Alternatively, if you wish to use a virtual environment and are accessing through our submission.zip:
```
# For MacOS/Linux
$ source venv/activate/bat

# For Windows
$ pip install -U virtualenv
$ virtualenv --system-site-packages -p python ./venv
$ .\venv\Scripts\activate
```