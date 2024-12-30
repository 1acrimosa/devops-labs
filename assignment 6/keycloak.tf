resource "docker_container" "keycloak" {
  image = "quay.io/keycloak/keycloak:latest"
  ports {
    internal = 8080
    external = 8081
  }

  name = ""
}
