import DownloadIcon from '@mui/icons-material/Download';
import IconButton, { IconButtonProps } from '@mui/material/IconButton';
import Popup from 'reactjs-popup';
import Typography from '@mui/material/Typography';
import TorrentVariations from './TorrentVariation';


export default function Modal(props) {
    return (
        <Popup
  trigger={<IconButton aria-label="download">
    <DownloadIcon />
</IconButton>}
  modal
  nested
>
  {close => (
    <div className="modal">
      <button className="close" onClick={close}>
        &times;
      </button>
      <Typography variant="h2"> {props.movie.title} </Typography>
      <Typography >
        {props.movie.overview}
      </Typography>
      <hr/> 
    <TorrentVariations movie={props.movie} />
    </div>
  )}
</Popup>
    )
} 