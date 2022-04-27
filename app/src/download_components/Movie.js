import React from "react";
import Header from "./movie_card/Header"
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Grid from "@mui/material/Grid";
import Typography from '@mui/material/Typography';
import Collapse from '@mui/material/Collapse';
import {getMovieTorrents, downloadTorrent} from './api_connectors/torrent_routes';


export function Movie(props) {
    const { movie, setMovie } = props;
    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
      setExpanded(!expanded);
    };

    const handleDownloadClick = () => {
        downloadTorrent(movie)
    }
    return (
        <Grid item xs={4}>
            <Card>
                <Header movie={movie} handleExpandClick handleDownloadClick expanded />
            <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
        <Typography variant="body2" color="text.secondary">{movie.overview}</Typography>
        </CardContent>
      </Collapse>
            </Card>
        </Grid>
    )
}