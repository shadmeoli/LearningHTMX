
# HTMX & FastAPI app

Simple HTMX and FastAPI app to help me understand HTMX and creating an app with it





## Tech Stack

**Client:** HTMX, TailwindCSS

**Server:** Python- FastAPI


## Run Locally

Clone the project

```bash
  git clone git@github.com:shadmeoli/LearningHTMX.git
```

Go to the project directory

```bash
  cd LearningHTMX
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Start the server

> using uvicorn 
```bash
  uvicorn main:app --reload
```

> using Gunicorn and uvicorn workers
```bash
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```



## Support

For support, email shadcodes@duck.com


