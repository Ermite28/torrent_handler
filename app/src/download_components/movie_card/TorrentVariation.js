import React, {useState, useEffect } from 'react'
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import DownloadIcon from '@mui/icons-material/Download';

import env from "react-dotenv"

export default function TorrentVariations(props){
    const [torrents, setTorrents] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        getMovieTorrents(props.movie).then(torrents => {setTorrents(torrents); console.log(torrents); setLoading(false)})
    }, []);

    function handleNewTorrents(){
        if (loading) {
            return (<Stack spacing={2} direction='row'>
            <Button loading variant="outlined"></Button>
            <Button loading variant="outlined"></Button>
            <Button loading variant="outlined"></Button>
            </Stack>)
        } else {
            return  (<Stack spacing={2} direction='row'>
            <Button variant="outlined">1280p</Button>
            <Button variant="outlined">720p</Button>
            <Button variant="outlined">360p</Button>
            </Stack>)
        }
    }

    return (
    <div>
     {handleNewTorrents()}
    </div>)
}

function getMovieTorrents(movie, site = "yts", limit = 2) {
    return new Promise(function (resolve, reject) {
        fetch(`${env.API_URL}/scrap_by_name/${movie.title}?site=${site}`, {
            method: "GET",
            headers: {
                "Access-Control-Allow-Origin": env.API_URL,
            }
        })
            .then(response => resolve(response.json()))
            .catch(error => console.log(error.txt()))
    })
}
