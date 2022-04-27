import React, { useState, useEffect } from 'react';
import TextField from '@mui/material/TextField'
import Container from '@mui/material/Container'
import Grid from "@mui/material/Grid";
import {searchMovies} from './api_connectors/torrent_routes'
import { Movie } from './Movie'


function SearchBar(props) {
  const [query, setQuery] = useState(
    {
      "query": "",
      "language": "fr-EU"
    }
  )


  const handleTextChange = (searchValue) => {
    setQuery({ ...query, query: searchValue })
    if (query.query.length > 2) {
      searchMovies(query).then((response) => {
        props.updateMovies(response.results)
      })
    }

  }

  return <Container maxWidth="lg" sx={{
    pb: "50px",
    pt: "10px"
  }}>
    <TextField hiddenLabel autoFocus fullWidth id="filled-hidden-label-large fullWidth" variant="filled" onChange={(e) => handleTextChange(e.target.value)}/>
  </Container>
}


export function SearchBox() {
  const [movies, setMovies] = useState([])

  const updateMovies = (movies) => {
    setMovies(movies)
  }
  return <Container maxWidth="xl" sx={{
    bgcolor: '#cfe8fc',
    height: '100vh'
  }}>
    <SearchBar updateMovies={updateMovies} />
    <Grid container spacing={3}>
      {movies.map((movie) => (<Movie movie={movie} />))}
    </Grid>
  </Container>
}