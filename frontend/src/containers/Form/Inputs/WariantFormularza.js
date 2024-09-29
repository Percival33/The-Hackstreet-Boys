import React from 'react';
import * as Yup from 'yup';
import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

export const wariantFormularzaValidationSchema = Yup.object().shape({
  wariantFormularza: Yup.number().required('Wariant formularza is required'),
});

const WariantFormularza = () => (
  <div>
    <label htmlFor="wariant_formularza">Wariant Formularza</label>
    <StyledField type="number" name="wariant_formularza" />
    <StyledErrorMessage name="wariant_formularza" component="div" />
  </div>
);

export default WariantFormularza;