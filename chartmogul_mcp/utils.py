import os
from dotenv import load_dotenv

load_dotenv()

CHARTMOGUL_TOKEN = os.getenv('CHARTMOGUL_TOKEN')
MCP_SERVER_NAME = "mcp-chartmogul"
DEPENDENCIES = [
    "chartmogul",
    "python-dotenv"
]