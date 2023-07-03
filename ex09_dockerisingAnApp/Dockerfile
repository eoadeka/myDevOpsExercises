# # STAGE 1: Build app
FROM node:latest as builder

COPY testapp /testapp

WORKDIR /testapp

RUN npm install
RUN $(npm bin)/ng build

# # STAGE 2: run nginx to serve application
FROM nginx

COPY --from=builder /testapp/dist/* /usr/share/nginx/html/

EXPOSE 80