import React, { useState, useEffect } from 'react';
import TextField from '@mui/material/TextField'
import Container from '@mui/material/Container'
import Box from '@mui/material/Box'
import Grid from "@mui/material/Grid";
import ApiConnector from './api_connectors/torrent_routes'
import {Movie} from './Movie'


function SearchBar(props) {
  const [query, setQuery] = useState(
    {
      "query": "",
      "language": "fr-EU"
    }
  )
  
  let apiConnector = new ApiConnector();    
  
  const searchMovies = (searchValue) => {
    setQuery({ ...query, query: searchValue })
    if (query.query.length > 2) {
      apiConnector.searchMovies(query).then((response) => {
        props.updateMovies(response.results)
      })
    }

  }

  return <Container maxWidth="sm">
    <TextField hiddenLabel fullWidth id="filled-hidden-label-large fullWidth" variant="filled" onChange={(e) => searchMovies(e.target.value)} />
  </Container>
}


export function SearchBox() {
  const [movies, setMovies] = useState([])

  const updateMovies = (movies) => {
    setMovies(movies)
  }
  return <Box sx={{
    bgcolor: '#cfe8fc',
    height: '100vh'
  }}>
    <SearchBar updateMovies={updateMovies} />
    <Grid container spacing={0.5}>
      {movies.map((movie) => (<Movie movie={movie}/>))}
    </Grid>
  </Box>
}