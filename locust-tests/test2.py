import settings
from locust import HttpUser, task


class Test2(HttpUser):
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

    # 302
    @task
    def redirect(self):
        self.client.head(
            "/api/pulp/redirect-check/",
            proxies=settings.proxy,
            cert=settings.cert,
            allow_redirects=False,
        )

    # 500
    @task
    def internal_server_error(self):
        self.client.head(
            "/api/pulp/internal-server-error-check/",
            proxies=settings.proxy,
            cert=settings.cert,
        )

    # 500 (from exception)
    @task
    def internal_server_error_exception(self):
        self.client.head(
            "/api/pulp/raise-exception-check/",
            proxies=settings.proxy,
            cert=settings.cert,
        )
