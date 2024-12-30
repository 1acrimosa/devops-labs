resource "docker_container" "postgres" {
  image = "postgres:latest"
  ports {
    internal = 5432
    external = 5434
  }
  name = ""
}
