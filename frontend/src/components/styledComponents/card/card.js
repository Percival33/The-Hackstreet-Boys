import React from 'react';
import styled from 'styled-components';

// Define the styled components
const CardContainer = styled.div`
  // background-color:#0052a5;
  background-color:#fff;
  border: 1px solid #d3d3d3; /* Light grey border */
  border-radius: 6px; /* Rounded corners */
  //box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
  // padding: 20px 0;
  margin: 25px 0 0px;
  transition: transform 0.2s; /* Smooth hover effect */
  // width:300px;
  // height:400px;
  width:20vw;
  max-width:15vw;
  padding: 20px 16px;
  // color:black;

  display: flex;
  flex-direction: column;
  align-items: center;

  
  
  &:hover {
    transform: translateY(-5px); /* Lift on hover */
    cursor:pointer;
  }
`;

const CardTitle = styled.h2`
  font-size: 1.5em;
  margin: 20px 0;
  font-family: 'Montserrat', sans-serif;
`;

const CardContent = styled.p`
  font-size: 1em;
  color: #000;
  margin: 5px 0;
  font-family: 'Open Sans', sans-serif;
  line-height: 1.6;
`;

const Card = ({ title, content,setInputValue }) => {
  return (
    <CardContainer onClick={()=> setInputValue(content)}>
      {/* <CardTitle>{title}</CardTitle> */}
      <CardContent>{content}</CardContent>
    </CardContainer>
  );
};

export default Card;