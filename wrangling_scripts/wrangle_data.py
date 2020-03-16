import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def clean_data(dataset, keepcolumns=['Country Name', '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'],
            value_variables=['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010']):
        """
        This will clean the data for you
        Args:
            dataset: the dataset you use for the company
            keepcolumns: the columns you want to keep
        """
        top_countries = ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada']
        df = pd.read_csv(dataset)
        df = df[keepcolumns]
        df = df[df['Country Name'].isin(top_countries)]
        
        df_melt = df.melt(id_vars='Country Name', value_vars=value_variables)
        df_melt.columns = ['country', 'year', 'variable']
        df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year
        
        return df_melt

def return_figures():
    """
    This function will help you to return the figures
    Args:
        None
    Return:
        figures
    """
    
    graph_one = []
    df = clean_data('data/data.csv')
    country_list = df.country.unique().tolist()
    
    for country in country_list:
        x_val = df[df['country'] == country].year.tolist()
        y_val = df[df['country'] == country].variable.tolist()
        
        graph_one.append(
            go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = country
            )
        )
        
        
    layout_one = dict(title = 'Electricity access from 1990 to 2010',
                xaxis = dict(title = 'Year',
                  autotick=False, tick0=1990, dtick=25),
                yaxis = dict(title = 'Electricity access'),
                )
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    
    return figures