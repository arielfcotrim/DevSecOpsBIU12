FROM node:latest
WORKDIR /app
COPY ["package.json", "yarn.lock", "/app/"]
RUN yarn
COPY [".", "/app"]
CMD ["npm", "build"]
