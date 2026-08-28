"""
=========================================================
QUANT ULTRA
Service Container
=========================================================
Dependency Injection Container
=========================================================
"""


class ServiceContainer:

    def __init__(self):

        self._services = {}

    # -------------------------------------------------
    # Register
    # -------------------------------------------------

    def register(

        self,

        name,

        service,

    ):

        self._services[name] = service

    # -------------------------------------------------
    # Get
    # -------------------------------------------------

    def get(

        self,

        name,

    ):

        if name not in self._services:

            raise KeyError(

                f"Service '{name}' not registered."

            )

        return self._services[name]

    # -------------------------------------------------

    def exists(

        self,

        name,

    ):

        return name in self._services

    # -------------------------------------------------

    def list_services(

        self,

    ):

        return sorted(

            self._services.keys()

        )


# ---------------------------------------------------------

if __name__ == "__main__":

    container = ServiceContainer()

    class Demo:

        pass

    container.register(

        "demo",

        Demo(),

    )

    print()

    print("=" * 60)

    print("SERVICE CONTAINER READY")

    print("=" * 60)

    print(container.list_services())