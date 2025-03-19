import mysql.connector as msq
connection=msq.connect(host="192.168.1.7",
                       port="3306",
                       unix_socket="run/mysqld/mysqld10.sock",
                       user="oskar",
                       password='@7221@031176kTA!@#')