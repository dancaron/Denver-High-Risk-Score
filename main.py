import streamlit as st

# Title and description
st.title('Denver HIV Risk Score Calculator')

st.markdown("""
### Calculate your Denver HIV Risk Score
The Denver HIV Risk Score is a clinical tool that helps determine the likelihood of undiagnosed HIV infection based on specific demographic and risk factors. This tool is primarily used in healthcare settings but can also be a general guide for individuals who want to assess their risk level.
Please enter the following details to calculate your score.
""")

# Input fields for the risk factors
age = st.selectbox('Age Group:', ['Under 30', '30-39', '40 and older'])
sex = st.radio('Sex:', ['Male', 'Female'])
race = st.selectbox('Race/Ethnicity:', ['White', 'Black', 'Hispanic/Latino', 'Other'])
msm = st.radio('Men who have sex with men (MSM):', ['Yes', 'No'])
sti = st.radio('Diagnosed with sexually transmitted infection (STI):', ['Yes', 'No'])
iv_drug_use = st.radio('Intravenous drug use:', ['Yes', 'No'])
high_risk_sex_partner = st.radio('Sex with a high-risk partner (e.g., HIV+, IV drug user):', ['Yes', 'No'])
condom_use = st.radio('Inconsistent condom use:', ['Yes', 'No'])

# Scoring based on input
score = 0

if age == 'Under 30':
    score += 6
elif age == '30-39':
    score += 5

if sex == 'Male':
    score += 2

if race == 'Black':
    score += 5
elif race == 'Hispanic/Latino':
    score += 3

if msm == 'Yes':
    score += 7

if sti == 'Yes':
    score += 6

if iv_drug_use == 'Yes':
    score += 3

if high_risk_sex_partner == 'Yes':
    score += 5

if condom_use == 'Yes':
    score += 5

# Display the calculated score
st.subheader(f'Your Denver HIV Risk Score: {score}')

# Add interpretation of the score
st.markdown("""
### Interpretation:
- A score below 20 indicates low risk.
- A score between 20 and 30 indicates moderate risk.
- A score above 30 indicates high risk. You may consider getting tested for HIV.
""")
