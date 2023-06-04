FROM node:latest
WORKDIR /app
COPY ["package.json", "yarn.lock", "/app/"]
RUN npm i
COPY [".", "/app"]
EXPOSE 3000
CMD ["npm", "start"]
