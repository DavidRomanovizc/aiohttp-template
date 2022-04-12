import argparse


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Host to connect", default="127.0.0.1")
    parser.add_argument("--port", help="Port to accept connections", default="8080")
    parser.add_argument("--reload", action="store_true", help="Autoreload code on change")
    parser.add_argument("-c", "--config", type=argparse.FileType(), help="Path to configuration file")
    return parser.parse_args()
