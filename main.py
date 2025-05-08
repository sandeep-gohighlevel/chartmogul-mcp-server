from chartmogul_mcp import mcp_server


if __name__ == "__main__":
    cm_mcp = mcp_server.ChartMogulMcp()
    cm_mcp.run()