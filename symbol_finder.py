import yfinance as yf

def find_symbol(company_name):
    """
    Try common exchanges automatically (NSE, US).
    """
    search_terms = [
        company_name,
        company_name + " NSE",
        company_name + " stock"
    ]

    for term in search_terms:
        try:
            search = yf.Search(term)
            if search.quotes:
                return search.quotes[0]["symbol"]
        except:
            pass

    raise ValueError("Company not found or not listed on stock exchange")
