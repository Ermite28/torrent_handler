import React from "react";
import { styled } from '@mui/material/styles';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Grid from "@mui/material/Grid";
import Typography from '@mui/material/Typography';
import Collapse from '@mui/material/Collapse';
import CardActions from '@mui/material/CardActions';
import IconButton, { IconButtonProps } from '@mui/material/IconButton';
import DownloadIcon from '@mui/icons-material/Download';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import {getMovieTorrents, downloadTorrent} from './api_connectors/torrent_routes';


const ExpandMore = styled((props) => {
    const { expand, ...other } = props;
    return <IconButton {...other} />;
  })(({ theme, expand }) => ({
    transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
    marginLeft: 'auto',
    transition: theme.transitions.create('transform', {
      duration: theme.transitions.duration.shortest,
    }),
  }));

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
                        <CardActions disableSpacing>
                <IconButton aria-label="download" onClick={() => {
                    handleDownloadClick();
                }}>
                <DownloadIcon/>
                </IconButton>
                <ExpandMore
                expand={expanded}
                onClick={handleExpandClick}
                aria-expanded={expanded}
                aria-label="show more"
                >
                <ExpandMoreIcon />
                </ExpandMore>
            </CardActions>
            <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
        <Typography variant="body2" color="text.secondary">{movie.overview}</Typography>
        </CardContent>
      </Collapse>
            </Card>
        </Grid>
    )
}