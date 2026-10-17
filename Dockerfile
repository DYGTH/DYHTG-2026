# syntax=docker/dockerfile:1

# FastAPI + Pydantic runtime
# (Frontend build stage removed until apps/frontend exists.)
FROM python:3.12-slim

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

RUN useradd --create-home appuser
USER appuser

WORKDIR /srv/backend
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
