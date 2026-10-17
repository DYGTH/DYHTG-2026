FROM node:24-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

FROM busybox:1.30 AS runner
WORKDIR /app
COPY --from=builder /app/dist .
RUN printf '.js:text/javascript\n.mjs:text/javascript\n.json:application/json\n.svg:image/svg+xml\n.png:image/png\n.jpg:image/jpeg\n' > /etc/httpd.conf
CMD ["busybox", "httpd", "-f", "-v", "-p", "5174", "-c", "/etc/httpd.conf"]
