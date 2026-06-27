from dataclasses import dataclass

@dataclass(slots=True)
class Result:

    dns_name:str

    dns_ip:str

    domain:str

    resolved_ip:str

    dns_ms:float

    tcp_ms:float

    tls_ms:float

    ttfb_ms:float

    download_ms:float

    total_ms:float

    bytes_received:int

    success:bool

    error:str=""