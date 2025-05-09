import traceback
import chartmogul
from chartmogul_mcp import utils

def init_chartmogul_config():
    return chartmogul.Config(utils.CHARTMOGUL_TOKEN)


## Customers Endpoints

def list_customers(config, data_source_uuid=None, external_id=None, status=None, system=None, limit=20) -> list:
    """
    List all customers from ChartMogul API.
        
    Returns: A list of chartmogul customers.
    """
    print(f"List customers for {data_source_uuid}, {external_id}, {status}, {system}.")
    all_customers = []
    has_more = True
    cursor = None
    per_page = 20
    total = 0
    while has_more and total < limit:
        request = chartmogul.Customer.all(config,
                                          data_source_uuid=data_source_uuid,
                                          external_id=external_id,
                                          status=status,
                                          system=system,
                                          cursor=cursor,
                                          per_page=per_page)
        try:
            customers = request.get()
            all_customers.extend([entry.__dict__ for entry in customers.entries])
            total += per_page
            has_more = customers.has_more
            cursor = customers.cursor
        except Exception as e:
            print(f"Error fetching ChartMogul customers: {str(e)}")
            traceback.print_exc()
            return None
    return all_customers


def retrieve_customer(config, uuid):
    """
    Retrieve a customer from ChartMogul API.

    Returns: The customer.
    """
    print(f"Retrieving customer for {uuid}.")
    request = chartmogul.Customer.retrieve(config, uuid=uuid)
    try:
        customer = request.get().__dict__
    except Exception as e:
        print(f"Error retrieving customer: {str(e)}")
        traceback.print_exc()
        return None
    return customer


def update_customer(config, uuid, data):
    """
    Update a customer from ChartMogul API.

    Returns:
    """
    print(f"Updating customer {uuid}, {data}.")
    request = chartmogul.Customer.modify(config, uuid=uuid, data=data)
    try:
        customer = request.get()
    except Exception as e:
        print(f"Error updating customer: {str(e)}")
        traceback.print_exc()
        return None
    return customer


def search_customers(config, email, limit=20) -> list:
    """
    Search all customers by email from ChartMogul API.

    Returns: A list of ChartMogul customers.
    """
    print(f"Search customers for {email}.")
    all_customers = []
    has_more = True
    cursor = None
    per_page = 20
    total = 0
    while has_more and total < limit:
        request = chartmogul.Customer.search(config, email=email, cursor=cursor, per_page=per_page)
        try:
            customers = request.get()
            all_customers.extend([entry.__dict__ for entry in customers.entries])
            total += per_page
            has_more = customers.has_more
            cursor = customers.cursor
        except Exception as e:
            print(f"Error searching ChartMogul customers: {str(e)}")
            traceback.print_exc()
            return None
    return all_customers


## Metrics API Endpoints

def all_metrics(config, start_date, end_date, interval, geo=None, plans=None) -> list:
    """
    List all metrics from ChartMogul API.

    Returns: A list of all metrics.
    """
    print(f" Fetching all metrics for {start_date}, {end_date}, {interval}, {geo}, {plans}.")
    request = chartmogul.Metrics.all(config,
                                     start_date=start_date,
                                     end_date=end_date,
                                     interval=interval,
                                     geo=geo,
                                     plans=plans
                                     )
    try:
        metrics = request.get()
        all_metrics = [entry.__dict__ for entry in metrics.entries]
    except Exception as e:
        print(f"Error fetching all metrics: {str(e)}")
        traceback.print_exc()
        return None
    return all_metrics


def mrr_metrics(config, start_date, end_date, interval, geo=None, plans=None) -> list:
    """
    List MRR metrics from ChartMogul API.

    Returns: A list of MRR metrics.
    """
    print(f" Fetching MRR metrics for {start_date}, {end_date}, {interval}, {geo}, {plans}.")
    request = chartmogul.Metrics.mrr(config,
                                     start_date=start_date,
                                     end_date=end_date,
                                     interval=interval,
                                     geo=geo,
                                     plans=plans
                                     )
    try:
        mrr = request.get()
        all_mrr = [entry.__dict__ for entry in mrr.entries]
    except Exception as e:
        print(f"Error fetching MRR metrics: {str(e)}")
        traceback.print_exc()
        return None
    return all_mrr


def arr_metrics(config, start_date, end_date, interval, geo=None, plans=None) -> list:
    """
    List ARR metrics from ChartMogul API.

    Returns: A list of ARR metrics.
    """
    print(f" Fetching ARR metrics for {start_date}, {end_date}, {interval}, {geo}, {plans}.")
    request = chartmogul.Metrics.arr(config,
                                     start_date=start_date,
                                     end_date=end_date,
                                     interval=interval,
                                     geo=geo,
                                     plans=plans
                                     )
    try:
        arr = request.get()
        all_arr = [entry.__dict__ for entry in arr.entries]
    except Exception as e:
        print(f"Error fetching ARR metrics: {str(e)}")
        traceback.print_exc()
        return None
    return all_arr


