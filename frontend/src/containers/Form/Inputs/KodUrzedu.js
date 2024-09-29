import React from 'react';
import * as Yup from 'yup';
import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

export const kodUrzeduValidationSchema = Yup.object().shape({
  kodUrzedu: Yup.string().required('Kod urzedu is required'),
});

const KodUrzedu = () => (
  <div>
    <label htmlFor="kod_urzedu">Kod Urzedu</label>
    <StyledField type="text" name="kod_urzedu" />
    <StyledErrorMessage name="kod_urzedu" component="div" />
  </div>
);

export default KodUrzedu;