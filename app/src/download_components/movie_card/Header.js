import React from "react";
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardActions from '@mui/material/CardActions';
import DownloadIcon from '@mui/icons-material/Download';
import IconButton, { IconButtonProps } from '@mui/material/IconButton';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { styled } from '@mui/material/styles';

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

export default function Header(props, handleExpandClick, handleDownloadClick, expanded) {
    const [movie, setMovie] = props;

    return (
        <React.Fragment>
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
                <DownloadIcon />
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
        </React.Fragment >
    )
}