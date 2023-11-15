from flask import Flask,request,jsonify
import wikipedia

app=Flask(__name__)


@app.get("/<prompt>")
def getresult(prompt):
    try:
        return {"status":1,"result":wikipedia.summary(prompt)}
    
    except:
        return {"status":0,"result":"Not Found"}
        
    


if(__name__=="__main__"):
    app.run(debug=True)


