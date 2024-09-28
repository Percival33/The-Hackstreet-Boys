// HistoryBar.js
import React from 'react';
import styled from 'styled-components';

// Define the styled components
const Navbar = styled.nav`
  background-color: #282c34;
  background-color:#0052a5;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: white;
  font-family: 'Montserrat', sans-serif;
  position:fixed;
`;

const NavItem = styled.div`
  margin: 0 10px;
  cursor: pointer;
  &:hover {
    text-decoration: underline;
  }
`;

const NavItemsContainer = styled.div`
  display: flex;
  align-items: center;
`;

const HistoryBar = () => {
  return (
    <Navbar>
      <NavItemsContainer>
        <NavItem>Version 1</NavItem>
        <NavItem>Version 2</NavItem>
        <NavItem>Version 3</NavItem>
      </NavItemsContainer>
      <NavItemsContainer>
        <NavItem>Settings</NavItem>
        <NavItem>Logout</NavItem>
      </NavItemsContainer>
    </Navbar>
  );
};

export default HistoryBar;