import React from 'react';
import styled from 'styled-components';

// Define the styled components
const CardContainer = styled.div`
  background-color:#fff;
  border: 1px solid #d3d3d3; /* Light grey border */
  border-radius: 6px; /* Rounded corners */
  margin: 10px 0 0px;
  transition: transform 0.2s; /* Smooth hover effect */
  width:20vw;
  max-width:15vw;
  padding: 20px 16px;
  font-size:10px;

  display: flex;
  flex-direction: column;
  align-items: center;

  
  opacity:${props=>props.visible===true ? '1' : '0'};
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

const Card = (props,{ title, content,setInputValue }) => {
  return (
    <CardContainer onClick={()=> props.setInputValue(props.content)} visible={props.visible}>
      <CardContent>{props.content}</CardContent>
    </CardContainer>
  );
};

export default Card;