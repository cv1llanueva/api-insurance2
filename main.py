from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "52.2.83.96"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_insurance2"  

# Obtener todos los siniestros
@app.get("/claims")
def get_claims():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM claims")
    result = cursor.fetchall()
    mydb.close()
    return {"claims": result}

# Obtener un siniestro por ID
@app.get("/claims/{id}")
def get_claim(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM claims WHERE id = {id}")
    result = cursor.fetchone()
    mydb.close()
    return {"claim": result}

# Agregar un nuevo siniestro
@app.post("/claims")
def add_claim(item:schemas.Claim):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    claim_number = item.claim_number
    policy_number = item.policy_number
    description = item.description
    amount = item.amount
    insured_person = item.insured_person
    date_of_incident = item.date_of_incident
    incident_location = item.incident_location
    date_filed = item.date_filed
    claim_status = item.claim_status
    adjuster_notes = item.adjuster_notes
    cursor = mydb.cursor()
    sql = """INSERT INTO claims (claim_number, policy_number, description, amount, insured_person, date_of_incident, 
             incident_location, date_filed, claim_status, adjuster_notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    val = (claim_number, policy_number, description, amount, insured_person, date_of_incident, incident_location, date_filed, claim_status, adjuster_notes)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Claim added successfully"}

# Modificar un siniestro
@app.put("/claims/{id}")
def update_claim(id:int, item:schemas.Claim):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    claim_number = item.claim_number
    policy_number = item.policy_number
    description = item.description
    amount = item.amount
    insured_person = item.insured_person
    date_of_incident = item.date_of_incident
    incident_location = item.incident_location
    date_filed = item.date_filed
    claim_status = item.claim_status
    adjuster_notes = item.adjuster_notes
    cursor = mydb.cursor()
    sql = """UPDATE claims set claim_number=%s, policy_number=%s, description=%s, amount=%s, insured_person=%s, 
             date_of_incident=%s, incident_location=%s, date_filed=%s, claim_status=%s, adjuster_notes=%s where id=%s"""
    val = (claim_number, policy_number, description, amount, insured_person, date_of_incident, incident_location, date_filed, claim_status, adjuster_notes, id)
    cursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    return {"message": "Claim modified successfully"}

# Eliminar un siniestro por ID
@app.delete("/claims/{id}")
def delete_claim(id: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM claims WHERE id = {id}")
    mydb.commit()
    mydb.close()
    return {"message": "Claim deleted successfully"}
