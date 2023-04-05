# create server script

from sys import argv, exit, stderr
from app import app
import argparse

class Parser:
    """Parses the command line arguments."""
    def __init__(self):
        parser = argparse.ArgumentParser(description="A timezone search application.")
        parser.add_argument("port", help="the port at which the server should listen")
        self.args = parser.parse_args()
        
    def get_port(self):
        # if port is not an integer, argparse will raise an error. Also if there are NOT exactly 2 arguments, argparse will raise an error.
        try: 
            port = int(self.args.port)
            return port
        except ValueError:
            print("Port must be an integer.", file=stderr)
            exit(1)
    

class Server:
    """Runs the server."""
    def __init__(self, port):
        self.port = port
        
    def run(self):
        try:
            app.run(host="0.0.0.0", port=self.port, debug=True)
        except Exception as ex:
            print(ex, file=stderr)
            exit(1)


def main():
    parser = Parser()
    port = parser.get_port()
    server = Server(port)
    server.run()
  
if __name__ == "__main__":
    main()

        

