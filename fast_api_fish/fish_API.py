#'''uvicorn fish_API:app --reload''' in terminal to lunch the API >>> copy and past the url in goolgle chrome

from fastapi import FastAPI
import pickle
from typing import Union
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.iolib.smpickle as sis

app = FastAPI()

@app.get('/')
def prediction(Species : Union[str, None] = 'Bream',
               Height : Union[float, None] = 0
                ):
    
    lm = sis.load_pickle('lm_fish.pkl')
    df = pd.DataFrame.from_dict({'Species' : [Species], 'Weight' : [0], 'Height' : [Height]})
    pred = lm.predict(df)
    return {'Weight' : f'{pred[0]}'}
