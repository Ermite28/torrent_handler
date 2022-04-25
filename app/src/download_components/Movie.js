import React from "react";
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Grid from "@mui/material/Grid";
import CardActionArea from '@mui/material/CardActionArea';
import Collapse from '@mui/material/Collapse';

export function Movie(props) {
    const { movie, setMovie } = props;
    return (
        <Grid item>
            <Card sx={{ width: 500, margin: 10 }}>
                <CardActionArea>
                        <CardMedia
                            style={{
                                width: "100%",
                                minHeight: "200px"
                            }}
                            compoment="img"
                            image={`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${movie.poster_path}`}
                            alt="Movie poster" />
                        <CardHeader
                            title={movie.title} />
                        <CardContent>
                            {movie.overview}
                        </CardContent>
                </CardActionArea>
            </Card>
        </Grid>
    )
}