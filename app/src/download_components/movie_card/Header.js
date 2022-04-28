import React from "react";
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardActions from '@mui/material/CardActions';
import IconButton, { IconButtonProps } from '@mui/material/IconButton';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { styled } from '@mui/material/styles';
import Modal from "./Popup";


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

export default function Header(props) {
    return (
        <React.Fragment>
            <CardMedia
                style={{
                    width: "100%",
                    minHeight: "200px"
                }}
                compoment="img"
                image={`https://www.themoviedb.org/t/p/w600_and_h900_bestv2${props.movie.poster_path}`}
                alt="Movie poster" />
            <CardHeader
                title={props.movie.title} />
            <CardActions disableSpacing>
                <Modal movie={props.movie}/>
            <ExpandMore
                expand={props.expanded}
                onClick={props.handleExpandClick}
                aria-expanded={props.expanded}
                aria-label="show more"
            >
                <ExpandMoreIcon />
            </ExpandMore>
        </CardActions>
        </React.Fragment >
    )
}