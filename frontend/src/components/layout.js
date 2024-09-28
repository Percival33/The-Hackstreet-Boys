/**
 * Layout component that queries for data
 * with Gatsby's useStaticQuery component
 *
 * See: https://www.gatsbyjs.com/docs/how-to/querying-data/use-static-query/
 */

import * as React from "react"
import { useStaticQuery, graphql } from "gatsby"
import { Helmet } from 'react-helmet';

import styled, { ThemeProvider, createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body {
    font-family: 'Montserrat', sans-serif;
    font-weight: 400;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    background-color: #f5f7fb;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
`;

const theme = {
  // fonts: {
  //   main: 'Montserrat, sans-serif',
  // },
};

const Layout = ({ children }) => {
  

  return (
    <>
       <Helmet>
        <link
          href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Open+Sans:wght@400;700&display=swap"
          rel="stylesheet"
        />
        </Helmet>
      
        <ThemeProvider theme={theme}>
        <GlobalStyle />
        
          <main>{children}</main>
        
      </ThemeProvider>
        
        <footer
          style={{
            marginTop: `var(--space-5)`,
            fontSize: `var(--font-sm)`,
          }}
        >
         
        </footer>
    
    </>
  )
}

export default Layout
