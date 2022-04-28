import React, { useState, useEffect } from 'react';
import Container from '@mui/material/Container'
import Box from '@mui/material/Box'
import { SearchBox } from "./download_components/SearchBox"
import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';


export default function App() {
  return <Container maxWidth="sl">
    <SearchBox />
  </Container>;
}