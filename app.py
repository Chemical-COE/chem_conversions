import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to the Chem Conversion App')
st.write('For more information reach out or make requests to the author: cfirkins@amafca.org')

st.info('Here we calculate the pH of a monoprotic weak Acid in Water')
st.write('The pka of Formic acid is 3.75 g/mol')
st.write('The molar mass mass of Formic acid is 46.03 g/mol')

chem_name = st.text_input(label = 'Input the Chemical Name')
st.write(f'The entered Chemical is {chem_name}')

pka = st.number_input(label = 'Input the Pka')
st.write(f'The entered pka is {pka}')

molar_mass = st.number_input(label = 'Input the Molar Mass in grams per mol')
st.write(f'The entered molar mass is {molar_mass} g/mol')       

conc = st.number_input(label = 'Enter the desired pH ex 7.0')
st.write(f'The target pH is {conc}')

vol = st.number_input(label = 'Enter the volume of water in gallons')
st.write(f'The target volume is {vol} gallons')

vol_liters = vol * 3.78541
h_plus = 10 ** (-conc)
ka = 10 ** (-pka)

molarity = (h_plus**2 / ka) + h_plus
grams = molarity * vol_liters * molar_mass

results_dic = {
    'Chemical Name': [chem_name],
    'pKa': [pka],
    'Molar Mass': [molar_mass],
    'Target pH': [conc],
    'Target Volume (gal)': [vol],
    'Calculated Molarity': [molarity],
    'Mass Needed (Grams)': [grams],
}

st.success(f'You need **{grams:.4f} grams** of solute.')
df = pd.DataFrame(results_dic)

st.write('Download Your Report Below :D')
st.dataframe(df)

# Optional: Adds an actual CSV download button
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label='Download CSV',
    data=csv,
    file_name='chem_report.csv',
    mime='text/csv',
)
