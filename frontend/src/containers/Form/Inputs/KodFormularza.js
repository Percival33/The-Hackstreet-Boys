import React from 'react';
import * as Yup from 'yup';
import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

export const kodFormularzaValidationSchema = Yup.object().shape({
  kodSystemowy: Yup.string().required('Kod systemowy is required'),
  kodPodatku: Yup.string().required('Kod podatku is required'),
  rodzajZobowiazania: Yup.string().required('Rodzaj zobowiazania is required'),
  wersjaSchemy: Yup.string().required('Wersja schemy is required'),
});

const KodFormularza = () => (
  <div>
    <label htmlFor="kod_systemowy">Kod Systemowy</label>
    <StyledField type="text" name="kod_systemowy" />
    <StyledErrorMessage name="kod_systemowy" component="div" />

    <label htmlFor="kod_odatku">Kod Podatku</label>
    <StyledField type="text" name="kod_podatku" />
    <StyledErrorMessage name="kodPodatku" component="div" />

    <label htmlFor="rodzaj_zobowiazania">Rodzaj Zobowiazania</label>
    <StyledField type="text" name="rodzaj_zobowiazania" />
    <StyledErrorMessage name="rodzajZobowiazania" component="div" />

    <label htmlFor="wersja_schemy">Wersja Schemy</label>
    <StyledField type="text" name="wersja_schemy" />
    <StyledErrorMessage name="wersja_schemy" component="div" />
  </div>
);

export default KodFormularza;