from locust import HttpUser, task, between


class EsportsUser(HttpUser):
    wait_time = between(2, 4)

    @task
    def buscar_perfil_jogadores(self):
        self.client.get("/users", name="GET /users")