from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mariadb
import sys
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://frontend:3000",
    "http://frontend:3000/",
    "http://localhost:8300",
    "http://localhost:8300/",
    "http://bakcend:8000",
    "http://0.0.0.0:3000",
    "http://0.0.0.0:8000",
    "http://0.0.0.0:8300",
    "http://0.0.0.0:8200",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Remplace * par l'URL de ton frontend en production
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
# # Middleware pour les logs détaillés
# class LoggingMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request, call_next):
#         # Log des détails de la requête entrante
#         print("Received request:")
#         print(f"  URL: {request.url}")
#         print(f"  Method: {request.method}")
#         print("  Headers:")
#         for name, value in request.headers.items():
#             print(f"    {name}: {value}")
#         print("  Query Parameters:")
#         for name, value in request.query_params.items():
#             print(f"    {name}: {value}")
#         # Appel de la suite du traitement
#         response = await call_next(request)
#         # Log de la réponse
#         print("Sent response:")
#         print(f"  Status Code: {response.status_code}")
#         print("  Headers:")
#         for name, value in response.headers.items():
#             print(f"    {name}: {value}")
#         return response

# # Ajout du middleware de logging
# app.add_middleware(LoggingMiddleware)


# Connexion à la base de données MariaDB
def connect_db():
    conn = mariadb.connect(
        user="root",
        password="",
        host="db",
        port=3306,
        database="cyka"
    )
    return conn


def get_cursor(conn):
    return conn.cursor()


@app.get("/")
async def read_root():
    return {"Message": "Hello World"}

@app.get("/test")
async def read_test():
    return {"Test": "ceci est un test"}

# Modèle Pydantic pour représenter les données
class Auteur(BaseModel):
    nom: str
    prenom: str

# Routes CRUD

@app.get("/api/auteurs")
def read_auteurs():
    cursor = get_cursor(connect_db())
    try:
        cursor.execute("SELECT id_auteur, nom, prenom FROM Auteur")
        result = cursor.fetchall()
        if result:
            return [{"id_auteur": row[0], "nom": row[1], "prenom": row[2]} for row in result]
        else:
            raise HTTPException(status_code=404, detail="Aucun auteur trouvé")
    except mariadb.Error as e:
        raise HTTPException(status_code=500, detail="Erreur lors de la lecture des auteurs")

@app.get("/api/auteurs/{id}")
def read_auteur(id: int):
    cursor = get_cursor(connect_db())
    try:
        cursor.execute("SELECT id_auteur, nom, prenom FROM Auteur WHERE id_auteur=?", (id,))
        result = cursor.fetchone()
        if result:
            return {"id_auteur": result[0], "nom": result[1], "prenom": result[2]}
        else:
            raise HTTPException(status_code=404, detail="Auteur non trouvé")
    except mariadb.Error as e:
        raise HTTPException(status_code=500, detail="Erreur lors de la lecture de l'auteur")

@app.post("/api/auteurs/create")
def create_auteur(auteur: Auteur):
    cursor = get_cursor(connect_db())
    try:
        cursor.execute("INSERT INTO Auteur (nom, prenom) VALUES (?, ?)", (auteur.nom, auteur.prenom,))
        connect_db().commit()
        return {"message": "Auteur créé avec succès"}
    except mariadb.Error as e:
        raise HTTPException(status_code=500, detail="Erreur lors de la création de l'auteur")
    

# @app.put("/items/{item_id}/")
# async def update_item(item_id: int, item: Item):
#     try:
#         cursor.execute("UPDATE items SET name=?, description=? WHERE id=?", (item.name, item.description, item_id))
#         conn.commit()
#         return {"message": "Item mis à jour avec succès"}
#     except mariadb.Error as e:
#         print(f"Error: {e}")
#         return {"message": "Erreur lors de la mise à jour de l'item"}

# @app.delete("/items/{item_id}/")
# async def delete_item(item_id: int):
#     try:
#         cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
#         conn.commit()
#         return {"message": "Item supprimé avec succès"}
#     except mariadb.Error as e:
#         print(f"Error: {e}")
#         return {"message": "Erreur lors de la suppression de l'item"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
