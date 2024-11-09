from fastapi import FastAPI
from loguru import logger
import argparse
from router import router

@logger.catch
def main():
    app = FastAPI()
    app.include_router(router)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store", default=7777)
    args = parser.parse_args()

    port = int(args.port)
    uvicorn.run(app, host="0.0.0.0", port=port, access_log=False)

if __name__ == "__main__":
    import uvicorn
    main()