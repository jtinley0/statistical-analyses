
# Hypertension Drug Market Analysis

## Abstract 
This analysis investigates the factors influencing the likelihood of receiving treatment for hypertension, with a focus on patient, physician, and drug characteristics. Using logistic regression, the study examines the binary outcome of whether a patient is prescribed medication, specifically comparing patients treated by cardiologists to those treated by family physicians. The key finding reveals that seeing a cardiologist at least once increases a patient's likelihood of receiving treatment (consuming HT drugs) by 2.23 times relative to family medicine providers. This effect is observed regardless of patient gender, age, comorbid diagnoses, or previous diagnoses from other specialties, including nephrology.

Further analysis of treatment levels, using linear regression & LASSO with total days' supply as the outcome variable, indicates that patients prescribed less common drugs, such as those other than Lisinopril (the most commonly prescribed medication observed), consumed significantly fewer days of supply. On average, these patients consumed 211 fewer days of medication compared to those prescribed Lisinopril. Notably, hypertensive drug consumption is price inelastic in the observed sample. 

Key insights from this study emphasize the importance of targeting women, who present with hypertension at younger ages, for earlier intervention. Marketing efforts should prioritize outreach to cardiologists, as they play a critical role in both diagnosing and treating hypertension. Overall, the findings suggest that while cardiologists are more likely to prescribe treatment, they do not influence the quantity of medication prescribed, and drug pricing does not impact patient consumption.

## Overview
- According to WHO (World Health Organization), more than 1.13 billion people are suffering from hypertension globally
- Global Market size in 2022: $30.5B and expected to exceed $40B by 2031 (with an estimated annual growth rate of 3.1%)
- Some key competitors
  - AstraZeneca PLC (DUTOPROL, ZESTORETIC, and ZESTRIL)
  - Johnson & Johnson Services, Inc (OPSUMIT, TRACLEER, UPTRAVI, VELETRI, and VENTAVIS)
  - Merck & Co., Inc. (COZAAR, HYZAAR, and PRINIVIL)
  - Novartis AG (DIOVAN, DIOVAN HCT, ENTRESTO, EXFORGE HCT, and LOTREL)
  - Pfizer Inc. (ACCURETIC, NORVASC, and REVATIO)
 
## Hypertension Definitions
- Hypertension (AKA high blood pressure) - a common condition that affects the body's arteries and forces the heart to work harder
  - many medical classifications for hypertension
  - For the purpose of this analysis, there are two broad types of hypertension:
    
### Essential Primary Hypertension 
- Broadest, most inclusive category
- No identifiable cause of hypertension

### Other Forms of Hypertension 
- Typically co-occur with other identifiable diagnoses (e.g., kidney disease)

## Sample characteristics 
- Data composition
 - 200 patients diagnosed with Essential (Primary) Hypertension
 - 105 females, 95 males
 - All of their diagnoses (hypertension or otherwise) over a 5-year period (March 2014 - March 2019)
 - and for 139 of these patients, we also have their prescription consumption data (assuming 81 were not prescribed)
- Data features
  - Patient level
   - Demographic data: age, gender
   - Drug data: e.g., prescription cost to patient, drug brand name
   - Diagnoses data: e.g, diagnosis description
 - Physician level
  - physician specialty

## TAKEAWAYS AND RECOMMENDATIONS
- Takeaways (of the present analysis)
  - Though patient demographic insights were limited, women present with hypertension younger and should be targeted earlier
  - Marketing efforts should prioritize cardiologist outreach due to their integral role in both diagnosis and likelihood of treating of hypertension
  - Quantity of hypertensive drug supply is not influenced by price to patient, nor who prescribed the drug 
- Future recommendations and follow-ups
  - Need non-hypertensive comparison diagnosis data: This will enable prediction of who is most likely to get hypertension and reach out to them before receiving the diagnosis
  - Though consumers here were mostly price insensitive. Future work could consider more rigorously testing price sensitivities (e.g., conjoint analyses).
  - Need more diverse data: least common physician specialties and drugs were all grouped in “Other” category






