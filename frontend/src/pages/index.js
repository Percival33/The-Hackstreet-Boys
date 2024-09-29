import React from "react"
import { useState,useEffect } from "react"
import { Link } from "gatsby"
import styled from "styled-components"
import { useLocation } from '@reach/router';

import Layout from "../components/layout"
import Seo from "../components/seo"

import Header from '../components/styledComponents/header/header'
import NavBar from '../components/styledComponents/navBar/navBar';
import HistoryBar from '../components/styledComponents/historyBar/historyBar';
import FlexContainer from '../containers/CardChat/CardChat';
import axios, { all } from 'axios'


const Wrapper = styled.div`
  display: flex;
  flex-direction: row;
   height: 90vh; /* Full height */
  min-height:600px;
  // align-items: center;
  // justify-content: center;

  
  
  `

  // const testPastCOnversation=

 

const IndexPage = () => {
  const [isHidden, setIsHidden] = useState(false);

  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const conversation_id = params.get('conversation_id');
  console.log(conversation_id);
const [entireResponses, setEntireResponses] = useState([]);
  
  useEffect(() => {
    const fetchConversations = async () => {
      try {
        const foo = await axios.get('http://95.217.184.211:8080/all_conversations');
        setEntireResponses(foo.data);
      } catch (error) {
        console.error('Error fetching conversations:', error);
      }
    };
  
    fetchConversations();
  }, []);


  // useEffect(() => {
  //   let pastConversation = null
  //   if(conversation_id && allConversations.length>0) {
  //   // pastConversation = historyArr[conversation_id]
  //   pastConversation = allConversations.find((conversation) => conversation.conversation_id === conversation_id)
  //   setMessages(pastConversation.messages)
  //   console.log('pastConversation',pastConversation)
  //   }

  //   return () => {
  //     console.log('Cleanup on conversation_id change');
  //   };
  // }, [allConversations]); // Dependency array includes conversation_id

  
  return (
  <>
  <Header>Przewodnik Podatkowy</Header>
  <NavBar />

<Wrapper>
  <HistoryBar allConversations={entireResponses} isHidden={isHidden} setIsHidden={setIsHidden}/>
  <FlexContainer conversation_obj={entireResponses.filter(obj=>obj.conversation_id==conversation_id)[0]} isId={!!conversation_id} conversation_id={conversation_id} isHidden={isHidden} setIsHidden={setIsHidden}>test </FlexContainer>
</Wrapper>
  
  <Layout>
  </Layout>
  </>
  )
}


export const Head = () => <Seo title="Home" />

export default IndexPage
