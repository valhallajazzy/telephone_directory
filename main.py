import os

from view import main_interaction
from dotenv import load_dotenv

load_dotenv()
path = os.getenv()

def main():
    main_interaction()


if __name__ == '__main__':
    main()

