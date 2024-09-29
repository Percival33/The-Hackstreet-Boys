import React from 'react';
import * as Yup from 'yup';
import { StyledField, StyledErrorMessage } from '../StyledComponents'; // Import the styled components

export const dataValidationSchema = Yup.object().shape({
  data: Yup.date().required('Data is required'),
});

const Data = () => (
  <div>
    <label htmlFor="data">Data</label>
    <StyledField type="date" name="data" />
    <StyledErrorMessage name="data" component="div" />
  </div>
);

export default Data;