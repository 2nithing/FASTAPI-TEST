from fastapi import FastAPI 
from pydantic import BaseModel
import pickle
import pandas as pd
app = FastAPI()

class ScoringItem(BaseModel):
    Height:float


with open('model.pkl','rb') as f:
    model = pickle.load(f) 

@app.post('/')
async def scoring_endpoint(item:ScoringItem):
    # df = pd.DataFrame([item.dict().values()],columns=item.dict().keys())
    pred = model.predict([[item.dict()['Height']]])
    print(type(pred))
    return {'predicted weight':pred[0]}