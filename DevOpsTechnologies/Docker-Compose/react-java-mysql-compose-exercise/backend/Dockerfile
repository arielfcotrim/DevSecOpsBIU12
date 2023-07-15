# Use Maven 3 and Java 11 to build the project.
FROM maven:3.8.1-openjdk-11 as build

# Set working directory for the image
WORKDIR /app

# Copy the pom.xml file.
COPY ./pom.xml ./pom.xml

# Download the dependencies.
RUN mvn dependency:go-offline -B

# Copy the rest of the application.
COPY . .

# Build a release artifact.
RUN mvn clean package

# Use AdoptOpenJDK for base image.
FROM adoptopenjdk:11-jdk-hotspot as runtime

WORKDIR /app

# Copy the jar file from the build stage.
COPY --from=build /app/target/*.jar ./app.jar

# Copy the wait script.
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

EXPOSE 8080

# Run the wait script before starting the application.
CMD ["/wait-for-it.sh", "db:3306", "--", "java", "-jar", "./app.jar"]
