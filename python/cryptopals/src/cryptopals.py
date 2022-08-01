import base64


def hex2base64(input: bytes) -> bytes:
    return base64.encodebytes(bytes.fromhex(input.decode('utf-8')))
