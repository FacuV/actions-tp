from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from databases import Database
from src.models.User import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración de base de datos
database = Database('postgresql://root:admin@postgres/users')

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello world"
    }

@app.post("/users")
async def create_user(User: User):
    query = "INSERT INTO users (username, password) VALUES (:username, :password)"
    values = {"username": User.username, "password": pwd_context.hash(User.password)}
    try:
        await database.connect()
        await database.execute(query=query, values=values)
        await database.disconnect()
        return {"message": "User created successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    query = "SELECT * FROM users WHERE id = :user_id"
    values = {"user_id": user_id}
    try:
        await database.connect()
        result = await database.fetch_one(query=query, values=values)
        if result:
            user = User(id=result["id"], username=result["username"], password=result["password"])
            await database.disconnect()
            return user
        else:
            await database.disconnect()
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))