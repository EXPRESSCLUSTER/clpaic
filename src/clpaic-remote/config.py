import os

OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL    = os.getenv("OPENAI_MODEL")

SSL_VERIFY      = os.getenv("SSL_VERIFY", "TRUE").upper() == "TRUE"
DRYRUN          = os.getenv("DRYRUN", "TRUE").upper() == "TRUE"

CLP_BASE_URL    = os.getenv("CLP_BASE_URL", "http://localhost:29009")
CLP_USERNAME    = os.getenv("CLP_USERNAME", "")
CLP_PASSWORD    = os.getenv("CLP_PASSWORD", "")
