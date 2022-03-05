#-------------------- Imports -------------------- 

#---------- Flask imports ---------- 
from flask import Flask, render_template,request

#---------- SQLite imports ----------
import sqlite3 
#--------------------------------------------------


app = Flask(__name__)


#---------- Route to write the main code ----------
@app.route("/")
def main():
    return("Hello!")



#---------- Data Base ----------
conn = sqlite3.connect('tableName.db')
conn.execute('CREATE TABLE IF NOT EXISTS tade(col1 TEXT, col2 TEXT, etc TEXT)')
conn.close()


#---------- Set mode to development ----------
if __name__ == "__main__":
    app.run(debug=True)