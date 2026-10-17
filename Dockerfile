# syntax=docker/dockerfile:1

# ---- Stage 1: build the React frontend ----
FROM node:22-alpine AS frontend-build
WORKDIR /frontend

COPY apps/frontend/package*.json ./
RUN npm ci

COPY apps/frontend/ ./
RUN npm run build   # outputs to /frontend/dist (Vite default; use "build" for CRA)


# ---- Stage 2: FastAPI + Pydantic runtime ----
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/srv/packages

WORKDIR /srv

COPY apps/backend/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Backend code and the shared Pydantic models
COPY apps/backend/ ./backend/
COPY packages/ ./packages/

# Built frontend, served by FastAPI as static files
COPY --from=frontend-build /frontend/dist ./backend/static

RUN useradd --create-home appuser
USER appuser

WORKDIR /srv/backend
EXPOSE 8000

# Expects apps/backend/app/main.py to define `app = FastAPI()`
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
