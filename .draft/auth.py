from typing import Annotated

from fastapi import Depends, FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware

from src import __version__
from src.api.v1.routers import v1


app = FastAPI(title="Dotflow", description="Dotflow API", version=__version__)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1, prefix="/v1")


@app.get("/status", include_in_schema=False)
def get_status():
    """Get status of messaging server."""
    return {"status": "it's alive"}


def auth(authorization: Annotated[str | None, Header()] = None):
    parts = authorization.split()
    token = parts[1]

    import json
    import jwt

    from six.moves.urllib.request import urlopen

    jsonurl = urlopen("https://dotflow.us.auth0.com/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())

    try:
        unverified_header = jwt.get_unverified_header(token)
    except jwt.PyJWTError as jwt_error:
        raise Exception(
            {
                "code": "invalid_header",
                "description": "Invalid header. "
                "Use an RS256 signed JWT Access Token",
            },
            401,
        ) from jwt_error
    if unverified_header["alg"] == "HS256":
        raise Exception(
            {
                "code": "invalid_header",
                "description": "Invalid header. "
                "Use an RS256 signed JWT Access Token",
            },
            401,
        )

    breakpoint()

    public_key = None
    for jwk in jwks["keys"]:
        if jwk["kid"] == unverified_header["kid"]:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key:
        payload = jwt.decode(
            token,
            public_key,
            algorithms=["RS256"],
            audience="https://dotflow.us.auth0.com/api/v2/",
            issuer="dotflow.us.auth0.com",
        )

    return {"authorization": authorization}


@app.get("/auth", include_in_schema=False)
def get_auth(commons: Annotated[dict, Depends(auth)]):
    return commons
