terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0"
    }
    postgresql = {
      source = "cyrilgdn/postgresql"
      version = "~> 1.16"
    }
  }
}

provider "docker" {}
provider "postgresql" {
  host     = "localhost"
  port     = 5432
  username = "your_username"
  password = "your_password"
  sslmode  = "disable"
}
