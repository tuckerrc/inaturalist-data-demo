import sys
from cloudquery.sdk import serve

from plugin import ObservationPlugin


def main():
    p = ObservationPlugin()
    serve.PluginCommand(p).run(sys.argv[1:])


if __name__ == "__main__":
    main()
