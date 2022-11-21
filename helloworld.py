import sys

""" Multi line documentation string
describing module."""

__version__ = "0.1.0"


class HelloWorld(object):
    """ documentation of the class."""

    # Single line Comment.

    @classmethod
    def main(cls, args):
        """ documentation string of the method."""
        print("Hello World")


def main():
    HelloWorld.main(sys.argv)


if __name__ == '__main__':
    main()
