import React,{useState,useEffect} from 'react';
import { FaPaperPlane,FaUser } from 'react-icons/fa'; // Import an icon from react-icons
import { Oval } from 'react-loader-spinner';
import styled from 'styled-components';
import ReactMarkdown from 'react-markdown';
import MidButtons from '../../components/styledComponents/midButtons/midButtons';
import axios from 'axios';
import Card from '../../components/styledComponents/card/card';
import StyledInput from '../../components/styledComponents/input/input';
import emblem from '../../images/national-emblem.svg'
import Form from '../Form/Form'


const FlexContainer = styled.div`
  flex: 1; /* Take up all available space */
  width: 70%;
  // padding:50px 0px 200px 400px;
  margin-top:70px;
  min-height: 100vh;
  hight:auto;
  display: flex;
  flex-direction: column; /* Adjust as needed */
  align-items: center; /* Adjust as needed */
  align-content: center; /* Adjust as needed */
  justify-content: space-between; /* Adjust as needed */
  background-color: #f5f7fb;
  position:relative;
  padding: ${props => (props.isPcc ? '50px 0px 100px 1px' : '50px 0px 100px 400px')};
  max-width: ${props => (props.isPcc ? '60%' : 'auto')};
  transition: padding 0.3s;
`;

const ScrollableWrapper = styled.div`
  height: 80vh;
  overflow-y: auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  // margin-top:200px;
  position:fixed;
  top:100px;
  right:50px;
  width:500px;
`;

const Ul = styled.ul`
flex: 0 0 auto;
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  width: 100%;
  justify-content: space-between;
  // position:fixed;
  bottom:50px;
  left:0;
  // padding-left:${props=>props.isPcc ? '200px' : '400px'};  
  padding:20px;
  max-width: ${props => (props.isPcc ? '50%' : 'auto')};
  max-height:300px;
  transition: 0.3s;
  // align-items:center;
  // align-content:center;
  // align-self:scretch
  
`;

const InputWrapper = styled.div`
  position: fixed;
  bottom:10px;
  left:400px;
  // padding-left:400px;
  width: ${props=>props.isPcc ? '50%' : '70%'};
  // width:70%;
  opacity: ${props => (props.visible === false ? 0 : 1)};
  display:flex;
  flex-direction:column;
  align-items:center;
  align-content:center;
  transform: ${props => props.isPcc ? "translateX(-300px)":"translateX(0)" };
`;
const StyledIcon = styled(FaPaperPlane)`
  position: absolute;
  right: 10px;
  bottom:8px;
  transform: translateY(-50%);
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
padding-bottom:${props=>props.isPcc ? '300px' : '200px'};
// padding-bottom:200px;

`

const MessageModel = styled.section`
flex:1;
width:100%;
//  max-width:70%;
margin:35px 0;
border: 2px solid #0052a5;
 border-radius:6px;
 padding:35px 50px;
 background-color:#fff;
 line-height:1.7;
 width:600px;
`

const MessageUSer = styled.section`
flex:1;
background-color: #f5f7fb;
//  max-width:70%;
// width:100%;
width:600px;
 padding:35px 30px;
 border: 2px solid #0052a5;

 border-radius:6px;
 line-height:1.6;
 
`

const ImgWrap = styled.div`
display:flex;
align-items:center;
`
const StyledXmlButton = styled.button`
  padding: 20px;
  background-color: #0052a5;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family:inherit;
  display: block;
  margin:10px auto;
  &:disabled {
    background-color: #ccc;
  }
`;


