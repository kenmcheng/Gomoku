import logging
from fastapi import FastAPI
import uvicorn

import api 

app = FastAPI(__name__)

def main():
    logging.info("App starting...")
    api.init(app)

main()

if __name__ == "__main__":
    uvicorn.run(app, debug=True, port=5000)