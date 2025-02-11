# Alzheimer’s disease brain imaging analysis
## Introduction
Today, there are over 6.5 million people living with Alzheimer’s disease (AD) in America. According to the Alzheimer’s Association, this number is expected to climb to over 13 million by 2050. Alzheimer’s is the leading cause of dementia, which is a general term for symptoms related to mental decline (i.e., memory loss, reasoning impairment, or decline in other cognitive abilities). This progressive disease often starts with mild memory loss, but frequently progresses to a severe level in which an individual loses the ability to carry on a conversation, respond to their environment, or attend to their daily needs. With no cure at this point, there is a race to better understand this disease and to identify  treatments  for  patients  suffering with  Alzheimer’s.  

The Open Access Series of Imaging Studies (OASIS) is an important initiative with the express goal of “[making] neuroimaging data sets of the brain freely available to the scientific community.” Their hope is that important future discoveries in neuroscience can be stimulated by leveraging the collective insights of the scientific community at large. The data set is specifically from a 2007 study titled Open Access Series of Imaging Studies (OASIS): Cross-sectional MRI Data in Young, Middle Aged, Nondemented, and Demented Older Adults that was published in the Journal of Cognitive Neuroscience. The original study evaluates influential factors that may be predictive of receiving an AD diagnosis. 

This analysis investigates the predictive factors of dementia, though an imperfect measure, a useful proxy for AD. Our specific research question is: Can you use a person’s demographic data, industry anatomic measures of brain health, clinical data, and/or MRI scans to predict clinical dementia, thereby illuminating those who may be at risk of AD? 

OASIS has provided a cross-sectional dataset of 416 men and women between the ages of 18 to 96 with varied neurological health backgrounds. The dataset also includes a second MRI scan on a subsequent visit for 20 nondemented participants, administered within 90 days of their initial scan, to serve as a measure of reliability. This makes for a total of 436 observations in the data set (416 unique individuals; 20 follow up observations from nondemented participants). Among the study participants, 100 have been diagnosed with a mild to moderate form of dementia and the remaining participants have no known clinical indications of dementia (CDR > 0) or AD diagnoses.

An Alzheimer’s diagnosis is a binary outcome. However, the progression of dementia-related cognitive and behavioral aspects of Alzheimer disease is indicated by a Clinical Dementia Rating (CDR) score. The CDR ratings include: 0 = nondemented; 0.5 = very mild dementia; 1 = mild dementia; 2 = moderate dementia; 3 = severe. All participants had CDR scores ranging from 0 - 2 or a CDR score was unavailable. Additionally, all participants with dementia (CDR >0) were diagnosed with probable AD. The CDR score is the dependent variable in this analysis. 

The viability of the below independent variables, collected for each participant, as a means of predicting CDR score is explored:
The variables include the following:
gender                                 	
dominant hand                           	
age_in_years                          	
education_level                         	
socioeconomic_status_(SES)              	
mini_mental_state_examination_(MMSE) - a clinical assessment of cognitive function    	
estimated_total_intracranial_volume_(eTIV) - an estimate of intracranial cavity volume
normalize_whole_brain_volume_(nWBV)- an estimate of intracranial cavity volume normalized for head size
atlas_scaling _factor_(ASF) - a unitless scaling factor that is used in normalizing for head size

Understanding which, if any, of the independent demographic, clinical, and neuroimaging variables are associated with an increase in CDR score will help illuminate risk factors associated with dementia, a proxy for Alzheimer’s. To this end, our model will use logistic regression to evaluate the significance of relationships that exist between the dependent (CDR) and independent variables in our dataset.  
Clinical evaluations such as the CDR are the gold standard in diagnosing dementia. However, physicians also rely heavily on brain scans to help formulate their diagnoses. We would therefore expect the MRI-derived estimates eTIV, nWBV, and ASF to be related with CDR scores. Additionally, we expect demographic variables such as education level and SES to have an inverse linear relationship with CDR scores, as lower scores in these categories may be associated with limited access to medical resources.  

## Statistical Analysis
The results of the statistical tests using a logistic regression model are provided in Table 1. Age, MMSE, and nWBV% were all significant predictors of the likelihood of being diagnosed with dementia, controlling for SES, gender, and education level. Specifically, a one unit increase in age (1 year) was associated with a 1.11 times greater likelihood of being diagnosed with dementia. For MMSE and nWBV%, a one unit increase was associated with a 0.5 times less likelihood and 	1.13 times greater likelihood of being diagnosed with dementia, respectively. The significant positive relationship between MMSE and dementia may be because dementia is assessed using CDR, which is a similar evaluation consisting of a memory, problem-solving, and orientation assessments. Additionally, to our surprise, SES, gender, and education level were not significant predictors of dementia. 

Contrary to our hypotheses, the relationship between nWBV% and dementia likelihood was positive, meaning that higher brain volumes were associated with an increased likelihood of dementia diagnoses. Preliminary exploration into related literature suggests that the presence of Lewy bodies could be a factor, whereby the typical hippocampal shrinkage characterizing dementia may be counteracted by the presence of Lewy body masses in the brain (Kantarci et al., 2016). However, we are uncertain whether this relationship is due to Lewy bodies or may simply be an artifact of potential multicollinearity among our predictors, primarily MMSE and nWBV%. However, we ran an exploratory correlation analysis (see Appendix 2), and though the two were significantly correlated, the strength of the relationship was moderate (r = 0.48, p <0.001). Additionally, we ran an exploratory logistic regression removing MMSE, and the effect of nWBV% was still positive, suggesting it might not be a multicollinearity issue. 

## Prediction

Using our test set and a cutoff threshold of 0.5, our logistic regression model has an accuracy of 77%. The results of our model on predicting dementia are provided in Figure 1f. 

Our model was not able to reliably predict whether someone with dementia has dementia (of the 30 individuals who truly have dementia, our model only predicted a dementia diagnosis in 19). However, it was able to accurately predict a “no dementia” diagnosis in 31 out of 35 nondemented individuals. Moreover, lowering the cutoff threshold yielded better accuracy in certain instances and reduced the number of false negatives. However, we chose to keep the model’s default cutoff threshold of 0.5 as we are not aware of any industry precedent that suggests changing this level, and the relatively high percentage of false negatives may be due to our predictors or random noise within our test set.


1 Alzheimer’s Association: Alzheimer’s Disease and Dementia. “Alzheimer’s and Dementia.” Accessed May 10, 2022. https://alz.org/alzheimer_s_dementia

2 OASIS Brains Project. “About.” Accessed May 10, 2022. https://www.oasis-brains.org/#about

3 Neurology. “Hippocampal volumes predict risk of dementia with Lewy bodies in mild cognitive impairment” Accessed June 1, 2022. https://www.aan.com/PressRoom/home/PressRelease/1500
