import requests

PROMETHEUS_URL = "http://SERVER_IP:9090/api/v1/query"


def query_prometheus(query: str):
    response = requests.get(
        PROMETHEUS_URL,
        params={"query": query},
        timeout=5,
    )
    response.raise_for_status()
    return response.json()


def main():
    query = "up"
    result = query_prometheus(query)

    print("Prometheus query:")
    print(query)
    print()
    print("Result:")
    print(result)


if __name__ == "__main__":
    main()
