import React,{useState,useEffect} from 'react';
import styled from 'styled-components';
import { Link,navigate } from 'gatsby';
import { FaArrowLeft, FaArrowRight } from 'react-icons/fa'; // Import icons from react-icons
import axios, { all } from 'axios'

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
  z-index: 998;
  transition: transform 0.3s ease-in-out;
  transform: ${({ isHidden }) => (isHidden ? 'translateX(-90%)' : 'translateX(0)')};
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

const NavButton = styled.a`
  margin: 10px 0;
  cursor: pointer;
  text-decoration: none;
  color: black;
  text-decoration: none;
  &:hover {
    text-decoration: underline;
  }
  &:visited {
    color: black;
  }
`;

const HideButton = styled.button`
  position: fixed;
  top: 10%;
  left:325px;
  cursor: pointer;
   transition: transform 0.3s ease-in-out;
  transform: ${({ isHidden }) => (isHidden ? 'rotate(180deg)' : 'rotate(0deg)')};
  z-index: 1000;
  border:none;
  background:none;
  font-size:20px;
`;

const items = [
  { id: 1, txt: 'Podate od Samochodu', NavLink: '?conversation_id=2137' },
  { id: 2, txt: 'Ryczałt z najmu', NavLink: '&conversation_id=2' },
  { id: 3, txt: 'E- Faktura na JDG', NavLink: '&conversation_id=3' },
  { id: 4, txt: 'Zmiany podatkowe 2025', NavLink: '&conversation_id=4' }
];



const HistoryBar = props => {
  const [isHidden, setIsHidden] = useState(false);
  // const [allConversations, setAllConversations] = useState([]);

  const toggleNavbar = () => {
    setIsHidden(!isHidden);
  };

  // useEffect(() => {
  //   const fetchConversations = async () => {
  //     try {
  //       const foo = await axios.get('http://95.217.184.211:8080/all_conversations');
  //       setAllConversations(foo.data);
  //     } catch (error) {
  //       console.error('Error fetching conversations:', error);
  //     }
  //   };
  
  //   fetchConversations();
  // }, []);
  
  const handleClick = (id) => {
    const currentUrl = window.location.pathname;
    navigate(`${currentUrl}?conversation_id=${id}`, { replace: true });
  };

  console.log('all conversations props',props.allConversations)
  
  return (
    <>
   
    <Navbar isHidden={isHidden}>
    <HideButton onClick={toggleNavbar} isHidden={isHidden}>
    <FaArrowLeft style={{color:'#0052a5'}}/>
        </HideButton>
    <PStyled>Historia zapytań</PStyled>
    <NavButton href={`/`}>Nowy czat</NavButton>
      {props.allConversations.map((item, index) => (
        <NavItem key={index} 
        >
          <NavButton href={`?conversation_id=${item.conversation_id}`}>{`${item.messages[0].text.substring(0, 35)}...`}</NavButton>
          </NavItem>
      ))}
    </Navbar>
    </>
  );
};

export default HistoryBar;