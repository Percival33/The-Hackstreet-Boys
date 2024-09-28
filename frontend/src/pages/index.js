import * as React from "react"
import { Link } from "gatsby"
import { StaticImage } from "gatsby-plugin-image"
import styled from "styled-components"

import Layout from "../components/layout"
import Seo from "../components/seo"
import * as styles from "../components/index.module.css"

import Header from '../components/styledComponents/header/header'
import NavBar from '../components/styledComponents/navBar/navBar';
import HistoryBar from '../components/styledComponents/historyBar/historyBar';
import FlexContainer from '../containers/CardChat/CardChat';

const utmParameters = `?utm_source=starter&utm_medium=start-page&utm_campaign=default-starter`

const Wrapper = styled.div`
  display: flex;
  flex-direction: row;
   height: 90vh; /* Full height */
  min-height:600px;
  // align-items: center;
  // justify-content: center;

  
  
  `

const IndexPage = () => (
  <>
  <Header>Poradnik podatkowy</Header>
  <NavBar />

<Wrapper>
  <HistoryBar/>
  <FlexContainer >test </FlexContainer>
</Wrapper>
  
  <Layout>
   {/* <h1>test</h1> */}
   {/* <p>tekst</p> */}
  </Layout>
  </>
)

/**
 * Head export to define metadata for the page
 *
 * See: https://www.gatsbyjs.com/docs/reference/built-in-components/gatsby-head/
 */
export const Head = () => <Seo title="Home" />

export default IndexPage
