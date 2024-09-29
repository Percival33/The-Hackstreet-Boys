import React from 'react';
import styled from 'styled-components';

// Wrapper with flex row
const Wrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  padding: 20px;
  background-color: none;
  border-radius: 8px;
//   box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width:100%;
  max-width:70%;
  podition:relative;
  z-index:501;
`;

const NavButton = styled.a`
  margin: 10px 0;
  cursor: pointer;
  text-decoration: none;
  color: white;
  text-decoration: none;
  &:hover {
    // text-decoration: underline;
  }
  &:visited {
    color: white;
  }
`;

// Styled button
const StyledButton = styled.button`
  padding: 10px 20px;
  background-color: #0052a5;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1em;
  transition: background-color 0.3s, transform 0.3s;
  font-family:inherit;
  color:white;

  &:hover {
    background-color: #0056b3;
    // transform: scale(1.05);
    cursor:pointer
  }

  &:active {
    background-color: #004494;
  }

  &:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
    position:relative;
    z-index:501;
`;

const MidButtons = props => {
  return (
    <Wrapper>
      <StyledButton onClick={()=>props.newConversationHandler()}>Zacznij nowy czat</StyledButton>
      <StyledButton onClick={()=>props.pccHandler()}>Wypełnij PCC-3</StyledButton>
    </Wrapper>
  );
};

export default MidButtons;