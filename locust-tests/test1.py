import settings
from locust import HttpUser, task


class QuickstartUser(HttpUser):

    @classmethod
    def access_configs(self):
        return {"cert": settings.cert, "proxy": settings.proxy}

    ####### API ########
    # 403, but not from Pulp!?
    # I could see 3xx in pulp-api logs, but the metrics are incrementing 4xx
    # @task
    # def forbidden(self):
    #    self.client.get("/api/pulp/api/v3/status",proxies=self.proxy)

    # 200
    @task
    def list_rpm_distributions(self):
        self.client.get(
            "/api/pulp/hyagi/api/v3/distributions/rpm/rpm/",
            proxies=self.proxy,
            cert=self.cert,
        )

    # random url to receive 404 from pulp-api and not reverse-proxy
    @task
    def not_found(self):
        self.client.get(
            "/api/pulp/hyagi/api/v3/containers/distribution/distribution/",
            proxies=self.proxy,
            cert=self.cert,
        )

    ####### CONTENT ########
    ## 500
    # @task
    # def content_list(self):
    #    self.client.get("/api/pulp-content/hyagi/test-rpm/Packages/f/fox-1.1-2.noarch.rpm",proxies=self.proxy,cert=self.cert)

    ## 500
    # @task
    # def internal_server_error(self):
    #    self.client.get("/api/pulp-content/hyagi/test/1.iso",proxies=self.proxy,cert=self.cert)
