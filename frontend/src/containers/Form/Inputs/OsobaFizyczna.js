import React from 'react';
import * as Yup from 'yup';
import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

export const osobaFizycznaValidationSchema = Yup.object().shape({
  PESEL: Yup.string().matches(/^\d{11}$/, 'PESEL must be 11 digits').required('PESEL is required'),
  ImiePierwsze: Yup.string().required('Imie Pierwsze is required'),
  Nazwisko: Yup.string().required('Nazwisko is required'),
  DataUrodzenia: Yup.date().required('Data Urodzenia is required'),
});

const OsobaFizyczna = () => (
  <div>
    <label htmlFor="pesel">PESEL</label>
    <StyledField type="text" name="pesel" />
    <StyledErrorMessage name="pesel" component="div" />

    <label htmlFor="imie_pierwsze">Imie Pierwsze</label>
    <StyledField type="text" name="imie_pierwsze" />
    <StyledErrorMessage name="imie_pierwsze" component="div" />

    <label htmlFor="nazwisko">Nazwisko</label>
    <StyledField type="text" name="nazwisko" />
    <StyledErrorMessage name="nazwisko" component="div" />

    <label htmlFor="data_urodzenia">Data Urodzenia</label>
    <StyledField type="date" name="data_urodzenia" />
    <StyledErrorMessage name="data_urodzenia" component="div" />
  </div>
);

export default OsobaFizyczna;