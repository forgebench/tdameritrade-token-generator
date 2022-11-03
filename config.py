from pathlib import Path

root = Path("./")

# Your TD Ameritrade application’s redirect URL. Note this must exactly match the value
# you’ve entered in your application configuration, otherwise login will fail with a security error.
redirect_url = 'https://localhost:8080'

# Put path to chromedriver here
chromedriver_path = root / 'chromedriver'