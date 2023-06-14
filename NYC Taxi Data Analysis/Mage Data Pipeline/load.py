import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # url = 'https://storage.googleapis.com/nyc-taxi-data-covid/nyc_taxi_data.csv'
    # response = requests.get(url)

    # return pd.read_csv(io.StringIO(response.text), sep=',')
    df=pd.DataFrame()
    base_url="https://storage.googleapis.com/nyc-taxi-data-covid/data/"
    for i in range(2019,2022):
        for j in range(1,13):
            url=base_url+str(i)+"/yellow_tripdata_"+str(i)+"-"+f"{j:02}"+".parquet"
            df_new=pd.read_parquet(url)
            df=pd.concat([df_new])
    df.head()
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