const Container = (props) => {
    const [inputValue, setInputValue] = useState('');
    const [loading, setLoading] = useState(false);
    const [conversation_id, setConversation_id] = useState(null);
    const [responses,setResponses]=useState([{txt:"Opowiedz o problemie",type:"model"}])
    const [actionToPerform, setActionToPerform] = useState(null);
    const [areMidButtonsVisible, setAreMidButtonsVisible] = useState(false);
    const [isPcc3Flow, setIsPcc3Flow] = useState(false);
    const [formObj, setFormObj] = useState(null);
    const[entireResponses,setEntireResponses]=useState(null)
    const [xmlObject, setXmlObject] = useState(null);
    // const 

    const handleDownload = () => {
      if (!!(entireResponses?.xml)) {
        // Parse the XML string
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(entireResponses.xml, "application/xml");
  
        // Serialize the XML document back to a string
        const serializer = new XMLSerializer();
        const xmlString = serializer.serializeToString(xmlDoc);
  
        // Create a Blob from the XML string
        const blob = new Blob([xmlString], { type: 'application/xml' });
  
        // Create a link element
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'response.xml';
  
        // Programmatically click the link to trigger the download
        link.click();
  
        // Clean up the URL object
        URL.revokeObjectURL(link.href);
      }
    };

    const handleCardClick = (content) => {
      setInputValue(content);
    };


    const [options, setOptions] = useState([
    "Chcę zapłacić podatek","Jak uniknąć podwójnego opodatkowania","Chcę wdrożyć system e-faktur","Jak zoptymalizować podatki" 
    ]);


    useEffect(() => {
    if(!!props.isId){
      // setResponses(props.conversation_obj)
      setEntireResponses(props.conversation_obj)
      
      setConversation_id(props.conversation_id)
      console.log('TUTAJ')
    }
    },[props]);  

    useEffect(() => {
      if(!!entireResponses){
      setFormObj(entireResponses.form)
      
      }
      if (!!(entireResponses?.xml)){

      }
      if(!!entireResponses && !isPcc3Flow){
      const arr_of_actionsToProceed = entireResponses.messages.filter(obj => !!obj.action_to_perform)
      console.log('wszystkie actions to proceed',arr_of_actionsToProceed)
      setIsPcc3Flow(arr_of_actionsToProceed.length>0)
      }
     
    }, [entireResponses]);

useEffect(() => {
  if(isPcc3Flow){
    props.setIsHidden(true)
  }
}, [isPcc3Flow]);

    useEffect(() => { 
   if(!!actionToPerform){

  // const _responses = [...responses]
  // _responses.pop()
  // let newText = `${actionToPerform.description}`;
  // const links  = [...actionToPerform.references]
  // links.forEach(link => {
  //   newText += `\n\n`;
  //   newText += `[${link}](${link})`;
  // });
  // links.forEach(link => {
  //   newText += `\n\n`;
  //   newText += `<a href="${link}" target="_blank">${link}</a>`;
  // });

  // setResponses([..._responses,{text:newText,type:'ASSISTANT'}])
  // setAreMidButtonsVisible(true)
  }
    }, [actionToPerform]);

    // useEffect(() => {
    //     const fetchData = async () => {
    //       try {
    //         const foo = await axios.get('https://jsonplaceholder.typicode.com/posts/1');
    //         console.log('Fetched data:',foo.data);
    //       } catch (error) {
    //         console.error('Error fetching data:', error);
    //       }
    //     };
    //     fetchData();
    // }, []);
    
      const handleIconClick = async () => {
        setLoading(true);
        if (inputValue === '') {
            setLoading(false)
            return;
        }
        try {
          // setOptions([])
          console.log('conversation_id before post: ',conversation_id)
            const foo = await axios.post('https://www.asystentpodatkowyai.pl/api/conversation', {
            // const foo = await axios.post(`https://www.asystentpodatkowyai.pl/${isPcc3Flow? 'form':'conversation'}`, {
              text: inputValue,
              conversation_id:conversation_id

            });
          console.log('Fetched data:',foo.data);
          setConversation_id(foo.data.conversation_id)
          setEntireResponses(foo.data)
          if(!!foo.data && !isPcc3Flow){
          const arr_of_actionsToProceed = foo.data.messages.filter(obj => !!obj.action_to_perform)
          console.log('wszystkie actions to proceed w axios',arr_of_actionsToProceed)
          setIsPcc3Flow(arr_of_actionsToProceed.length>0)
          }

            // setResponses([...responses,
            //    {txt:inputValue,type:'user'},
            //    {txt:`Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin iaculis tincidunt elit, at convallis lacus tincidunt vitae. Suspendisse accumsan imperdiet orci eu venenatis. Pellentesque nec lorem at ligula lobortis rutrum. Nam nulla tellus, venenatis sit amet placerat ut, elementum id arcu. Vestibulum elit nunc, molestie vitae metus in ${Math.floor(Math.random() * 100)}`, type:'model'}    
            //     ])
            // setResponses(foo.data.messages)
            // setOptions(foo.data.messages[foo.data.messages.length-1].choices)
            // setActionToPerform(foo.data.messages[foo.data.messages.length-1].action_to_perform)
            // if(foo.data.messages[foo.data.messages.length-1])


        } catch (error) {
          console.error('Error fetching data:', error);
        }
        finally {
          console.log('conversation_id finally: ',conversation_id)  
          console.log('text finally: ',inputValue)
          setLoading(false);
            setInputValue('');
            // setOptions([
            //     { title: "Card 1", content: `This is the content of card ${Math.floor(Math.random() * 100)}` },
            //     { title: "Card 2", content: `This is the content of card ${Math.floor(Math.random() * 100)}` },
            //     { title: "Card 3", content: `This is the content of card ${Math.floor(Math.random() * 100)}` },
            //     { title: "Card 4", content: `This is the content of card ${Math.floor(Math.random() * 100)}` },
            //   ])
           
          }
      };


//  console.log('input value, reponses',inputValue,responses)
//  console.log('props',props)
//  console.log('conversation_id',conversation_id)
//  console.log('options',options)
//  console.log('actionToPerform',actionToPerform)
console.log('formObj',formObj)
console.log('entireResponses',entireResponses)
console.log('conversation_id',conversation_id)
console.log('inputValue',inputValue)
console.log('isPcc3Flow',isPcc3Flow)
 return(
 <>
 <FlexContainer isPcc={isPcc3Flow}>
   <UlMessages isPcc={isPcc3Flow}>
  {(!!entireResponses&&entireResponses.messages.length>0)&& entireResponses.messages.map((obj, index) => (
    <>
      {obj.type != 'USER' ? (
       <>
       <MessageModel>
         <ImgWrap>
         <img src={emblem} alt="Logo" style={{ width: '25px',margin:'0 15px 0 0 ' }} /> 
         <h3 style={{display:'inline-block'}}>Asystent AI</h3>
         </ImgWrap>
       <br></br>
       
       {/* {!!obj.action_to_perform? <ReactMarkdown>{obj.action_to_perform.description}</ReactMarkdown> : <ReactMarkdown>{obj.text}</ReactMarkdown>} */}
       <ReactMarkdown>{obj.text}</ReactMarkdown>
       
        </MessageModel>
       </>
      ) : (
        <MessageUSer>
            <ImgWrap>
            <FaUser style={{ width: '25px', height: '25px', margin: '0 15px 0 0',color:'#0052a5' }}/>
            <h3 style={{display:'inline-block',color:'#0052a5'}}>Ty</h3>
            </ImgWrap>
            <br></br>
            {obj.text}
            
            </MessageUSer>
      )}
      </>
  ))}

{/* {areMidButtonsVisible && <MidButtons pccHandler={()=>{
  setAreMidButtonsVisible(false)
  setIsPcc3Flow(true)
  // setIsO
  //post new conversation
}
}
newConversationHandler={()=>{
  setAreMidButtonsVisible(false)
  setInputValue('')
  // setResponses([{txt:"Opowiedz o problemie",type:"model"}])
  setConversation_id(null)
  // setActionToPerform(null)
  setOptions(["Chcę zapłacić podatek","Jak uniknąć podwójnego opodatkowania","Chcę wdrożyć system e-faktur","Jak zoptymalizować podatki" ])
  setEntireResponses(null)
}}

/>} */}
</UlMessages>
          <InputWrapper visible={true} isPcc={isPcc3Flow}>
          <Ul >
          
          {!entireResponses && options.map((card, index) => (
  <li key={index} style={{ margin: '10px' }}>
    <Card title={card} content={card} setInputValue={setInputValue} 
    visible={!loading}
    // visible={true}
     />
  </li>
))}
           
           {(!isPcc3Flow && !!entireResponses ) && entireResponses.messages[entireResponses.messages.length-1]?.choices?.map((card, index) => (
              <li key={index} style={{ margin: '10px' }}>
                <Card title={card} content={card} setInputValue={setInputValue}  
                visible={!loading} 
                // visible={true}
                />
              </li>
            ))}
            

            {loading &&  <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center',margin:'0 auto 10px' }}>
        <Oval
          height={70}
          width={70}
          color="#0052a5"
          visible={true}
          ariaLabel="oval-loading"
          secondaryColor="#f0f0f0"
          strokeWidth={2}
          strokeWidthSecondary={2}
        />
      </div>}
          </Ul>

          <StyledInput placeholder="Type something..." 
        value={inputValue}
        // isPcc={isPcc3Flow} 
        disabled={loading 
          // || !!actionToPerform
        }
        // visible={!actionToPerform}
        onKeyDown={(e) => {
          if (e.key === 'Enter') {
            handleIconClick();
          }
        }}
        onChange={(e) => setInputValue(e.target.value)} />
        <StyledIcon onClick={handleIconClick} disabled={loading || inputValue === ''}/>
        </InputWrapper>
    </FlexContainer>;
        { isPcc3Flow &&
         <ScrollableWrapper>
          {/* <Form formObj={entireResponses.form}/> */}
            <>
            <Form formObj={entireResponses.form}/>
            <StyledXmlButton onClick={handleDownload}disabled={!(entireResponses?.xml)}>Download XML</StyledXmlButton>
            </>
         </ScrollableWrapper>
         }
    </>)
};

export default Container;