def arpa_metrics(config, start_date, end_date, interval, geo=None, plans=None) -> list:
    """
    List ARPA metrics from ChartMogul API.

    Returns: A list of ARPA metrics.
    """
    print(f" Fetching ARPA metrics for {start_date}, {end_date}, {interval}, {geo}, {plans}.")
    request = chartmogul.Metrics.arpa(config,
                                      start_date=start_date,
                                      end_date=end_date,
                                      interval=interval,
                                      geo=geo,
                                      plans=plans
                                      )
    try:
        arpa = request.get()
        all_arpa = [entry.__dict__ for entry in arpa.entries]
    except Exception as e:
        print(f"Error fetching ARPA metrics: {str(e)}")
        traceback.print_exc()
        return None
    return all_arpa


def asp_metrics(config, start_date, end_date, interval, geo=None, plans=None) -> list:
    """
    List ASP metrics from ChartMogul API.

    Returns: A list of ASP metrics.
    """
    print(f" Fetching ASP metrics for {start_date}, {end_date}, {interval}, {geo}, {plans}.")
    request = chartmogul.Metrics.asp(config,
                                     start_date=start_date,
                                     end_date=end_date,
                                     interval=interval,
                                     geo=geo,
                                     plans=plans
                                     )
    try:
        asp = request.get()
        all_asp = [entry.__dict__ for entry in asp.entries]
    except Exception as e:
        print(f"Error fetching ASP metrics: {str(e)}")
        traceback.print_exc()
        return None
    return all_asp


def customer_count_metrics(config, start_date, end_date, interval, geo=None, plans=None) -> list:
    """
    List Customer count metrics from ChartMogul API.

    Returns: A list of Customer count metrics.
    """
    print(f" Fetching Customer count metrics for {start_date}, {end_date}, {interval}, {geo}, {plans}.")
    request = chartmogul.Metrics.customer_count(config,
                                                start_date=start_date,
                                                end_date=end_date,
                                                interval=interval,
                                                geo=geo,
                                                plans=plans
                                                )
    try:
        customer_count = request.get()
        all_customer_count = [entry.__dict__ for entry in customer_count.entries]
    except Exception as e:
        print(f"Error fetching Customer count metrics: {str(e)}")
        traceback.print_exc()
        return None
    return all_customer_count


def customer_churn_rate_metrics(config, start_date, end_date, interval, geo=None, plans=None) -> list:
    """
    List Customer churn rate metrics from ChartMogul API.

    Returns: A list of Customer churn rate metrics.
    """
    print(f" Fetching Customer churn rate metrics for {start_date}, {end_date}, {interval}, {geo}, {plans}.")
    request = chartmogul.Metrics.customer_churn_rate(config,
                                                     start_date=start_date,
                                                     end_date=end_date,
                                                     interval=interval,
                                                     geo=geo,
                                                     plans=plans
                                                     )
    try:
        customer_churn_rate = request.get()
        all_customer_churn_rate = [entry.__dict__ for entry in customer_churn_rate.entries]
    except Exception as e:
        print(f"Error fetching Customer churn rate metrics: {str(e)}")
        traceback.print_exc()
        return None
    return all_customer_churn_rate


def mrr_churn_rate_metrics(config, start_date, end_date, interval, geo=None, plans=None) -> list:
    """
    List MRR churn rate metrics from ChartMogul API.

    Returns: A list of MRR churn rate metrics.
    """
    print(f" Fetching MRR churn rate metrics for {start_date}, {end_date}, {interval}, {geo}, {plans}.")
    request = chartmogul.Metrics.mrr_churn_rate(config,
                                                start_date=start_date,
                                                end_date=end_date,
                                                interval=interval,
                                                geo=geo,
                                                plans=plans
                                                )
    try:
        mrr_churn_rate = request.get()
        all_mrr_churn_rate = [entry.__dict__ for entry in mrr_churn_rate.entries]
    except Exception as e:
        print(f"Error fetching MRR churn rate metrics: {str(e)}")
        traceback.print_exc()
        return None
    return all_mrr_churn_rate


def ltv_metrics(config, start_date, end_date, interval, geo=None, plans=None) -> list:
    """
    List LTV metrics from ChartMogul API.

    Returns: A list of LTV metrics.
    """
    print(f" Fetching LTV metrics for {start_date}, {end_date}, {interval}, {geo}, {plans}.")
    request = chartmogul.Metrics.ltv(config,
                                     start_date=start_date,
                                     end_date=end_date,
                                     interval=interval,
                                     geo=geo,
                                     plans=plans
                                     )
    try:
        ltv = request.get()
        all_ltv = [entry.__dict__ for entry in ltv.entries]
    except Exception as e:
        print(f"Error fetching LTV metrics: {str(e)}")
        traceback.print_exc()
        return None
    return all_ltv
