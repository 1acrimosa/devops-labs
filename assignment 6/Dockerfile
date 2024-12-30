FROM quay.io/keycloak/keycloak:latest

ENV KC_DB=postgres
ENV KC_DB_URL=jdbc:postgresql://postgresql:5432/keycloak
ENV KC_DB_USERNAME=your_username
ENV KC_DB_PASSWORD=your_password

EXPOSE 8080

ENTRYPOINT ["/opt/keycloak/bin/kc.sh", "start"]
