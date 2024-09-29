import React from 'react';
import * as Yup from 'yup';
import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

export const celZlozeniaValidationSchema = Yup.object().shape({
  celZlozenia: Yup.number().required('Cel zlozenia is required'),
});

const CelZlozenia = () => (
  <div>
    <label htmlFor="cel_zlozenia">Cel Zlozenia</label>
    <StyledField type="number" name="cel_zlozenia" />
    <StyledErrorMessage name="cel_zlozenia" component="div" />
  </div>
);

export default CelZlozenia;