{"cells":[{"cell_type":"code","execution_count":null,"metadata":{},"outputs":[],"source":[]},{"cell_type":"markdown","metadata":{},"source":[]},{"cell_type":"code","execution_count":null,"metadata":{},"outputs":[],"source":[]},{"cell_type":"code","execution_count":null,"metadata":{},"outputs":[],"source":[]}],"metadata":{"language_info":{"name":"python"},"orig_nbformat":4},"nbformat":4,"nbformat_minor":2}
import fredapi as fpi
import pandas as pd

fred = fpi.Fred(api_key='2b4f190fb1c9aa72c94f0a4d3bd04589')
GDP = fred.get_series('GDP')
GDP=GDP.to_frame()
GDP.rename(columns={0 :'GDP'}, inplace=True)
GDP['GDP'].plot()