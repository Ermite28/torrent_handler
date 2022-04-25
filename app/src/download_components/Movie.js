import React from "react";
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Collapse from '@mui/material/Collapse';

export function Movie (props) {
    const {movie, setMovie} = props;

    return (
        <Card sx={{ maxWidth:345}}>
            <CardHeader
                title = {movie.title}/>
            <CardMedia
            compoment="img"
            height="194"
            image={`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`}
            alt="Movie poster"/>
        </Card>
    )
}