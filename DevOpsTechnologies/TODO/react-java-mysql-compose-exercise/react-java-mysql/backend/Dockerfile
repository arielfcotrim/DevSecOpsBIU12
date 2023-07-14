# Use the official maven/Java 8 image to create a build artifact.
# https://hub.docker.com/_/maven
FROM maven:3.8.1-openjdk-8-slim as builder

# Copy local code to the container image.
WORKDIR /app
COPY . .

# Build a release artifact.
RUN mvn clean package

# Use AdoptOpenJDK for base image.
# It's important to use OpenJDK 8u191 or above that has container support enabled.
# https://docs.docker.com/samples/java/
FROM adoptopenjdk:8-jre-hotspot

# Copy the jar to the production image from the builder stage.
COPY --from=builder /app/target/*.jar /app.jar

# Run the web service on container startup.
CMD ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
