FROM python:3.12-slim AS builder
# from baseimage:tag As stage. uses python:3.12-slim lightweight slim image
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#stage2- runner
#FROM  python:3.12-slim AS runner
#WORKDIR /app
#COPY --from=BUILDER /usr/local /usr/local
COPY . .
RUN playwright install --with-deps chromium
CMD [ "pytest","tests/","-v","--cov-report=xml" ]



