import uvicorn
from fastapi import FastAPI

from config import DatabaseSession

from graphql_.query import Query
from graphql_.mutation import Mutation

import strawberry
from strawberry.fastapi import GraphQLRouter

def init_app():
    db = DatabaseSession()
    app = FastAPI(
        title="GraphQL and FastApi",
        description="This is a GraphQL API with FastApi",
        version="1.0.0"
    )

    @app.on_event('startup')
    async def startup():
        await db.create_all()
    
    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    @app.get('/')
    def home():
        return "Works!!"

    # Graphql endpoint
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    app.include_router(graphql_app, prefix="/graphql")

    return app

app = init_app()

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=8888, reload=True)