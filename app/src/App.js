import React, { useState, useEffect } from 'react';
import Container from '@mui/material/Container'
import Box from '@mui/material/Box'
import {SearchBox} from "./download_components/SearchBox" 



export default function App() {
  return <Container maxWidth="sl">
    <SearchBox/>
  </Container>;
}
