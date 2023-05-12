from typing import Any, Dict, Optional

import requests


def get(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, str]] = None,
    timeout: int = 10,
) -> requests.Response:
    response = requests.get(
        url, headers=headers, params=params, timeout=timeout
    )
    response.raise_for_status()
    return response


def post(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    data: Optional[Dict[str, str]] = None,
    json: Optional[Any] = None,
    timeout: int = 10,
) -> requests.Response:
    response = requests.post(
        url, headers=headers, data=data, json=json, timeout=timeout
    )
    response.raise_for_status()
    return response
