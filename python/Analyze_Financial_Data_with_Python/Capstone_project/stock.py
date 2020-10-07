class Stock:

    names = []
    prt = lambda: print(*Stock.names, sep = ", ")
    length = lambda: len(Stock.names)
    _range = lambda: range(Stock.length())
    get_list_of_means = lambda stocks: [stock.get_mean() * 100 for stock in stocks]
    get_list_of_variances = lambda stocks: [stock.get_variance() * 100 for stock in stocks]
    get_list_of_std = lambda stocks: [stock.get_standard_deviation() * 100 for stock in stocks]
    dropped = []

    def __init__(self, name, df):
        self.name = name
        self.df = df
        Stock.names.append(name)

    def get_adjClose(self):
        return self.df.adjClose.reset_index()

    def get_simple_rate_of_return(self):
        simple_rate_of_return = self.df.adjClose.pct_change().reset_index()
        simple_rate_of_return.rename(columns = {"adjClose": "daily_s_ror"}, inplace = True)
        return simple_rate_of_return

    def get_mean(self):
        simple_rate_of_return = self.get_simple_rate_of_return()
        mean = simple_rate_of_return.mean().daily_s_ror
        return mean
    
    def get_variance(self):
        simple_rate_of_return = self.get_simple_rate_of_return()
        variance = simple_rate_of_return.var().daily_s_ror
        return variance
    
    def get_standard_deviation(self):
        simple_rate_of_return = self.get_simple_rate_of_return()
        standard_deviation = simple_rate_of_return.std().daily_s_ror
        return standard_deviation

    def get_name_val_from_corr_table(self, correlations):
        i = 0
        list_of_names_pairs = []
        list_of_corr_val = []
        for name in Stock.names:
            wait = True
            values = list(correlations[name].values)
            for y in range(len(values)):
                if values[y] == 1:
                    stock_name1 = name + " / "
                    wait = False
                    continue
                if not wait:
                    stock_name2 = correlations.index[y]
                    list_of_names_pairs.append(stock_name1 + stock_name2)
                    list_of_corr_val.append(values[y])
            i += 1
        return list_of_names_pairs, list_of_corr_val