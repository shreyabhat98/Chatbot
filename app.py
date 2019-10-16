from flask import Flask, render_template, request
 #import pyodbc


app = Flask(__name__)

def service_bot():
    print("Hello! Welcome to the RBS Business Intelligence Service Portal. how may I help you? \n [1] I have trouble logging in \n [2] I have to report another issue")
    response_one = input("Please enter the number corresponding to your choice: ")
    if response_one == "1":
        access_issue()
    elif response_one == "2":
        call_ai_fun()
    else:
        print("Sorry, we didn't understand your selection.")
        service_bot()
'''def access_issue():
    #retrieve the url from the database (yet to be created)
    print("Please follow the instructions in the given url.")
    import pyodbc 
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LONMS11504\DMLNFARM01;'
                      'Database=UBDWH;'
                      'Trusted_Connection=no;'
                      'UID=App_Archive_User_Dev;'
                      'PWD=Welcome2rbs@2017;')
                      

    cursor = conn.cursor()
    cursor.execute('select * from ubdwh.dbo.url')
    rows = cursor.fetchone()
 
    for row in rows:
        print (str(row)) 
   
    ans=input("\n Is there anything I could help you with?")
    if ans=="yes":
        service_bot()
    else:
        print("Thank you for reaching out. Hope I could be of some help") '''
        
        
@app.route("/ai")        
def call_ai_fun():
    #ask for the problem
    
  #prob=input("Hi! What is the problem you are facing?")
     #rackf=input("what is your rackf?")
    # domain=input("what is your domain?")
   #  log=input("Have you logged in before?")'''
    import pyodbc 
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LONMS11504\DMLNFARM01;'
                      'Database=UBDWH;'
                      'Trusted_Connection=no;'
                      'UID=App_Archive_User_Dev;'
                      'PWD=Welcome2rbs@2017;')
                      

    cursor = conn.cursor()
    #insertQuery = "insert into UBDWH.dbo.chat (rackf, domain) values(\'"+rackf+"\',\'"+domain+"\')"
    #print(insertQuery)
   # cursor.execute(insertQuery)
   # conn.commit()
    cursor.close()
    return "test"
   
 # if log=="yes":
    #     date_time=input("When was the last time you logged in? Please provide us the date and approximate time")
   #  else:
   #      impact=input("Does it impact only you?")
   #      if impact=="yes":
  #          print("We are sorry to know that.We will definitely help you out")
      #   else:
         #    ref_rackf=print("Please give us the rackf of the other person who has the same problem")'''
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def access_issue():
    #retrieve the url from the database (yet to be created)
  #  return "Please follow the instructions in the given url."
    import pyodbc 
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LONMS11504\DMLNFARM01;'
                      'Database=UBDWH;'
                      'Trusted_Connection=no;'
                      'UID=App_Archive_User_Dev;'
                      'PWD=Welcome2rbs@2017;')
                      

    cursor = conn.cursor()
    cursor.execute('select * from ubdwh.dbo.url')
    rows = cursor.fetchone()
 
    for row in rows:
        #userInput=request.args.get('msg')
        return str(row)
    
    #userInput=request.args.get('msg')

   
   # ans=input("\n Is there anything I could help you with?")
    #if ans=="yes":
    #    service_bot()
    #else:
     #   print("Thank you for reaching out. Hope I could be of some help")
#def get_bot_response():
 #   userText = request.args.get('msg')
  #  return str(get_response(userText))

if __name__ == "__main__":
    app.run()
