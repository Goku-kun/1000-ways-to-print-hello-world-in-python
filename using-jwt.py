## Require  pip install pyjwt
## Create new jwtcode -> https://jwt.io

import jwt
key = "secret"
myJwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSGVsbG8gV29ybGQifQ.O6NCuG8GMD9AGrRXlLQSH1NlYZq3IZbj6plokX5gYos"
decode = jwt.decode(myJwt, key, algorithms="HS256")

print(decode["name"]);

