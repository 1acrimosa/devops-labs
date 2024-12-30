resource "docker_image" "portainer" {
  name = "portainer/portainer-ce:latest"
}

resource "docker_container" "portainer" {
  name  = "portainer"
  image = "portainer/portainer-ce"
  ports {
    internal = 9000
    external = 9001
  }

  restart = "unless-stopped"

}
