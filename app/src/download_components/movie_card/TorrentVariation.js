import React, { useState, useEffect } from 'react'
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import DownloadIcon from '@mui/icons-material/Download';

import env from "react-dotenv"

export default function TorrentVariations(props) {
    const [torrents, setTorrents] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        getMovieTorrents(props.movie).then(torrents => { setTorrents(torrents); setLoading(false) })
    }, []);

    function handleNewTorrents() {
        if (loading) {
            return ("Loading ...")
        } else {
            return (<Stack spacing={2} direction='row'>
                {torrents['torrents'].map((o, i) => <Button variants='outlined' key={i} onClick={() => handleClick(i)}><DownloadIcon />{o['quality']}</Button>)}
            </Stack>)
        }
    }
    function handleClick(id) {
        downloadTorrent(torrents['torrents'][id])
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

function downloadTorrent(torrent) {
    let requestOptions = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": env.API_URL,
        },
        body: JSON.stringify(torrent),
        redirect: 'follow',
    };
    fetch(`${env.API_URL}/new_torrent/`, requestOptions).then(response => response.text()
        .then(result => console.log(result))
        .catch(error => console.log(error)))
}