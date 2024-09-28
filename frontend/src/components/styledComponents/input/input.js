import React from 'react';
import styled from 'styled-components';

const StyledInput = styled.input`
  width: 100%;
  padding: 10px;
 
  border: 1px solid #d3d3d3;
  border-radius: 4px;
  font-size: 1em;
  font-family: 'Open Sans', sans-serif;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: border-color 0.2s;

  &:focus {
    border-color: #007BFF;
    outline: none;
  }
`;

export default StyledInput;