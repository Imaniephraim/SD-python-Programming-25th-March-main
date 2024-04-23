import sqlite3
import random
import string
from fpdf import FPDF

class User:
    """Represents a User that buys a cinema seat"""
    database = 'cinema.db'
    
    # constructor
    def __init__(self, seat_id):
        self.seat_id = seat_id
        
    # method to get the price of the seat from the db
    def get_price(self):
        """Get the price pf a certain seat from the DB"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "SELECT price FROM seats WHERE seat_id = ?"
        cursor.execute(query, [self.seat_id])
        price = cursor.fetchall()[0][0] #[(1000,)]
        return price
    
    # A method to check if the seat is free
    def is_free(self):
        """Checks in the db if a seat is taken(free) or not"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "SELECT taken FROM seats WHERE seat_id = ?"
        cursor.execute(query, [self.seat_id])
        result = cursor.fetchall()[0][0] # 1 for taken or 0 for not taken
        
        if result == 0:
            return
        else:
            return False
        
    # A method to occupy a seat which is free
    def occupy(self):
        """Changes the value of taken in the DB from 0 to 1 if seat is free"""
        if self.is_free():
            """Checks in the db if a seat is taken(free) or not"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "UPDATE seats SET taken = ? WHERE seat_id = ?"
        cursor.execute(query, [1, self.seat_id])
        connection.commit()
        connection.close()
        
class Seat:
    """Represents a cinema seat that can be purchased"""
    
class Card:
    """Represents a bank card needed to finalise a seat purchase"""
    database = 'cinema.db'
    
    # constructor
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        
    def validate(self, price):
        """Checks if card is valid and has balance, subtract price of the seat from card balance"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "SELECT balance FROM card WHERE number = ? AND cvc = ?"  
        cursor.execute(query, [self.number, self.cvc])
        result = cursor.fetchall() #[(2000,)]
        
        if result:
            balance = result[0][0]
            if balance >= price:
                query = "UPDATE card SET balance = ? WHERE number = ? AND cvc = ?"
                cursor.execute(query, [(balance - price), self.number, self.cvc])
                connection.commit()
                connection.close()
                return True
            
        
class Ticket:
    """Represents a cinema ticket purchased by the user"""