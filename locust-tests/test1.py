import settings
from locust import HttpUser, task


class Test1(HttpUser):

    ####### API ########
    # 200
    @task
    def list_rpm_distributions(self):
        self.client.get(
            "/api/pulp/hyagi/api/v3/distributions/rpm/rpm/",
            proxies=settings.proxy,
            cert=settings.cert,
        )

    # random url to receive 404 from pulp-api and not reverse-proxy
    @task
    def not_found(self):
        self.client.get(
            "/api/pulp/hyagi/api/v3/containers/distribution/distribution/",
            proxies=settings.proxy,
            cert=settings.cert,
        )

    ####### CONTENT ########
    ## 500
    # @task
    # def content_list(self):
    #    self.client.get("/api/pulp-content/hyagi/test-rpm/Packages/f/fox-1.1-2.noarch.rpm",proxies=settings.proxy,cert=settings.cert)

    ## 500
    # @task
    # def internal_server_error(self):
    #    self.client.get("/api/pulp-content/hyagi/test/1.iso",proxies=settings.proxy,cert=settings.cert)
