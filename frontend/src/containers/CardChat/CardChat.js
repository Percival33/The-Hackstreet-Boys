import React,{useState} from 'react';
import { FaPaperPlane,FaUser } from 'react-icons/fa'; // Import an icon from react-icons
import styled from 'styled-components';
import axios from 'axios';
import Card from '../../components/styledComponents/card/card';
import StyledInput from '../../components/styledComponents/input/input';
import emblem from '../../images/national-emblem.svg'


// Define the styled container component
const FlexContainer = styled.div`
  flex: 1; /* Take up all available space */
  width: 100%;
  padding:50px 0px 100px 400px;
  margin-top:70px;
  min-height: 100vh;
  hight:auto;
  display: flex;
  flex-direction: column; /* Adjust as needed */
  align-items: center; /* Adjust as needed */
  justify-content: space-between; /* Adjust as needed */
//   align-content:center;
  
  background-color: #f5f7fb;
`;

const Ul = styled.ul`
  display: flex;
  flex-wrap: wrap;
//   padding: 0 0 20px;
//   margin:0 0 18px;
  list-style: none;
  width: 100%;
  justify-content: space-between;
  position:fixed;
  bottom:50px;
  left:0;
  padding-left:380px;
`;

const InputWrapper = styled.div`
  position: fixed;
  bottom:10px;
  right:5px;
  padding-left:400px;
  width: 100%;
//    margin: 60px 0 2px;
`;
const StyledIcon = styled(FaPaperPlane)`
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
//   cursor: pointer;
   color: ${props => (props.disabled ? '#d3d3d3' : '#007BFF')};
   &:hover {
    cursor: ${props => (props.disabled ? 'not-allowed' : 'pointer')};
  }
`;

const UlMessages=styled.ul`
list-style-type:none;
width:100%;
display:flex;
flex-direction:column;
justify-content:center;
margin:auto;
align-items:center;
align-content:center;
margin-bottom:200px;
padding-bottom:200px;

`

const MessageModel = styled.section`
flex:1;
width:100%;
 max-width:70%;
margin:35px 0;
border: 2px solid #0052a5;
 border-radius:6px;
 padding:35px 30px;
 background-color:#fff;
 line-height:1.6;
//  transform: translateX(-30px);
`

const MessageUSer = styled.section`
flex:1;
background-color: #f5f7fb;
 max-width:70%;
width:100%;
 padding:35px 30px;
//  margin-right:20px;
//  border: 1px solid #d3d3d3; /* Light grey border */
 border: 2px solid #0052a5;

 border-radius:6px;
 line-height:1.6;
//   transform: translateX(30px);
 
`

const ImgWrap = styled.div`
display:flex;
align-items:center;
`



const Container = ({ children }) => {
    const [inputValue, setInputValue] = useState('');
    const [loading, setLoading] = useState(false);

    const handleCardClick = (content) => {
      setInputValue(content);
    };

    const [options, setOptions] = useState([
        { title: "Card 1", content: "This is the content of card 1." },
        { title: "Card 2", content: "This is the content of card 2." },
        { title: "Card 3", content: "This is the content of card 3." },
        { title: "Card 4", content: "This is the content of card 4." },
      ]);

      const [responses,setResponses]=useState([{txt:"Opowiedz o problemie",type:"model"}])

      
    
      const handleIconClick = async () => {
        setLoading(true);
        if (inputValue === '') {
            setLoading(false)
            return;
        }
// `Tera inny problem ${Math.floor(Math.random() * 100)}`
        try {
          setOptions([])
            const foo = await axios.get('https://jsonplaceholder.typicode.com/posts/1');
          console.log('Fetched data:',foo.data);
            setResponses([...responses,
               {txt:inputValue,type:'user'},
               {txt:`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin iaculis tincidunt elit, at convallis lacus tincidunt vitae. Suspendisse accumsan imperdiet orci eu venenatis. Pellentesque nec lorem at ligula lobortis rutrum. Nam nulla tellus, venenatis sit amet placerat ut, elementum id arcu. Vestibulum elit nunc, molestie vitae metus in ${Math.floor(Math.random() * 100)}`, type:'model'}    
                ])

        } catch (error) {
          console.error('Error fetching data:', error);
        }
        finally {
            setLoading(false);
            setInputValue('');
            setOptions([
                { title: "Card 1", content: `This is the content of card ${Math.floor(Math.random() * 100)}` },
                { title: "Card 2", content: `This is the content of card ${Math.floor(Math.random() * 100)}` },
                { title: "Card 3", content: `This is the content of card ${Math.floor(Math.random() * 100)}` },
                { title: "Card 4", content: `This is the content of card ${Math.floor(Math.random() * 100)}` },
              ])
          }
      };


 console.log(inputValue,responses)
 return <FlexContainer>
   <UlMessages>
  {responses.map((obj, index) => (
    // <li key={index}>
    <>
      {obj.type === 'model' ? (
       <>
       
       <MessageModel>
         <ImgWrap>
         <img src={emblem} alt="Logo" style={{ width: '25px',margin:'0 15px 0 0 ' }} /> 
         <h3 style={{display:'inline-block'}}>Asystent AI</h3>
         </ImgWrap>
       <br></br>
       
        {obj.txt}</MessageModel>
       </>
      ) : (
        <MessageUSer>
            <ImgWrap>
            <FaUser style={{ width: '25px', height: '25px', margin: '0 15px 0 0',color:'#0052a5' }}/>
            <h3 style={{display:'inline-block',color:'#0052a5'}}>Ty</h3>
            </ImgWrap>
            <br></br>
            {obj.txt}
            
            </MessageUSer>
      )}
      </>
    // </li>
  ))}
</UlMessages>
   


          <InputWrapper>
          <Ul>
            {options.map((card, index) => (
              <li key={index} style={{ margin: '10px' }}>
                <Card title={card.title} content={card.content} setInputValue={setInputValue}/>
              </li>
            ))}
          </Ul>

          <StyledInput placeholder="Type something..." 
        value={inputValue} 
        disabled={loading }
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            handleIconClick();
          }
        }}
        onChange={(e) => setInputValue(e.target.value)} />
        <StyledIcon onClick={handleIconClick} disabled={loading || inputValue === ''}/>
        </InputWrapper>
    </FlexContainer>;
};

export default Container;