import sys
import traceback
from typing import Dict
from mcp.server.fastmcp import FastMCP
from chartmogul_mcp import api_client
from chartmogul_mcp import utils
from dotenv import load_dotenv


class ChartMogulMcp:

    def __init__(self):
        load_dotenv()

        # Initialize MCP Server
        self.mcp = FastMCP(utils.MCP_SERVER_NAME, deps=utils.DEPENDENCIES)
        print("ChartMogul MCP Server initialized", file=sys.stderr)

        self.config = api_client.init_chartmogul_config()

        # Register MCP tools
        self._register_tools()


    def _register_tools(self):
        """Register MCP tools to interact with ChartMogul API."""

        ## customers
        @self.mcp.tool()
        async def list_customers(data_source_uuid: str = None, external_id: str = None, status: str = None,
                                 system: str = None) -> list:
            return api_client.list_customers(self.config, data_source_uuid, external_id, status, system)

        @self.mcp.tool()
        async def search_customers(email: str) -> list:
            return api_client.search_customers(self.config, email)

        @self.mcp.tool()
        async def retrieve_customer(uuid: str) -> Dict:
            return api_client.retrieve_customer(self.config, uuid)

        @self.mcp.tool()
        async def delete_customer(uuid: str) -> bool:
            return api_client.delete_customer(self.config, uuid)

        @self.mcp.tool()
        async def update_customer(uuid: str, data: dict) -> Dict:
            return api_client.update_customer(self.config, uuid, data)

        @self.mcp.tool()
        async def merge_customers(from_uuid: str, to_uuid: str) -> Dict:
            return api_client.merge_customers(self.config, from_uuid, to_uuid)

        @self.mcp.tool()
        async def unmerge_customers(customer_uuid: str, data_source_uuid: str, external_id: str,
                                    move_to_new_customer: list) -> Dict:
            return api_client.unmerge_customers(self.config, customer_uuid, data_source_uuid,
                                                external_id, move_to_new_customer)

        ## metrics api
        @self.mcp.tool()
        async def all_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                              plans: str = None) -> list:
            return api_client.all_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool()
        async def mrr_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                              plans: str = None) -> list:
            return api_client.mrr_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool()
        async def arr_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                              plans: str = None) -> list:
            return api_client.arr_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool()
        async def arpa_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                               plans: str = None) -> list:
            return api_client.arpa_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool()
        async def asp_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                              plans: str = None) -> list:
            return api_client.asp_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool()
        async def customer_count_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                                         plans: str = None) -> list:
            return api_client.customer_count_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool()
        async def customer_churn_rate_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                                              plans: str = None) -> list:
            return api_client.customer_churn_rate_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool()
        async def mrr_churn_rate_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                                         plans: str = None) -> list:
            return api_client.mrr_churn_rate_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool()
        async def ltv_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                              plans: str = None) -> list:
            return api_client.ltv_metrics(self.config, start_date, end_date, interval, geo, plans)


    def run(self):
        """Start the MCP server."""
        try:
            print("Running MCP Server for ChartMogul API interactions", file=sys.stderr)
            self.mcp.run(transport="stdio")
        except Exception as e:
            print(f"Fatal Error in ChartMogul MCP Server: {str(e)}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)
