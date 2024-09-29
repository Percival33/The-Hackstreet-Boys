import React from 'react';
import * as Yup from 'yup';
import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

export const podmiot1ValidationSchema = Yup.object().shape({
  rola: Yup.string().required('Rola is required'),
});

const Podmiot1 = () => (
  <div>
    <label htmlFor="rola">Rola</label>
    <StyledField type="text" name="rola" />
    <StyledErrorMessage name="rola" component="div" />
  </div>
);

export default Podmiot1;