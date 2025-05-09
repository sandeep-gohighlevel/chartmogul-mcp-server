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
        @self.mcp.tool(name='list_customers',
                       description='Get a list of customers in your ChartMogul account. '
                                   'We have a default limit of 20 customers, '
                                   'ask but discourage the user if they want more than 20 as this will exhaust AI tokens.'
                                   'You can also filter based on data_source_uuid, external_id, '
                                   'status (one of New_Lead, Working_Lead, Qualified_Lead, Unqualified_Lead, Active, '
                                   'Past_Due or Cancelled) and billing system e.g. Stripe, Recurly, Custom, etc.')
        async def list_customers(data_source_uuid: str = None, external_id: str = None, status: str = None,
                                 system: str = None, limit: int = 20) -> list:
            return api_client.list_customers(self.config, data_source_uuid, external_id, status, system, limit)

        @self.mcp.tool(name='search_customers',
                       description='Search a list of all customers with the specified email address '
                                   'in your ChartMogul account.'
                                   'We have a default limit of 20 customers, '
                                   'ask but discourage the user if they want more than 20 as this will exhaust AI tokens.')
        async def search_customers(email: str, limit: int = 20) -> list:
            return api_client.search_customers(self.config, email, limit)

        @self.mcp.tool(name='retrieve_customer',
                       description='Retrieve a customer from your ChartMogul account using its UUID.')
        async def retrieve_customer(uuid: str) -> Dict:
            return api_client.retrieve_customer(self.config, uuid)

        @self.mcp.tool(name='update_customer',
                       description='Update certain modifiable attributes of a customer in your ChartMogul account. '
                                   'Attributes that can be modified are: company, lead_created_at, '
                                   'free_trial_started_at, zip, city, state, country, attributes '
                                   '(nested object which includes tags and custom object), owner, '
                                   'primary_contact, status and website_url, and should be included in a '
                                   'data dictionary.')
        async def update_customer(uuid: str, data: dict) -> Dict:
            return api_client.update_customer(self.config, uuid, data)

        ## metrics api
        @self.mcp.tool(name='all_metrics',
                       description='Retrieve all key metrics, for the specified time period, interval and filters. '
                                   'Metrics include: MRR, ARR, ARPA, ASP, customer count, customer churn rate, '
                                   'MRR churn rate and LTV. '
                                   'Provide the start-date, end-date and interval (possible values are day, week, month,'
                                   'or quarter. Additional filter values include geo (A comma-separated list of ISO '
                                   '3166-1 Alpha-2 formatted country codes) and plans (A comma-separated list of '
                                   'plan names (as configured in your ChartMogul account), UUIDs and external IDs to '
                                   'filter the results. Spaces in plan names must be URL-encoded, '
                                   'e.g., Silver%20plan,Gold%20plan,Enterprise%20plan).'
                                   'All amounts are given in the selected currency of your account '
                                   'and are an integer number of cents. Divide by 100 to obtain the actual value.')
        async def all_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                              plans: str = None) -> list:
            return api_client.all_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool(name='mrr_metrics',
                       description='Retrieve Monthly Recurring Revenue (MRR) metrics, for the specified time period, interval and filters. '
                                   'Provide the start-date, end-date and interval (possible values are day, week, month,'
                                   'or quarter. Additional filter values include geo (A comma-separated list of ISO '
                                   '3166-1 Alpha-2 formatted country codes) and plans (A comma-separated list of '
                                   'plan names (as configured in your ChartMogul account), UUIDs and external IDs to '
                                   'filter the results. Spaces in plan names must be URL-encoded, '
                                   'e.g., Silver%20plan,Gold%20plan,Enterprise%20plan).'
                                   'All amounts are given in the selected currency of your account '
                                   'and are an integer number of cents. Divide by 100 to obtain the actual value.')
        async def mrr_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                              plans: str = None) -> list:
            return api_client.mrr_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool(name='arr_metrics',
                       description='Retrieve Annualized Run Rate (ARR) metrics, for the specified time period, interval and filters. '
                                   'Provide the start-date, end-date and interval (possible values are day, week, month,'
                                   'or quarter. Additional filter values include geo (A comma-separated list of ISO '
                                   '3166-1 Alpha-2 formatted country codes) and plans (A comma-separated list of '
                                   'plan names (as configured in your ChartMogul account), UUIDs and external IDs to '
                                   'filter the results. Spaces in plan names must be URL-encoded, '
                                   'e.g., Silver%20plan,Gold%20plan,Enterprise%20plan).'
                                   'All amounts are given in the selected currency of your account '
                                   'and are an integer number of cents. Divide by 100 to obtain the actual value.')
        async def arr_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                              plans: str = None) -> list:
            return api_client.arr_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool(name='arpa_metrics',
                       description='Retrieve Average Revenue Per Account (ARPA) metrics, for the specified time period, interval and filters. '
                                   'Provide the start-date, end-date and interval (possible values are day, week, month,'
                                   'or quarter. Additional filter values include geo (A comma-separated list of ISO '
                                   '3166-1 Alpha-2 formatted country codes) and plans (A comma-separated list of '
                                   'plan names (as configured in your ChartMogul account), UUIDs and external IDs to '
                                   'filter the results. Spaces in plan names must be URL-encoded, '
                                   'e.g., Silver%20plan,Gold%20plan,Enterprise%20plan).'
                                   'All amounts are given in the selected currency of your account '
                                   'and are an integer number of cents. Divide by 100 to obtain the actual value.')
        async def arpa_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                               plans: str = None) -> list:
            return api_client.arpa_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool(name='asp_metrics',
                       description='Retrieve Average Sale Price (ASP) metrics, for the specified time period, interval and filters. '
                                   'Provide the start-date, end-date and interval (possible values are month,'
                                   'or quarter. Additional filter values include geo (A comma-separated list of ISO '
                                   '3166-1 Alpha-2 formatted country codes) and plans (A comma-separated list of '
                                   'plan names (as configured in your ChartMogul account), UUIDs and external IDs to '
                                   'filter the results. Spaces in plan names must be URL-encoded, '
                                   'e.g., Silver%20plan,Gold%20plan,Enterprise%20plan).'
                                   'All amounts are given in the selected currency of your account '
                                   'and are an integer number of cents. Divide by 100 to obtain the actual value.')
        async def asp_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                              plans: str = None) -> list:
            return api_client.asp_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool(name='customer_count_metrics',
                       description='Retrieve customer count metrics, for the specified time period, interval and filters. '
                                   'Provide the start-date, end-date and interval (possible values are day, week, month,'
                                   'or quarter. Additional filter values include geo (A comma-separated list of ISO '
                                   '3166-1 Alpha-2 formatted country codes) and plans (A comma-separated list of '
                                   'plan names (as configured in your ChartMogul account), UUIDs and external IDs to '
                                   'filter the results. Spaces in plan names must be URL-encoded, '
                                   'e.g., Silver%20plan,Gold%20plan,Enterprise%20plan).')
        async def customer_count_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                                         plans: str = None) -> list:
            return api_client.customer_count_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool(name='customer_churn_rate_metrics',
                       description='Retrieve customer churn rate metrics, for the specified time period, interval and filters. '
                                   'Provide the start-date, end-date and interval (possible values are day, week, month,'
                                   'or quarter. Additional filter values include geo (A comma-separated list of ISO '
                                   '3166-1 Alpha-2 formatted country codes) and plans (A comma-separated list of '
                                   'plan names (as configured in your ChartMogul account), UUIDs and external IDs to '
                                   'filter the results. Spaces in plan names must be URL-encoded, '
                                   'e.g., Silver%20plan,Gold%20plan,Enterprise%20plan).')
        async def customer_churn_rate_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                                              plans: str = None) -> list:
            return api_client.customer_churn_rate_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool(name='mrr_churn_rate_metrics',
                       description='Retrieve Net MRR Churn Rate metrics, for the specified time period, interval and filters. '
                                   'Provide the start-date, end-date and interval (possible values are day, week, month,'
                                   'or quarter. Additional filter values include geo (A comma-separated list of ISO '
                                   '3166-1 Alpha-2 formatted country codes) and plans (A comma-separated list of '
                                   'plan names (as configured in your ChartMogul account), UUIDs and external IDs to '
                                   'filter the results. Spaces in plan names must be URL-encoded, '
                                   'e.g., Silver%20plan,Gold%20plan,Enterprise%20plan).')
        async def mrr_churn_rate_metrics(start_date: str, end_date: str, interval: str, geo: str = None,
                                         plans: str = None) -> list:
            return api_client.mrr_churn_rate_metrics(self.config, start_date, end_date, interval, geo, plans)

        @self.mcp.tool(name='ltv_metrics',
                       description='Retrieve Customer Lifetime Value (LTV) metrics, for the specified time period, and filters. '
                                   'Provide the start-date, end-date. Additional filter values include geo (A comma-separated list of ISO '
                                   '3166-1 Alpha-2 formatted country codes) and plans (A comma-separated list of '
                                   'plan names (as configured in your ChartMogul account), UUIDs and external IDs to '
                                   'filter the results. Spaces in plan names must be URL-encoded, '
                                   'e.g., Silver%20plan,Gold%20plan,Enterprise%20plan).'
                                   'All amounts are given in the selected currency of your account '
                                   'and are an integer number of cents. Divide by 100 to obtain the actual value.')
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
