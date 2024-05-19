from fastapi import FastAPI
from fastapi_pagination import add_pagination
from workout_api.routers import api_router
from workout_api.centro_treinamento.routes import router as centro_treinamento_router

app = FastAPI(title='WorkoutApi')

# Inclua o api_router já existente no api
app.include_router(api_router)

# Adiciona a Rota que crie  o centro_treinamento_router com o prefixo
app.include_router(centro_treinamento_router, prefix="/centros_treinamento")

# Adicione a paginação
add_pagination(app)

# Inicialização do servidor necessaria sem isso estava dando erro 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

