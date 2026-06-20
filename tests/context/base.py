from pydantic import BaseModel

from tests.context.scenario import Scenario


class RequestContext(BaseModel):
    """
    Единый контекст запроса для тестового слоя.

    """
    scenario: Scenario


def build_grpc_test_metadata(context: RequestContext) -> list[tuple[str, str]]:
    """
    Преобразует RequestContext в gRPC metadata.

    """
    return [("x-test-scenario", context.scenario)]


def build_http_test_headers(context: RequestContext) -> dict[str, str]:
    """
    Преобразует RequestContext в HTTP headers.

    """
    return {"x-test-scenario": context.scenario}
