// HistoryBar.js
import React from 'react';
import styled from 'styled-components';

// Define the styled components
const Navbar = styled.nav`
  background-color: white; /* Optional: background color */
  padding: 100px 70px 10px 40px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  color: black;
  font-family: 'Montserrat', sans-serif;
 height:100%;
 left:0;
  width: 350px; /* Fixed width */
  border-right:1px solid #c0392b;
  border-right:1px solid #ccc;
  position:fixed;
`;

const NavItem = styled.div`
  margin: 10px 0;
  cursor: pointer;
  &:hover {
    text-decoration: underline;
  }
`;

const PStyled = styled.h2`
padding:25px 0;
font-weight:700;
font-size:24px;
`

const items = ['Podate od Samochodu', 'Ryczałt z najmu', 'E- Faktura na JDG', 'Zmiany podatkowe 2025']; // Array of strings

const HistoryBar = () => {
  return (
    <>
   
    <Navbar>
    <PStyled>Historia zapytań</PStyled>
      {items.map((item, index) => (
        <NavItem key={index}>{item}</NavItem>
      ))}
    </Navbar>
    </>
  );
};

export default HistoryBar;