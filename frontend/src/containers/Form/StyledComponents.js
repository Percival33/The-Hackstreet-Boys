import styled from 'styled-components';
import { Field, ErrorMessage } from 'formik';

export const StyledField = styled(Field)`
  font-family: inherit;
  padding: 10px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  box-sizing: border-box;
`;

export const StyledErrorMessage = styled(ErrorMessage)`
  color: red;
  font-size: 12px;
  margin-top: 5px;
`;