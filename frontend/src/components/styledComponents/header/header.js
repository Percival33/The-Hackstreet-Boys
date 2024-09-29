// header.js
import React from 'react';
import styled from 'styled-components';
import emblem from '../../../images/national-emblem.svg';


const HeaderContainer = styled.header`
  background-color:#fff;
  padding: 20px;
  color: black;
  text-align: center;
  font-family: 'Montserrat', sans-serif;
  width: 100%;
  border-bottom:1px solid #ccc;
  font-weight:bold;
   display: flex;
  align-items: center;
  justify-content: left;
  position:fixed;
  z-index:999;
  width:100%:
  height:80px;
`;

const Title = styled.h1`
  font-size: 20px;
  margin: 0;
  font-family: 'Montserrat', sans-serif;
  text-align: left;
  font-weight:bold;
`;


const Header = props => {
  return (
    <HeaderContainer>
       <img src={emblem} alt="Logo" style={{ width: '25px',margin:'0 5px 0 0 ' }} />
      <Title>{props.children}</Title>
    </HeaderContainer>
  );
};

export default Header;