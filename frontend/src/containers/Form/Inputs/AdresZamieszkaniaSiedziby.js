import React from 'react';
import * as Yup from 'yup';
import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

export const adresZamieszkaniaSiedzibyValidationSchema = Yup.object().shape({
  rodzajAdresu: Yup.string().required('Rodzaj adresu is required'),
  KodKraju: Yup.string().required('Kod kraju is required'),
  Wojewodztwo: Yup.string().required('Wojewodztwo is required'),
  Powiat: Yup.string().required('Powiat is required'),
  Gmina: Yup.string().required('Gmina is required'),
  Ulica: Yup.string().required('Ulica is required'),
  NrDomu: Yup.string().required('Nr domu is required'),
  NrLokalu: Yup.string().required('Nr lokalu is required'),
  Miejscowosc: Yup.string().required('Miejscowosc is required'),
  KodPocztowy: Yup.string().matches(/^\d{2}-\d{3}$/, 'Kod pocztowy must be in the format XX-XXX').required('Kod pocztowy is required'),
});

const AdresZamieszkaniaSiedziby = () => (
  <div>
    <label htmlFor="rodzaj_adresu">Rodzaj Adresu</label>
    <StyledField type="text" name="rodzaj_adresu" />
    <StyledErrorMessage name="rodzaj_adresu" component="div" />

    <label htmlFor="kod_kraju">Kod Kraju</label>
    <StyledField type="text" name="kod_kraju" />
    <StyledErrorMessage name="kod_kraju" component="div" />

    <label htmlFor="wojewodztwo">Wojewodztwo</label>
    <StyledField type="text" name="wojewodztwo" />
    <StyledErrorMessage name="wojewodztwo" component="div" />

    <label htmlFor="powiat">Powiat</label>
    <StyledField type="text" name="powiat" />
    <StyledErrorMessage name="powiat" component="div" />

    <label htmlFor="gmina">Gmina</label>
    <StyledField type="text" name="gmina" />
    <StyledErrorMessage name="gmina" component="div" />

    <label htmlFor="ulica">Ulica</label>
    <StyledField type="text" name="ulica" />
    <StyledErrorMessage name="ulica" component="div" />

    <label htmlFor="nr_domu">Nr Domu</label>
    <StyledField type="text" name="nr_domu" />
    <StyledErrorMessage name="nr_domu" component="div" />

    <label htmlFor="nr_lokalu">Nr Lokalu</label>
    <StyledField type="text" name="nr_lokalu" />
    <StyledErrorMessage name="nr_lokalu" component="div" />

    <label htmlFor="miejscowosc">Miejscowosc</label>
    <StyledField type="text" name="miejscowosc" />
    <StyledErrorMessage name="miejscowosc" component="div" />

    <label htmlFor="kod_pocztowy">Kod Pocztowy</label>
    <StyledField type="text" name="kod_pocztowy" />
    <StyledErrorMessage name="kod_pocztowy" component="div" />
  </div>
);

export default AdresZamieszkaniaSiedziby;