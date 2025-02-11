# Final project: 32100-81
# Names: Jim Tinley
# importing packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import scipy as scp
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import r2_score

sns.set_theme(style = "ticks")

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# reading in our cross-sectional dataset with 436 total observations 
# (416 are the first MRI scan, 20 observations are a second MRI scan administered to 20 individuals without dementia symptoms)

fp_cs = pd.read_csv("MRI_and_alzheimers_cross_sectional_data.csv", index_col=0)
fp_cs


# In[3]:


# removing the observations for those who recieved a second MRI scan (ID's ending in MR2), we will use only first MRI scans in our analysis 
# removing dominant hand and delay columns 

MR1_df = fp_cs.head(416)
MR1_df = MR1_df.drop(columns = ['dominant_hand','Delay'])
MR1_df.head()


# In[4]:


# creating gender binary (F=0, M=1)

MR1_df["gender"] = pd.get_dummies(MR1_df["gender"], drop_first=True)
MR1_df.head()


# In[5]:


# checking for the total number of individuals who did not recieve a CDR score (CDR="NaN")
# removing observations for those without a CDR rating, and saving this as a new dataframe CDR_df
# assessing our final dataframe (CDR_df) which will be split into train and test sets

print(MR1_df['clinical_dementia_rating_(CDR)'].isna().sum())
CDR_df = MR1_df.dropna(subset=["clinical_dementia_rating_(CDR)","socioeconomic_status_(SES)"])
print(CDR_df.info())
CDR_df.head()


# In[6]:


# converting the variable "normalize_whole_brain_volume_(nWBV)" which is a proportion to a %
# renaming the "normalize_whole_brain_volume_(nWBV)" to 'normalize_whole_brain_volume%_(nWBV%)'

CDR_df["normalize_whole_brain_volume_(nWBV)"] = CDR_df["normalize_whole_brain_volume_(nWBV)"] * 100
CDR_df = CDR_df.rename(columns={'normalize_whole_brain_volume_(nWBV)':'normalize_whole_brain_volume%_(nWBV%)'})
CDR_df.head()


# In[7]:


# checking the unique CDR score values in our dataset
# creating binary condition: 1 = clinical dementia symptoms (CDR > 0), 0 = no dementia symptoms (CDR=0).
# checking the total number of individuals with CDR > 0 

print(CDR_df["clinical_dementia_rating_(CDR)"].unique())
CDR_df["dementia_binary"] = np.where(CDR_df["clinical_dementia_rating_(CDR)"] > 0, 1, 0)
CDR_df["dementia_binary"].sum()


# In[8]:


# plotting the dementia_binary variable to get a rough idea of our data

sns.countplot(CDR_df["dementia_binary"])


# In[9]:


# spliting our data into train and test sets for our logistic regression model

np.random.seed(123)
X_train, X_test, y_train, y_test = train_test_split(CDR_df[['age_in_years',
                                                            'gender',
                                                            'education_level',
                                                            'socioeconomic_status_(SES)',
                                                            'mini_mental_state_examination_(MMSE)',
                                                            'normalize_whole_brain_volume%_(nWBV%)']],
                                                    CDR_df['dementia_binary'], test_size=0.3)

print(y_train)
X_train


# In[10]:


# using the statsmodels.api package to get coefs for our independent variables

log_reg_s = sm.Logit(y_train, X_train).fit()
print(log_reg_s.summary())


# In[11]:


# using the sklearn package to create our logistic regression ML model

log_reg_ML = LogisticRegression(fit_intercept=False, C = 1e9)
log_reg_ML.fit(X_train,y_train)
print(log_reg_ML.get_params())


# In[12]:


# checking that the coefs derived from the statsmodels.api package match the sklearn coefs
# ** note both packages were used to access different features for our logisitic regression model
# the statsmodels.api package is used for the function "log_reg_s"; and the sklearn package is used for "log_reg_ML" **
# converting the coefs to Odds Ratios: e^[coefficient]

print(log_reg_ML.coef_)
print("Coefficients: \n", log_reg_s.params)
print("Odds Ratios: \n", np.exp(log_reg_ML.coef_))


# In[13]:


# getting accuracy score for our model

y_pred = log_reg_ML.predict(X_test)
log_reg_ML.score(X_test, y_test)


# In[14]:


# creating matrix

confusion_matrix(y_test, y_pred)


# In[15]:


# plotting matrix

plot_confusion_matrix(log_reg_ML, X_test, y_test, cmap='Greys', display_labels=['no dementia','dementia'])
plt.show()


# In[16]:


# checking matrix data is correct

print("Test set data", "\n")
print("total observations",y_test.count())
print("True # of individuals who do not have dementia:", y_test.count()-y_test.sum())
print("True # of individuals who do have dementia:", y_test.sum())

print("Predicted # of individuals who do not have dementia:", y_test.count()-y_pred.sum())
print("Predicted # of individuals who do have dementia:", y_pred.sum())


# In[17]:


# data exploration

sns.regplot(x=CDR_df["age_in_years"], y=CDR_df["dementia_binary"], logistic=True, 
            scatter_kws={"color": "gray"})


# In[18]:


# data exploration

sns.boxplot(data = CDR_df, y="clinical_dementia_rating_(CDR)", x = "age_in_years", orient="h", palette="Blues")


# In[19]:


# data exploration

sns.regplot(x=CDR_df["mini_mental_state_examination_(MMSE)"], y=CDR_df["dementia_binary"], logistic=True,
            scatter_kws={"color": "gray"}, 
            line_kws={"color": "red"})


# In[20]:




sns.boxplot(data = CDR_df, y="clinical_dementia_rating_(CDR)", x = "mini_mental_state_examination_(MMSE)", orient="h", palette="Reds")


# In[21]:


# data exploration 

sns.regplot(x=CDR_df["normalize_whole_brain_volume%_(nWBV%)"], y=CDR_df["dementia_binary"], logistic=True, 
            scatter_kws={"color": "gray"}, 
            line_kws={"color": "green"})


# In[22]:


# data exploration

sns.boxplot(data = CDR_df, y="clinical_dementia_rating_(CDR)", x = "normalize_whole_brain_volume%_(nWBV%)", orient="h", palette="Greens")


# In[23]:


# checking for correlation between nWBV% and MMSE

print(scp.stats.pearsonr(CDR_df['normalize_whole_brain_volume%_(nWBV%)'], CDR_df["mini_mental_state_examination_(MMSE)"]))
sns.lmplot(data = CDR_df, x="mini_mental_state_examination_(MMSE)", y = "normalize_whole_brain_volume%_(nWBV%)")


# In[24]:


# exploration of relationships among biomedical variables
print("(r, p-value)")
print("nWBV% v. eTIV:", scp.stats.pearsonr(CDR_df['normalize_whole_brain_volume%_(nWBV%)'], CDR_df["estimated_total_intracranial_volume_(eTIV)"]))
print("nWBV% v. ASF:", scp.stats.pearsonr(CDR_df['normalize_whole_brain_volume%_(nWBV%)'], CDR_df["atlas_scaling _factor_(ASF)"]))
print("eTIV v. ASF:", scp.stats.pearsonr(CDR_df["estimated_total_intracranial_volume_(eTIV)"], CDR_df["atlas_scaling _factor_(ASF)"]))
sns.pairplot(CDR_df, vars=["normalize_whole_brain_volume%_(nWBV%)", "atlas_scaling _factor_(ASF)", "estimated_total_intracranial_volume_(eTIV)"], height = 3)


# In[ ]:




