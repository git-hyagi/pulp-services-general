import settings
from locust import HttpUser, task


class Test3(HttpUser):

    ####### CONTENT ########
    #2xx
    @task
    def ok(self):
      self.client.get(
          "/api/pulp-content/default/",
          proxies=settings.proxy,
          cert=settings.cert,
          )

    #3xx
    @task
    def redirect(self):
      self.client.get(
          "/api/pulp-content/hyagi-s3/test/1.iso",
          proxies=settings.proxy,
          cert=settings.cert,
          allow_redirects=False,
          )

    #404
    @task
    def not_found(self):
      self.client.get(
          "/api/pulp-content/hyagi-s3/test/5.iso",
          proxies=settings.proxy,
          cert=settings.cert,
          )

    # 500
    @task
    def internal_server_error(self):
        self.client.get(
            "/api/pulp-content/hyagi/test/1.iso",
            proxies=settings.proxy,
            cert=settings.cert,
        )
