import pytest
import os.path
import src.app.csv
import sqlite3
import loader


@pytest.fixture
def setup_database(self):
    

def AssertDate(self, setup_database):
    cur = setup_database
    assert (cur.execute('SELECT * FROM CASH_REGISTRY') == '01/01/2000')    
    
def AssertCashAmount(self, setup_database):
    cur = setup_database
    assert (cur.execute('SELECT * FROM CASH_REGISTRY') == 100)    

def AssertCardAmount(self, setup_database):
    cur = setup_database
    assert (cur.execute('SELECT * FROM CASH_REGISTRY') == 102)    

def AssertTotalExpense(self, setup_database):
    cur = setup_database
    assert (cur.execute('SELECT * FROM CASH_REGISTRY') == 120)    
