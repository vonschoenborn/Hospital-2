
import pandas as pd
import os

cleaveland = pd.read_csv(os.path.join('.','data','processed.cleveland.data'),names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num'], na_values=[-9.0,'?'])
hungarian = pd.read_csv(os.path.join('.','data','reprocessed.hungarian.data'),sep=' ',names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num'], na_values=[-9.0,'?'])
switzerland = pd.read_csv(os.path.join('.','data','processed.switzerland.data'),names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num'], na_values=[-9.0,'?'])
va = pd.read_csv(os.path.join('.','data','processed.va.data'),names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','num'], na_values=[-9.0,'?'])


for location in ['cleaveland','hungarian','switzerland','va']:
    cleaveland[location]=0
    hungarian[location]=0
    switzerland[location]=0
    va[location]=0

cleaveland['cleaveland']=1
hungarian['hungarian']=1
switzerland['switzerland']=1
va['va']=1

processedData = pd.concat([cleaveland,hungarian,switzerland,va])
